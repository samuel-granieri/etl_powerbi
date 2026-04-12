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

    return {"error": "dados não disponíveis no cache"}