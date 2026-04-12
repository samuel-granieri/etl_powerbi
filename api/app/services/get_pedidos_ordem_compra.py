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


    return {"error": "dados não disponíveis no cache"}