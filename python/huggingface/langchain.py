from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate

model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
template = "<s>[INST] {question} [/INST]"

client = InferenceClient(model_id)

prompt = PromptTemplate.from_template(template)
print(prompt)
