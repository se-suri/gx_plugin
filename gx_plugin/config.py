import yaml
from pathlib import Path

def load_config(path="gx_config.yml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)