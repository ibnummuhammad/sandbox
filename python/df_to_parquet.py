import pandas as pd


df = pd.DataFrame(data={"col1": [1, 2], "col2": [3, 4]})
print(df)
print(df.dtypes)

df = df.astype(
    {
        "col1": str,
        "col2": str,
    }
)
print(df)
print(df.dtypes)

df.to_parquet("df.parquet.gzip", compression="gzip")
df_output = pd.read_parquet("df.parquet.gzip")
print(df_output)
print(df_output.dtypes)
