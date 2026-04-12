def clear_cache(table_name: str):
    import redis
    r = redis.Redis(host="redis", port=6379)
    r.delete(table_name)