#Ввід даних

from Dat import dataset
from validators.validator import name_validator

from validators.validator import product_validator

from validators.validator import date_validator

from validators.validator import num_validator

def adder(client,product,date,quantity,price):
    if client in dataset:
        if product in dataset[client]:
            if date in dataset[client][product]["date"] and dataset[client][product]["price"][dataset[client][product]["date"].index(date)]==price:
                print("There is it")
            else:
                dataset[client][product]["date"].append(date)
                dataset[client][product]["price"].append(float(price))
        else:
            dataset[client][product] = {
                "date": [date],
                "quantity": quantity,
                "price": [float(price)]
                                        }
    else:
        dataset[client] = {
            product: {
                "date": [date],
                "quantity": quantity,
                "price": [float(price)]
                    }
                        }

def get_val():
    name = name_validator()
    while not name:
        print("Incorrect")
        name = name_validator()

    prod = product_validator()
    while not prod:
        print("Incorrect product")
        prod = product_validator()

    date = date_validator()
    while not date:
        print("Incorrect date")
        date = date_validator()

    quantity = num_validator("quantity")
    while not quantity:
        print("Incorrect quantity")
        quantity = num_validator("Quantity:")

    price = num_validator("Price:")
    while not price:
        print("Incorrect price")
        price = num_validator("Price:")

    print(dataset)
    adder(name,prod,date,quantity,price)


adder("Mike","kovbasa","10.20.4000","1",200)
print(dataset)
adder("Mike","kovbasa","10.20.4000","1",300)
print(dataset)
get_val()