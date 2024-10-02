import glob
import yaml


YAML_FILES = []

YAML_FILES_PATH = glob.glob(
    "/Users/ibnu.muhammad/Documents/tiptip/data-transformation/staging/models/data_lake/**/*",
    recursive=True,
)
for file_path in YAML_FILES_PATH:
    file_name = file_path.split("/", -1)[-1]
    file_extension = file_name.split(".", -1)[-1]
    if file_extension in ["yml", "yaml"]:
        with open(file_path, "r") as file:
            file_json = yaml.load(file, Loader=yaml.FullLoader)
            if "meta" in list(file_json["sources"][0]["tables"][0].keys()):
                if "job" in list(file_json["sources"][0]["tables"][0]["meta"].keys()):
                    YAML_FILES.append(file_name)

print(YAML_FILES)
