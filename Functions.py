import Inventary as iv
#returns statistics of provinces
def returnProvinceData(p):
    for province in iv.IndiceDiario.keys():
        if p.upper() in province:
            data = iv.IndiceDiario[province] 
            return " En la provincia de {} se contabilizan {} casos lo que representa un porcentaje de {} con respecto al total de contagiados en el Ecuador".format(province,data[0],data[1])

#filter received text
def filterText(p, eliminate):
    p = p.replace(eliminate,"")
    return p
