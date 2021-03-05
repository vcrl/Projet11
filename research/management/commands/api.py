from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError
import requests
from ...models import Product, Category, Substitute

class Command(BaseCommand):
    help = "Script d'ajout des produits en base de donnée."

    def __init__(self):
        self.api_url = "https://fr.openfoodfacts.org/cgi/search.pl?action=process"
    
    def handle(self, *args, **kwargs):

        CATEGORIES = [
            "Boissons",
            "Snacks",
            "Epicerie",
            "Conserves",
            "Desserts"
        ]

        NUTRISCORE = [
            'a',
            'b',
            'c'
        ]

        PRODUCTS_NB = 150

        for nutriscore in NUTRISCORE:
            for page in range(1, 3):
                for category in CATEGORIES:
                    products = self.get_products(category, nutriscore, page)
                    self.insert_products_in_db(products)
            
        print("ok")
        
    def insert_products_in_db(self, products):
        for product in products:
            try:
                if product['name']:
                    print("name ok")
                    add = Product.objects.create( # ICI ça marche pas todo: ca marche pas
                        name = product['name'],
                        brands = product['brand'],
                        category = product['category'],
                        url = product['url'], img_url = product['img_url'],
                        nutriscore = product['nutriscore'],
                        )
                    print(add)
                    add.save()
                    print('added')
                    
            except IntegrityError:
                continue

            except KeyError:
                pass

            except:
                pass
    
    def insert_category_in_db(self, category):
        add = Category.objects.update_or_create(
            name = category
        )
        add.save()

    def get_products(self, category, nutriscore, products_nb):

        payload = {
                'action': 'process',
                'tagtype_0': 'categories',
                'tag_contains_0': 'contains',
                'tag_0': category,
                'tagtype_1': 'nutrition_grade',
                'tag_contains_1': 'contains',
                'page_size': products_nb,
                'json': '1',
                }

        response = requests.get(self.api_url, params=payload)
        response_as_json = response.json()
        product_to_add = []
        for product in response_as_json['products']:
            
            try:
                values = {
                    "name": product['product_name'],
                    "brand": product['brands'],
                    "category": category,
                    "url": product['url'],
                    "img_url": product['image_url'],
                    "nutriscore": product['nutrition_grades'],
                }
                product_to_add.append(values)
                #print(product_to_add)
            except KeyError:
                pass

            except requests.exceptions.ConnectionError:
                print("Lancement impossible : vérifiez votre connexion internet.")
                break
            
        return product_to_add