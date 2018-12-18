dataset = dict()
with open("data/order.txt") as file:
    text = file.read()
    lines = text.splitlines()
    for line in lines[1:]:
        line = line.split(",")
        client = line[0]
        date = line[1]
        product = line[2]
        quantity = line[3]
        price =  line[4]
        if client in dataset:
            if product in dataset[client]:
                dataset[client][product]["date"].append(date)
                dataset[client][product]["price"].append(float(price))
            else:
                dataset[client][product] = {
                                "date" : [date],
                                "quantity" : quantity,
                                "price" : [float(price)]
                            }
        else:
            dataset[client] = {
                        product : {
                                "date" : [date],
                                "quantity" : quantity,
                                "price" : [float(price)]
                            }
                }
print(dataset)