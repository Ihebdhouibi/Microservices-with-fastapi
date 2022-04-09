from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host="redis-11349.c135.eu-central-1-1.ec2.cloud.redislabs.com",
    port=11349,
    password="fvCn9Ug0pkAv480mBMlf1kd8oa90JpJ1",
    decode_responses=True,
)

