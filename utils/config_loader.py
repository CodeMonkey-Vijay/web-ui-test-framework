from pydantic import BaseModel
import yaml, os

class Config(BaseModel):
    base_url: str
    default_city: str

def load_config(env="dev") -> Config:
    path = f"config_{env}.yaml"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Config file {path} not found")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return Config(**data)
