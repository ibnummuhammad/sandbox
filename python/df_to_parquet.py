import pandas as pd


df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
print("original...")
print(df)
print(df.dtypes)

df = df.astype(
    {
        "col1": str,
        "col2": str,
    }
)
print("\nconvert_to_str...")
print(df)
print(df.dtypes)

df.to_parquet("df.parquet.gzip", compression="gzip")
df_output = pd.read_parquet("df.parquet.gzip")
print("\nto_parquet...")
print(df_output)
print(df_output.dtypes)

df.to_csv("checkable_pd.csv", index=False)
df_csv = pd.read_csv("checkable_pd.csv")
print("\nto_csv...")
print(df_csv)
print(df_csv.dtypes)
