from locust import HttpUser, task, between
from random import randint


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # locust will wait 1~5 seconds between each tasks

    # (2): is weight.
    @task(2)
    def view_products(self):
        print('View Products')
        collection_id = randint(2, 6)
        self.client.get(f"/store/products/?collection_id={collection_id}", name='/store/products')
        # with self.client we can send http request to server

    @task(4)
    def view_product(self):
        print('View Product Detail')
        collection_id = randint(2, 6)
        self.client.get(f"/store/products/{collection_id}", name='/store/products/:id')

    @task(1)
    def add_to_cart(self):
        print('Add To Cart')
        # we want to check if updating product quantity cause performance issue
        product_id = randint(1, 10)
        self.client.post(
            f'/store/carts/{self.cart_id}/items/',
            name='/store/carts/items',
            json={'product_id': product_id, 'quantity': 1}
        )
        # here we need cart id and it should be generated when the user start browsing our website
        # for that we have special method called on_start

    @task
    def say_hello(self):
        self.client.get('/playground/hello/')

    # def on_start(self):
    #     # It's not a task it's life cycle hook
    #     response = self.client.post('/store/carts/')
    #     result = response.json()
    #     self.cart_id = result['id']
    def on_start(self):
        response = self.client.post('/store/carts/')
        result = response.json()
        self.cart_id = result['id']
