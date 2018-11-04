from pymongo import MongoClient
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
customers = db["customers"]
customers_list = customers.find()

acc_event = 0
acc_ads = 0
acc_wom = 0

for i in customers_list:
    if i["ref"] == "events":
        acc_event +=1
    elif i["ref"] == "ads":
        acc_ads +=1
    elif i["ref"] ==  "wom":
        acc_wom +=1
     
print("noi khac mua hang tai event: ",acc_event)
print("noi khac mua hang tai ads: ",acc_ads)
print("noi khac mua hang tai wom: ",acc_wom)
       
machine_count = [acc_event,acc_ads,acc_wom]
machine_names = ["events", "ads", "wom"]

pyplot.pie(machine_count, labels= machine_names, autopct = "%.1f%%", shadow=True, explode=[0,0.1,0.1])
pyplot.title("REF")
pyplot.axis("equal")
pyplot.show()