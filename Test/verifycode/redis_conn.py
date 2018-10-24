import redis


from config import REDIS_CONF


redis_conn_info = REDIS_CONF.get('produce_redis')


def operator_status(func):
    def gen_status(*args, **kwargs):
        error, result = None, None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            error = str(e)

        return {'result': result, 'error': error}

    return gen_status


class RedisCache(object):
    def __init__(self):
        if not hasattr(RedisCache, 'pool'):
            RedisCache.create_pool()
        self._connection = redis.Redis(connection_pool=RedisCache.pool)

    @staticmethod
    def create_pool():
        if redis_conn_info['pwd']:
            RedisCache.pool = redis.ConnectionPool(
                host=redis_conn_info['host'],
                port=redis_conn_info['port'],
                db=redis_conn_info['db_id'],
                password=redis_conn_info['pwd'])
        else:
            RedisCache.pool = redis.ConnectionPool(
                host=redis_conn_info['host'],
                port=redis_conn_info['port'],
                db=redis_conn_info['db_id'])

    @operator_status
    def set_data(self, key, value):
        return self._connection.set(key, value)

    @operator_status
    def set_data_expire(self, key, value):
        self._connection.set(key, value)
        return self._connection.expire(key, 1800)

    @operator_status
    def get_data(self, key):
        return self._connection.get(key)

    @operator_status
    def del_data(self, key):
        return self._connection.delete(key)

    @operator_status
    def get_lpop(self, key):
        return self._connection.lpop(key)

    @operator_status
    def get_rpop(self, key):
        return self._connection.rpop(key)

    @operator_status
    def set_lpush(self, key, value):
        return self._connection.lpush(key, value)

    @operator_status
    def set_rpush(self, key, value):
        return self._connection.rpush(key, value)

    @operator_status
    def set_rpush_expire(self, key, value):
        self._connection.rpush(key, value)
        return self._connection.expire(key, 3600)

    @operator_status
    def get_list_len(self, key):
        return self._connection.llen(key)

    @operator_status
    def set_add(self, key, value):
        self._connection.sadd(key, value)
        return self._connection.expire(key, 3600)

    @operator_status
    def set_ismembers(self, key, value):
        return self._connection.sismember(key, value)


if __name__ == '__main__':
    print(RedisCache().set_data('Testkey', "Simple Test"))
    print(RedisCache().get_data('Testkey'))
    print(RedisCache().del_data('Testkey'))
    print(RedisCache().get_data('Testkey'))
    print(RedisCache().set_rpush('Test', {1: "test", 2: "88888"}))
    # a = RedisCache().get_rpop('Test')
    # 转为字典
    # b = eval(a['result'])
    # print(b)
