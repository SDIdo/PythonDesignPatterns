# from abc import ABC, abstractmethod

class Builder():
    pass

class Pizza(Builder):
    def __init__(self):
        self.__tomato = False
        self.__ketchop = False
        self.__cheese = False
        self.__onion = False
        self.__anchovi = False
        self.__size = 1
        self.__dough = 'thin'
        self.__added_items = set()
    
    @property
    def tomato(self):
        return self.__tomato
    
    def set_tomato(self, value: bool) -> Builder:
        self.__tomato = value
        if value:
            self.__added_items.add("tomato")
        else:
            self.__added_items.remove("tomato")
        return self

    @property
    def ketchop(self):
        return self.__ketchop
    
    
    def set_ketchop(self, value: bool):
        self.__ketchop = value
        if value:
            self.__added_items.add("ketchop")
        else:
            self.__added_items.remove("ketchop")
        return self

    @property
    def cheese(self):
        return self.__cheese
    
    
    def set_cheese(self, value: bool):
        self.__cheese = value
        if value:
            self.__added_items.add("cheese")
        else:
            self.__added_items.remove("cheese")
        return self

    def __repr__(self):
        return f"Pizza with {'nothing' if len([item for item in self.__added_items]) == 0 else [item for item in self.__added_items]}"


class PizzaOrder():
    def __init__(self):
        self.reset()

    def reset(self):
        self.__product = Pizza()

    def get_minimal_order(self):
        self.reset()
        self.__product.set_cheese(True).set_tomato(True)
        return self.__product

    def get_extra_order(self):
        self.reset()
        self.__product.set_cheese(True).set_tomato(True).set_ketchop(True)
        return self.__product

    
# driver
builder = PizzaOrder()
extra_pizza = builder.get_extra_order()
print(extra_pizza)
minimal_pizza = builder.get_minimal_order()
print(minimal_pizza)
