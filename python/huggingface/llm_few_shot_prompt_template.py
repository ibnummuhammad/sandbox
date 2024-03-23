import json
import os

from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate


# create our examples
examples = [
    {"query": "How are you?", "answer": "I can't complain but sometimes I still do."},
    {"query": "What time is it?", "answer": "It's time to get a watch."},
]

# create a example template
example_template = """
User: {query}
AI: {answer}
"""

# create a prompt example from above template
example_prompt = PromptTemplate(
    input_variables=["query", "answer"], template=example_template
)

# now break our previous prompt into a prefix and suffix
# the prefix is our instructions
prefix = """The following are exerpts from conversations with an AI
assistant. The assistant is typically sarcastic and witty, producing
creative  and funny responses to the users questions. Here are some
examples: 
"""

# and the suffix our user input and output indicator
suffix = """
User: {query}
AI: """

# now create the few shot prompt template
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=["query"],
    example_separator="\n\n",
)

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.5)

query = "What is the meaning of life?"

llm_chain = LLMChain(prompt=few_shot_prompt_template, llm=llm)
llm_response = llm_chain.invoke(query)
print(json.dumps(llm_response, indent=2))
