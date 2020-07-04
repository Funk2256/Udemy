class Beverage():
    prices = {"Strawberries": 1.5, "Banana": 0.5, "Mango": 2.5,
              "Blueberries": 1, "Raspberries": 1, "Apple": 1.75,
              "Pineapple": 3.5}

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def get_cost(self):
        cl_lst = []
        for x in self.ingredients:
            values_prices = (self.prices.get(x))
            cl_lst.append(values_prices)
        cost = (sum(cl_lst))
        self.cost = cost
        return(f'${(cost):.2f}')

    def get_price(self):
        return(f'${self.cost * 2.5:.2f}')

    def get_name(self):
        sort_list = sorted([i.replace('ies', 'y') for i in self.ingredients])

        if len(sort_list) > 1:
            sort_list.append("Fusion")
        else:
            sort_list.append("Smoothie")
        return ' '.join(sort_list)

s1 = Beverage(['Banana'])

print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())



"""class Beverage():
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.cost = sum([prices[fruit] for fruit in self.ingredients])
        self.prices = self.cost * 2.5

    def get_cost(self):
        return f'${self.cost:.2f}'

    def get_prices(self):
        return f'${self.prices:.2f}'

    def get_name(self):
        lst = sorted([i.replace('ies', 'y') for i in self.ingredients])
        return f"{' '.join(lst)}{'Fusion' if len(lst) > 1 else 'Smoothie'}"   """