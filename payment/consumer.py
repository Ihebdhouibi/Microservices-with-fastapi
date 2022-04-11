from main import redis, Order
import time

key = 'refund-order'
group = "payment-group"

try:
    redis.xgroup_create(key, group)
except:
    print("Group already exist!")

# Consume events loop
while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
        if results:
            for result in results:
                obj =result[1][0][1]
                order = Order.get(obj['pk'])
                order.status = 'Refunded'
                order.save()
    except Exception as e:
        print("There an error consuming events: \n "+str(e))
    time.sleep(1)