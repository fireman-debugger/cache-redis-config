enum CacheType {
  REDIS_CLUSTER = 'redis_cluster',
  REDIS_SENTINEL = 'redis_sentinel',
  REDIS_SINGLE = 'redis_single',
}

enum CacheError {
  MISS = 'MISS',
  HIT = 'HIT',
  EXPIRED = 'EXPIRED',
  NOT_FOUND = 'NOT_FOUND',
  EMPTY = 'EMPTY',
}

type CacheConfig = {
  host: string;
  port: number;
  password?: string;
  db?: number;
  maxIdle?: number;
  maxActive?: number;
  minIdle?: number;
  testOnBorrow?: boolean;
  testOnReturn?: boolean;
  testWhileIdle?: boolean;
  timeBetweenEvictionRunsMillis?: number;
  numTestsPerEvictionRun?: number;
  minEvictableIdleTimeMillis?: number;
  softMinEvictableIdleTimeMillis?: number;
  numLifecycleEventsPerConnection?: number;
  testOnConnect?: boolean;
  testOnBorrow?: boolean;
  validationQuery?: string;
  validationQueryTimeout?: number;
  validationQueryTimeoutUnit?: 'MILLISECONDS' | 'SECONDS';
};

type RedisClientConfig = {
  host: string;
  port: number;
  password?: string;
  db?: number;
};

type RedisHash = {
  field: string;
  value: string;
  expire?: number;
};

type Options = {
  // cache
  cacheType?: CacheType.REDIS_CLUSTER | CacheType.REDIS_SENTINEL | CacheType.REDIS_SINGLE;
  cachePrefix?: string;
  cacheMaxConnect?: number;
  cacheMaxIdle?: number;
  cacheIdleTimeout?: number;
  cacheFailover?: boolean;

  // redis
  redisHost?: string;
  redisPort?: number;
  redisPassword?: string;
  redisDb?: number;
};