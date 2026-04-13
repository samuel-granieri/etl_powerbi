import redis
import json

r = redis.Redis(host="redis", port=6379)

def save_to_redis(df, table_name):

    #limpar cache
    r.delete(table_name)

    pipe = r.pipeline()

    for row in df.toLocalIterator():
        pipe.rpush(table_name, json.dumps(row.asDict(), default=str))

    pipe.execute()

    print(f"✅ Tabela {table_name} salva no Redis")