import json

from langchain_community.llms.huggingface_endpoint import HuggingFaceEndpoint
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate

input = "PROVINSIDKIJAKARTA JAKARTA BARAT IK 3172011411890004 ama FIRMAN GUNAWAN empat/Tgll Lahir JAKARTA, 14-11-1989 nis kelamin LAKI-LAKI Gol. Darah A amat PERMATA TAMAN PALEM BLOK D-2/19 RT/RW 005/003 Kel/Desa PEGADUNGAN Kecamatan : KALIDERES jama : KRISTEN atus Perkawinan: BELUM KAWIN JAKARTA BARAT kerjaan : KARYAWAN SWASTA 12-02-2016 warganegaraan: WNI rlaku Hingga : SEUMUR HIDUP fue"

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
