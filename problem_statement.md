# Q: 4 "Thinking Mode" Sampler
## Goal: Explore chain-of-thought reasoning + self-consistency.

## Task
Write a script that:

    - Prompts the model with a GRE-style arithmetic word problem.
    - Generates 10 completions using temperature=1.1, each including "Let's think step-by-step."
    - Extracts the numerical answer from each completion.
    - Performs a majority vote over the 10 answers.
## Evaluation
Compare accuracy on 10 problems using:

    - (a) Single deterministic run (temperature=0)
    - (b) Majority vote (from your script)

## Deliverables
    - self_consistency.py
    - problems.json
    - accuracy.png