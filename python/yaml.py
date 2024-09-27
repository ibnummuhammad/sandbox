import glob


files = glob.glob(
    "/Users/ibnu.muhammad/Documents/tiptip/data-transformation/staging/models/data_lake/**/*",
    recursive=True,
)
print(len(files))
