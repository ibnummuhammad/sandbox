import json
import yaml


data_yaml = """
version: 2

sources:
  - name: data_lake
    tables:
      - name: disposable_email_domains
        description: domains data from github disposal email
        meta:
          owner: "benski"
          dag_dependency:
            name: disposable-email-pipeline
            allowed_states:
              - success
              - failed
            failed_states:
            timeout: 21600
        columns:
          - name: params
            description: parameters to get data.
          - name: payload
            description: domain data from source.
          - name: etl_id
            description: Id of etl process to identify whether the data was successfully updated to H-1. Format YYYY-MM-DD-HH
            tests:
              - dbt_expectations.expect_column_to_exist
          - name: etl_id_ts
            description: Timestamp of etl process for this data (in UTC)
            tests:
              - dbt_expectations.expect_column_to_exist
          - name: etl_id_partition
            description: Parition of etl id
            tests:
              - dbt_expectations.expect_column_to_exist
          - name: run_ts
            description: Parition of run ts
"""  # noqa: E501

data_dict = yaml.load(data_yaml, Loader=yaml.FullLoader)
data_json = json.dumps(data_dict, indent=2)
print(data_json)
