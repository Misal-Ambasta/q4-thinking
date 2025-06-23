# Q4-Thinking: Chain-of-Thought Sampler

## Overview
This project explores chain-of-thought reasoning and self-consistency in language models using GRE-style arithmetic word problems. The script prompts a model, collects multiple completions, extracts answers, and compares the accuracy of single deterministic runs versus majority voting.

## Features
- Prompts the model with GRE-style arithmetic word problems
- Generates 10 completions per problem with temperature=1.1 ("Let's think step-by-step.")
- Extracts numerical answers and performs a majority vote
- Compares accuracy with a single deterministic run (temperature=0)
- Outputs results and a comparison plot

## Files
- `self_consistency.py`: Main script for running the experiment
- `problems.json`: List of 10 GRE-style arithmetic word problems
- `plot_accuracy.py`: Script to generate a bar plot comparing accuracies
- `accuracy.png`: Bar plot comparing single run and majority vote accuracy
- `self_consistency_results.json`: Detailed results for each problem
- `accuracy.json`: Accuracy values for both methods
- `.env`: (Not tracked) Store your OpenAI API key as `OPENAI_API_KEY=your_key_here`
- `.gitignore`: Ignores sensitive and output files

## Setup
1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install openai python-dotenv matplotlib
   ```
3. **Add your OpenAI API key** to a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage
1. **Run the main experiment:**
   ```bash
   python self_consistency.py
   ```
   This will generate `self_consistency_results.json` and `accuracy.json`.
2. **Generate the accuracy plot:**
   ```bash
   python plot_accuracy.py
   ```
   This will create `accuracy.png`.

## Deliverables
- `self_consistency.py`
- `problems.json`
- `accuracy.png`

## License
MIT