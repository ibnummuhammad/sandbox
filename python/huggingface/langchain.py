import numpy as np
import pandas as pd

import torch
from transformers import (
    BitsAndBytesConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    GenerationConfig,
    pipeline,
)

# Model version of Mistral
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

# Quantization is a technique used to reduce the memory and computation requirements
# of deep learning models, typically by using fewer bits, 4 bits
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

# Initialization of a tokenizer for the Mistral-7b model,
# necessary to preprocess text data for input
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=True)
tokenizer.pad_token = tokenizer.eos_token
print(tokenizer)
