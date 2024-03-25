import pandas as pd


df = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
df.to_parquet('df.parquet.gzip', compression='gzip')
df_output = pd.read_parquet('df.parquet.gzip')
print(df_output)
