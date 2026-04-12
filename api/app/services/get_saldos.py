import pandas as pd
import redis
import json
import os

GOLD_PATH = os.getenv("GOLD_PATH", "/data/gold/saldos_oc")

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_all_saldos():
    # tenta cache
    cache = r.get("saldos_all")

    if cache:
        print("🔥 vindo do Redis")
        return json.loads(cache)

    print("📂 lendo parquet")

    df = pd.read_parquet(GOLD_PATH)
    df = df.astype(str)
    data = df.to_dict(orient="records")

    # salva no cache (TTL 60 segundos)
    r.setex("saldos_all", 60, json.dumps(data))

    return data