from main import redis, Product
import time


key = "order_completed"
group = "inventory-group"

try:
    redis.xgroup_create(key, group)
except:
    print("Group already exists!")

# Consume events loop
while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)# '>' to read all events
        if results:
            for result in results:
                obj = result[1][0][1]
                try:
                    product = Product.get(obj['product_id'])
                    if product:
                        product.quantity -= int(obj['quantity'])
                        product.save()

                except:
                    print("Product is deleted")
                    redis.xadd('refund-order', obj, '*')
    except Exception as e:
        print("There is an error consuming event : \n "+str(e))
    time.sleep(1)
