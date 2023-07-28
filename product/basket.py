from .models import Product
from .serializers import ProductListSerializer

class Basket():

    def __init__(self, request):
        self.session = request.session
        self.request = request
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket


    def save(self):
        self.session.modified = True

        
    def add(self, product):
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {}
        

        self.save()
    
    def update(self,productid,productqty):
        self.basket[str(productid)]['productqty'] = productqty
        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects .filter(id__in=product_ids)
        basket = self.basket.copy()


        for product in products:
            product_data = ProductListSerializer(product, context={"request":self.request}).data
            product_data["quantity"] = 1
            basket[str(product.id)] = product_data
            


        for item in basket.values():
            yield item
            
    # def __len__(self):
    #     return sum(item['productqty'] for item in self.basket.values())

    # def sub_total(self):
    #     return sum([item['total_price'] for item in self.basket.values()])
    
    def delete(self,productid):
        id = str(productid)
        if id in self.basket:
            del self.basket[id]
        self.save()
