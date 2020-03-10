import csv
class Telek:
    def __init__(self, row, header, the_id):
       self.__dict__ = dict(zip(header, row)) 
       self.the_id = the_id
    def __repr__(self):
       return self.the_id

    dataframe = list(csv.reader(open('telek.csv', encoding='utf-8'), delimiter=','))

ins = [Telek(a, Telek.dataframe[0], "epulet_{}".format(i+1)) for i, a in enumerate(Telek.dataframe[1:])]

for i in range(len(ins)):
    print(ins[i].Helyrajziszam, ins[i].Telepules, ins[i].Tombazonosito)