
def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert product['price']*.5 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 500}
print(apply_discount(shoes,.6))