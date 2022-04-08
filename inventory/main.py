from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel

redis = get_redis_connection(
    host="redis-11349.c135.eu-central-1-1.ec2.cloud.redislabs.com",
    port=11349,
    password="fvCn9Ug0pkAv480mBMlf1kd8oa90JpJ1",
    decode_responses=True,
)


# This class will generate models that will be converted to redis tables.
class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


