#Скільки грошей витрачає кожний покупець на покупки? (графік)
from Dat import dataset
import plotly
import plotly.graph_objs as go

dicty = {}
for client in dataset:
    count = 0
    for prod in dataset[client]:
        for i in dataset[client][prod]["price"]:
            count+=i
    dicty[client] = count
print(dicty)

diagram = go.Pie(labels=[i for i in dicty], values= [i for i in dicty.values()])
plotly.offline.plot([diagram],filename = "money.html")