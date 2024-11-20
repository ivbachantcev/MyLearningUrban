class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
    

class Shop:
    __file_name ='products.txt'
    def get_products(self):
        list_product = ''
        f = open(self.__file_name, 'r')
        for s in f.readlines():
            list_product += s
        f.close()
        return list_product
    
    def add(self, *products: Product):
        f = open(self.__file_name, 'r')
        cur_products = []
        for x in f.readlines():
            # x.split(', ')[0] - вытаскиваем название, т.к. просили сравнивать только названия
            cur_products.append(x.split(', ')[0])
        f.close()
        f = open(self.__file_name, 'a')
        for p in products:
            # str(p).split(', ')[0] - вытаскиваем название, т.к. просили сравнивать только названия
            if str(p).split(', ')[0] not in cur_products:
                f.write(str(p) + '\n')
            else:
                print(f'Продукт {str(p)} уже есть в магазине')
        f.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())