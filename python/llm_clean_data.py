from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import pandas as pd


REPO_ID = "mistralai/Mixtral-8x7B-Instruct-v0.1"
TEMPLATE = """
### OBJECTIVE ###
Your task is to classify the input value based on examples below.

### EXAMPLES ###
<input>: Saya sangat menyukai film ini!
<classification>: Positive

<input>: Filmnya ga seru!
<classification>: Negative

<input>: Bosenin banget filmnya
<classification>: Negative

<input>: Film yang bagus untuk ditonton bersama keluarga
<classification>: Positive

<input>: Film yang menyenangkan
<classification>: Positive

### USER INPUT ###
<input>: {input}

### OUTPUT ###
<classification>: 
"""  # noqa E501

df = pd.read_csv("csv/2024-04-03-19-29-42_result.csv")
df_new = df[["account_type", "url", "description"]].copy()
df_new_v2 = df_new[df_new["url"].str.contains("datascienceindo")]

llm = HuggingFaceEndpoint(repo_id=REPO_ID, temperature=0.1)
prompt = PromptTemplate.from_template(TEMPLATE)
llm_chain = LLMChain(prompt=prompt, llm=llm)

for i in range(0, 1):
    input = df_new.iloc[i]["description"]
    llm_response = llm_chain.invoke("Filmnya asik")
    print(llm_response)
