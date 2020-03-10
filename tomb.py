import csv
class Tomb:
    def __init__(self, row, header, the_id):
       self.__dict__ = dict(zip(header, row)) 
       self.the_id = the_id
    def __repr__(self):
       return self.the_id

    dataframe = list(csv.reader(open('tomb.csv', encoding='utf-8'), delimiter=','))

ins = [Tomb(a, Tomb.dataframe[0], "epulet_{}".format(i+1)) for i, a in enumerate(Tomb.dataframe[1:])]

for i in range(len(ins)):
    print(ins[i].Telepules, ins[i].Tombazonosito, ins[i].QT_vil_cs, ins[i].QT_vil_real_cs)