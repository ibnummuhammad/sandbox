import os
import openai
from openai import OpenAI
import pandas as pd


ktp_ocr_data = pd.read_csv("~/Downloads/ktp_ocr_data_20240319 (3).csv")
print(ktp_ocr_data)
