
import yaml
with open("etl_config.yaml") as stream:
    try:
        etl_config = (yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)