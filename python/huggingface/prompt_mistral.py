import os
import openai
from openai import OpenAI
import pandas as pd


ktp_ocr_data = pd.read_csv("~/Downloads/ktp_ocr_data_20240319 (3).csv")
ktp_ocr_data = ktp_ocr_data[["user_id", "ocr_text"]]
print(ktp_ocr_data.count())

ktp_ocr_data_1 = ktp_ocr_data.iloc[:1000].reset_index(drop=True)
ktp_ocr_data_2 = ktp_ocr_data.iloc[1000:2000].reset_index(drop=True)
ktp_ocr_data_3 = ktp_ocr_data.iloc[2000:3000].reset_index(drop=True)
ktp_ocr_data_4 = ktp_ocr_data.iloc[3000:].reset_index(drop=True)
