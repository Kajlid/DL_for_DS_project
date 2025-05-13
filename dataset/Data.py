import os
import requests

dataset_file_origin = 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'
save_path = os.path.join('dataset', 'shakespeare.txt')

response = requests.get(dataset_file_origin)
response.raise_for_status()

with open(save_path, 'w', encoding='utf-8') as f:
    f.write(response.text)
    
print(f"Saved dataset to {save_path}")

with open(save_path, 'r', encoding='utf-8') as f:
    text_data = f.read()

print(f"Dataset length: {len(text_data)} characters")
print("Preview:\n")
print(text_data[:500])