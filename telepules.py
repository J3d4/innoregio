import csv
class Telepules:
    def __init__(self, row, header, the_id):
        self.__dict__ = dict(zip(header, row)) 
        self.the_id = the_id
    def __repr__(self):
        return self.the_id
    dataframe = list(csv.reader(open('telepules.csv', encoding='utf-8'), delimiter=','))

ins = [Telepules(a, Telepules.dataframe[0], "telepules_{}".format(i+1)) for i, a in enumerate(Telepules.dataframe[1:])]

for i in range(len(ins)):
    print(ins[i].id, ins[i].Telepules, ins[i].QK_vil_cs)