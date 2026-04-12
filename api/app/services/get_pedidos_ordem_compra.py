import pandas as pd
import redis
import json
import os

GOLD_PATH = os.getenv("GOLD_PATH", "/data/gold/pedidos_ordem_compras")

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_all_pedidos_ordem_compra():
    # tenta cache
    cache = r.get("pedidos_ordem_compras")

    if cache:
        print("🔥 vindo do Redis")
        return json.loads(cache)

    print("📂 lendo parquet")

    df = pd.read_parquet(GOLD_PATH)
    df = df.astype(str)
    data = df.to_dict(orient="records")

    # salva no cache (TTL 60 segundos)
    r.setex("pedidos_ordem_compras", 60, json.dumps(data))

    return data