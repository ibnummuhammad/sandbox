import json
import os

from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

input = "hello!"

template = """### Instruction ###
Translate the text below to Spanish:

Text: '{input}'

Answer:"""

prompt = PromptTemplate.from_template(template)

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.5)
llm_chain = LLMChain(prompt=prompt, llm=llm)
llm_response = llm_chain.invoke(input)
print(json.dumps(llm_response, indent=2))
