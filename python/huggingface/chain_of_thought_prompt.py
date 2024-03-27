import json

from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

input = "PROVINSI DKI JAKARTA JAKARTA SELATAN IK 3174073007960007 na : DIMAS RADITYO npat/Tgl Lahir : JAKARTA, 30-07-1996 is kelamin : LAKI-LAKI Gol. Darah :0 mat : JL.RADIO IV NO.2 RT/RW 001/004 Kel/Desa : KRAMAT PELA Kecamatan : KEBAYORAN BARU ma : ISLAM us Perkawinan: KAWIN erjaan : KARYAWAN SWASTA JAKARTA SELATAN arganegaraan: WNI 27-12-2021 aku Hingga : SEUMUR HIDUP"

template = """### INSTRUCTIONS ###
I have a text data that I got from doing an OCR to Indonesian ID Card (KTP or Kartu Tanda Penduduk). You must convert the text into a structured format. The structured output must be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":

The OCR result might not be complete and contains some typo, but you must adhere to these 15 keys above and leave it empty if you can't detect the keys. I will give you the text data and you MUST only return the JSON in a code snippet & nothing else.

### USER INPUT ###
{input}"""

prompt = PromptTemplate.from_template(template)

repo_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(repo_id=repo_id, temperature=0.5)
llm_chain = LLMChain(prompt=prompt, llm=llm)
llm_response = llm_chain.invoke(input)
print(json.dumps(llm_response, indent=2))
print(json.dumps(llm_response["text"], indent=2))
