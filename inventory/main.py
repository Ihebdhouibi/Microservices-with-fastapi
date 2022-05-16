from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
from pydantic import BaseModel

app = FastAPI()

# Allow front client to use API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*'],
)

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


@app.get('/products')
def get_all_products():
    """
    This function will return the primary keys of all the products stored in our database
    :return:
    """
    return [format(k) for k in Product.all_pks()]

def format(pk: str):
    """
    :arg
        pk : Primary key of a product, of type string.

    returns: a dict containing product attributes
    """
    product = Product.get(pk)

    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.quantity,
    }


@app.post('/products')
def create_product(product: Product):
    """
    :arg:
        Product : An instance of Product class.
    :return:
    """
    return product.save()


@app.get('/products/{pk}')
def get_product(pk: str):
    """
    :arg:
        pk : string containing the primary key of a product.

    returns:
        The product of the given primary key.
    """
    return Product.get(pk)


@app.delete('/products/{pk}')
def delete_product(pk: str):
    """
    :arg:
        pk : string containing the primary key of a product.

    returns:

    """
    return Product.delete(pk)


