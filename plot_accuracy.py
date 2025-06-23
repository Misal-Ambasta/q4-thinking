import json
import matplotlib.pyplot as plt

# Load accuracy data
with open('accuracy.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

methods = ['Single Run', 'Majority Vote']
accuracies = [data['single_run_accuracy'], data['majority_vote_accuracy']]

plt.figure(figsize=(6, 4))
plt.bar(methods, accuracies, color=['skyblue', 'orange'])
plt.ylim(0, 1)
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison: Single Run vs Majority Vote')
plt.savefig('accuracy.png')
plt.close() 