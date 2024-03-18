from transformers import AutoTokenizer
import transformers
import torch

model = "mistralai/Mixtral-8x7B-Instruct-v0.1"

tokenizer = AutoTokenizer.from_pretrained(model)
print(tokenizer)
