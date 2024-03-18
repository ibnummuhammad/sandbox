from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")

template = "<s>[INST] tell me a joke [/INST]"

prompt = PromptTemplate.from_template(template)
print(prompt)
