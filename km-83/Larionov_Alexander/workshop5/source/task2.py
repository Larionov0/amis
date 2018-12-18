print("task1")


from Dat import dataset
list = []
for client in dataset:
    for product in dataset[client]:
        for i in range(len(dataset[client][product]["date"])):
            list.append((product,dataset[client][product]["date"][i],dataset[client][product]["price"][i]))


print(list)
