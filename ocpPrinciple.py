class Product:
    def __init__(self, price):
        '''Initializing the price attribute'''
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, price, discount):
        '''super() inherits init method of parent class product'''
        super().__init__(price)
        self.discount = discount

def calculate_total_price(products):
    ''''Calculate the discounted price, iterating through product class,
    checking if it's an instance of DiscountedProduct using isinstance()'''
    total_price = 0
    for product in products:
        if isinstance(product, DiscountedProduct):
            total_price += (product.price - product.discount)
        else:
            total_price += product.price
    return total_price

products = [Product(100), DiscountedProduct(50, 10), Product(75)]
print("Total Price:", calculate_total_price(products))
