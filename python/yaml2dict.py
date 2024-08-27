import yaml


data_yaml = """
dag:
  default_args:
    owner: 
  slack_id: 
kubeflow:
  external_task_sensor:
    allowed_states:
      - asdfas
      - asdfdf
    failed_states:
    deferrable: true
"""
data_dict = yaml.load(data_yaml, Loader=yaml.FullLoader)
print(data_dict)
