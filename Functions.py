#import firebase sdk administrator
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

import Inventary as iv
#returns statistics of provinces
def returnProvinceData(p):
    for idx in range(len(iv.IndiceDiario)):
        if p.upper() in iv.IndiceDiario[idx]:
            

            return " En la provincia de {} se contabilizan {} casos lo que representa un porcentaje de {} con respecto al total de contagiados en el Ecuador".format(province,data[0],data[1])

#filter received text
def filterText(p, eliminate):
    p = p.replace(eliminate,"")
    return p


ref = db.reference('dinosaurs')
snapshot = ref.order_by_child('height').get()
for key, val in snapshot.items():
    print('{0} was {1} meters tall'.format(key, val))