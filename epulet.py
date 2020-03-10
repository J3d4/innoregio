import csv

class Epulet:
    def __init__(self, row, header, the_id):
       self.__dict__ = dict(zip(header, row)) 
       self.the_id = the_id
    def __repr__(self):
       return self.the_id

    dataframe = list(csv.reader(open('epulet.csv', encoding='utf-8'), delimiter=','))

ins = [Epulet(a, Epulet.dataframe[0], "epulet_{}".format(i+1)) for i, a in enumerate(Epulet.dataframe[1:])]

#region Calculations

for i in range(len(ins)):
    ins[i].Ee = float(ins[i].E0) * float(ins[i].a)
    if ins[i].Sz == '':
        ins[i].Sz = 0.0
    ins[i].Tbr = float(ins[i].Sz) * float(ins[i].te)
    ins[i].Ter_est = float(ins[i].Tbr) * float(ins[i].Tn_Tbr)
    ins[i].deltaEe = float(ins[i].Ee) - float(ins[i].Ee_cs)
    #ins[i].Ee = float(ins[i].E0) * float(ins[i].a)

#endregion