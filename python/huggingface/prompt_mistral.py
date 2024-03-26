import os
import openai
from openai import OpenAI
import pandas as pd


ktp_ocr_data = pd.read_csv("~/Downloads/ktp_ocr_data_20240319 (3).csv")
ktp_ocr_data = ktp_ocr_data[["user_id", "ocr_text"]]

ktp_ocr_data_0 = ktp_ocr_data.iloc[:1].reset_index(drop=True)
ktp_ocr_data_1 = ktp_ocr_data.iloc[:1000].reset_index(drop=True)
ktp_ocr_data_2 = ktp_ocr_data.iloc[1000:2000].reset_index(drop=True)
ktp_ocr_data_3 = ktp_ocr_data.iloc[2000:3000].reset_index(drop=True)
ktp_ocr_data_4 = ktp_ocr_data.iloc[3000:].reset_index(drop=True)

print(ktp_ocr_data_0)

system_prompt = """
### INSTRUCTIONS ###
I have a text data that I got from doing an OCR to Indonesian ID Card (KTP or Kartu Tanda Penduduk). You must convert the text into a structured format. The structured output must be a markdown code snippet formatted in the following schema, including the leading and trailing "```json" and "```":

```json
{
  "Provinsi":string
  "Kota/Kabupaten":string
  "NIK":int
  "Nama":string
  "Tempat/Tgl Lahir":string
  "Jenis Kelamin":string
  "Alamat":string
  "RT/RW":string
  "Kel/Desa":string
  "Kecamatan":string
  "Agama":string
  "Status Perkawinan":string
  "Pekerjaan":string
  "Kewarganegaraan":string
  "Berlaku Hingga":string
}
```

The OCR result might not be complete and contains some typo, but you must adhere to these 15 keys above and leave it empty if you can't detect the keys. I will give you the text data and you MUST only return the JSON in a code snippet & nothing else.

### USER INPUT ###
"""

messages_0 = []
messages_0.append(
    [
        {"role": "system", "content": f"{system_prompt}"},
        {"role": "user", "content": f"{ktp_ocr_data_1['ocr_text'][0]}"},
    ]
)
print(messages_0)
