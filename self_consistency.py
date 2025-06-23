import json
import re
from collections import Counter
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

MODEL_NAME = "gpt-3.5-turbo"  # or another model if desired

PROMPT_SUFFIX = " Let's think step-by-step."


def load_problems(filename="problems.json"):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_number(text):
    # Extract the last number in the text (assume it's the answer)
    numbers = re.findall(r"[-+]?[0-9]*\.?[0-9]+", text)
    return numbers[-1] if numbers else None

def get_completions(problem, n=10, temperature=1.1):
    messages = [{"role": "user", "content": problem + PROMPT_SUFFIX}]
    responses = []
    for _ in range(n):
        response = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=temperature,
            max_tokens=128,
        )
        responses.append(response.choices[0].message.content)
    return responses

def majority_vote(answers):
    count = Counter(answers)
    most_common = count.most_common(1)
    return most_common[0][0] if most_common else None

def get_single_completion(problem, temperature=0):
    messages = [{"role": "user", "content": problem + PROMPT_SUFFIX}]
    response = openai.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=temperature,
        max_tokens=128,
    )
    return response.choices[0].message.content

def main():
    problems = load_problems()
    results = []
    single_run_correct = 0
    majority_vote_correct = 0
    # Add ground truth answers for evaluation
    # You may want to update this with actual answers
    ground_truth = {
        1: "150",
        2: "5",
        3: "25",
        4: "40",
        5: "12",
        6: "80",
        7: "5",
        8: "230",
        9: "6",
        10: "19"
    }
    for prob in problems:
        print(f"Problem: {prob['question']}")
        # (a) Single deterministic run
        single_completion = get_single_completion(prob['question'])
        single_answer = extract_number(single_completion)
        print(f"Single run answer: {single_answer}")
        # (b) Majority vote
        completions = get_completions(prob['question'])
        answers = [extract_number(c) for c in completions]
        voted = majority_vote([a for a in answers if a is not None])
        print(f"Majority vote answer: {voted}\n")
        # Evaluate
        gt = ground_truth.get(prob["id"])
        if single_answer == gt:
            single_run_correct += 1
        if voted == gt:
            majority_vote_correct += 1
        results.append({
            "id": prob["id"],
            "question": prob["question"],
            "single_answer": single_answer,
            "majority": voted,
            "ground_truth": gt,
            "single_correct": single_answer == gt,
            "majority_correct": voted == gt
        })
    # Save results
    with open("self_consistency_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)
    # Print and save accuracy
    single_acc = single_run_correct / len(problems)
    majority_acc = majority_vote_correct / len(problems)
    print(f"Single run accuracy: {single_acc:.2f}")
    print(f"Majority vote accuracy: {majority_acc:.2f}")
    with open("accuracy.json", "w", encoding="utf-8") as f:
        json.dump({"single_run_accuracy": single_acc, "majority_vote_accuracy": majority_acc}, f, indent=2)

if __name__ == "__main__":
    main() 