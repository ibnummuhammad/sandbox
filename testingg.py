import glob
import yaml


DATA_LIST = []

files_path = glob.glob(
    "/Users/ibnu.muhammad/Documents/tiptip/data-transformation/staging/models/data_lake/**/*",
    recursive=True,
)
for file_path in files_path:
    file_name = file_path.split("/", -1)[-1]
    file_extension = file_name.split(".", -1)[-1]
    if file_extension in ["yml", "yaml"]:
        with open(file_path, "r") as file:
            file_json = yaml.load(file, Loader=yaml.FullLoader)
            if "meta" in list(file_json["sources"][0]["tables"][0].keys()):
                if "dag_dependency" in list(
                    file_json["sources"][0]["tables"][0]["meta"].keys()
                ):
                    if file_json["sources"][0]["tables"][0]["meta"][
                        "dag_dependency"
                    ].get("airflow"):
                        DATA_LIST.append(file_name)

print(DATA_LIST)
