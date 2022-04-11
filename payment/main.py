from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks
from redis_om import get_redis_connection, HashModel
from starlette.requests import Request
import requests, time

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


class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str  # pending - completed - refunded

    class Meta:
        database = redis


@app.get('/orders/{pk}')
def get_order(pk: str):
    return Order.get(pk)


@app.post('/orders')
async def create_order(request: Request, background_tasks: BackgroundTasks):
    """:arg
    """
    body = await request.json()

    req = requests.get('http://localhost:8000/products/%s' % body['id'])
    product = req.json()

    order = Order(
        product_id=body['id'],
        price=product['price'],
        fee=0.15 * product['price'],
        total=1.15 * product['price'],
        quantity=body['quantity'],
        status='pending',
    )
    order.save()

    background_tasks.add_task(order_Completed, order)

    return order


def order_Completed(order: Order):
    time.sleep(5)
    order.status = 'Completed'
    order.save()
    redis.xadd('order_completed', order.dict(), '*')
