import yaml, os, re

def resolve_env_vars(config):
    if isinstance(config, dict):
        return {k: resolve_env_vars(v) for k, v in config.items()}
    elif isinstance(config, list):
        return [resolve_env_vars(i) for i in config]
    elif isinstance(config, str):
        return re.sub(r'\$\{(\w+)\}', lambda m: os.environ.get(m.group(1), m.group(0)), config)
    return config

def load_config(path: str = "config/config.yaml") -> dict:
    with open(path) as f:
        return resolve_env_vars(yaml.safe_load(f))