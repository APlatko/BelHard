class Soda:


    def __init__(self, additive):
        if isinstance(additive, str):
            self.additive = additive
        else:
            self.additive = None

    def show_my_drink(self):
        if self.additive:
            print(f"Soda with {self.additive}")
        else:
            print(f"Regular soda")


soda_strawberry = Soda("strawberry")
soda_strawberry.show_my_drink()


class Counter:

    def __init__(self, start, stop, value=0):
        self.value = value
        self.start = start
        self.stop = stop

    def increase(self, num=1):
        self.value += num
        return self.value

    def decrease(self, num=1):
        self.value -= num
        return self.value

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.stop):
            if i >= self.stop:
                raise StopIteration()
            self.value += 1
            return self.value

count_1 = Counter(1, 5, 20)
print(next(count_1))
print(next(count_1))
print(next(count_1))
print(count_1.decrease(5))
print(count_1.increase())




class Phone:

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, caller_name):
        print(f"{caller_name} is calling.")

    def get_info(self):
        parameters = (self.brand, self.model, self.issue_year)
        return parameters

    def __str__(self):
        print(f"Brand:{self.brand} Model:{self.model} Issue year:{self.issue_year}")


phone_1 = Phone("Nokia", 3310, 2001)
phone_1.receive_call("Anna")
print(phone_1.get_info())
phone_1.__str__()



