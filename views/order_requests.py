ORDERS = [
     {
      "id": 1,
      "styleId": 2,
      "sizeId": 1,
      "metalId": 3
    },
    {
      "id": 2,
      "styleId": 2,
      "sizeId": 1,
      "metalId": 4
    },
    {
      "id": 3,
      "styleId": 1,
      "sizeId": 1,
      "metalId": 1
    }
]

def get_all_orders():
    return ORDERS

def get_single_order(id):
   
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    last_order = ORDERS[-1]["id"]
    new_id = last_order + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def delete_order(id):
    order_index = -1
    for index, order in enumerate(ORDERS):
        if id == order["id"]:
            order_index = index
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
