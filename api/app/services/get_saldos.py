import redis
import json

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_all_saldos():
    data = r.lrange("saldos_oc", 0, -1)

    if not data:
        return {"error": "dados não disponíveis no cache"}

    return [json.loads(item) for item in data]