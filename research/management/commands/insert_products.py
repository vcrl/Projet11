from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
import requests
from ...models import Product, Category, Substitute

class Command(BaseCommand):
    help = "Script d'ajout des produits en base de donnée."

    def __init__(self):
        self.api_url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
    
    def handle(self, *args, **kwargs):

        self.categories = [
            "Boissons",
            "Snacks",
            "Epicerie",
            "Conserves",
            "Desserts"
        ]

        self.insert_category_in_db()
        categories = Category.objects.all()
        for category in categories:
            products = self.get_products(category.name)
            self.insert_products_in_db(products, category)

    def get_products(self, category):
        payload = {
                'action': 'process',
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category,
                'tagtype_1': 'nutrition_grade',
                'tag_contains_1': 'contains',
                'page_size': 100,
                'json': '1',
                }

        response = requests.get(self.api_url, params=payload)
        response_as_json = response.json()
        product_to_add = []
        for product in response_as_json['products']:
            try:
                product_values = {
                    "name": product['product_name'],
                    "brand": product['brands'],
                    "category": category,
                    "url": product['url'],
                    "img_url": product['image_url'],
                    "nutriscore": product['nutrition_grades'],
                }
                product_to_add.append(product_values)
            except KeyError:
                pass
            
        return product_to_add

    def insert_products_in_db(self, products, category):
        for product in products:
            try:
                if product['name']:
                    add = Product(
                        name = product['name'],
                        brand = product['brand'],
                        category = category,
                        url = product['url'],
                        img_url = product['img_url'],
                        nutriscore = product['nutriscore'],
                        )
                    add.save()

            except IntegrityError:
                continue

            except KeyError:
                pass
    
    def insert_category_in_db(self):
        for category in self.categories:
            add = Category(
                name = category
            )
            add.save()