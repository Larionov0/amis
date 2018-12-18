# Як змінювалась ціна на яблука? (графік)
import plotly
import plotly.graph_objs as go
list = []

from Dat import dataset
list = []
for client in dataset:
    for product in dataset[client]:
        if product == "apple":
            for i in range(len(dataset[client][product]["date"])):
                list.append((product,dataset[client][product]["date"][i],dataset[client][product]["price"][i]))

list1 = [tup[1] for tup in list]
list2 = [tup[2] for tup in list]

print(list1)
print(list2)

dicti =dict()

for i in range(len(list1)):
    dicti[list1[i]] = list2[i]
print(dicti)
list1 = [key for key in dicti]
list1.sort()
list2 = []
for date in list1:
    list2.append(dicti[date])
print("\n\n\n\n\n")
print(list1)
print(list2)
diagram = go.Bar(x = list1,y = list2)
plotly.offline.plot([diagram],filename = "diag.html")


