import csv

class Epulet:
    def __init__(self, row, header):
       self.__dict__ = dict(zip(header, row)) 

    data = list(csv.reader(open('/home/jeda/Work/bastyainno/epulet.csv', 'r', encoding='utf-8'), delimiter=','))
    writer = csv.writer(open('/home/jeda/Work/bastyainno/output-epulet.csv', 'w', encoding='utf-8'), delimiter=',')

ins = [Epulet(i, Epulet.data[0]) for i in Epulet.data[1:]]

#region Calculations

for i in range(len(ins)):
    ins[i].Ee = float(ins[i].E0) * float(ins[i].a)
    if ins[i].Sz == '':
        ins[i].Sz = 0.0
    ins[i].Tbr = float(ins[i].Sz) * float(ins[i].te)
    ins[i].Ter_est = float(ins[i].Tbr) * float(ins[i].Tn_Tbr)
    ins[i].deltaEe = float(ins[i].Ee) - float(ins[i].Ee_cs)
    if ins[i].Ter == '' or ins[i].Ter == 0.0:
        ins[i].deltaQe = float(ins[i].deltaEe) * float(ins[i].Ter_est)    
        ins[i].Ter = ins[i].Ter_est
    else:
        ins[i].deltaQe = float(ins[i].deltaEe) * float(ins[i].Ter)
    if ins[i].Epulet_funkcio == 'Lakoepulet':
        ins[i].Ee_vil_cs = float(ins[i].Ee_cs)
        ins[i].Ee_vil = float(ins[i].Ee)
    else:
        ins[i].Ee_vil_cs = float(ins[i].Ee_cs) - float(ins[i].Evil_cs)
        ins[i].Ee_vil = float(ins[i].Ee) - float(ins[i].Evil)
    ins[i].Ee_vil_real_cs = float(ins[i].Ee_vil_cs) * float(ins[i].k)
    
    if ins[i].Ael_cs == '':
        ins[i].Ael_cs = 0.0
    if ins[i].Etech == '':
        ins[i].Etech = 0.0
    ins[i].Eel_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Ael_cs) + (float(ins[i].Evil_cs) + float(ins[i].Etech))
    if ins[i].Aelcs_cs == '':
        ins[i].Aelcs_cs = 0.0
    ins[i].Eel_cs_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Aelcs_cs)
    ins[i].Ega_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Aga_est_cs)
    ins[i].Eol_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Aol_est_cs)
    ins[i].Esz_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Asz_est_cs)
    ins[i].Ebm_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Abm_est_cs)
    ins[i].Eth_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Ath_est_cs)
    
    if ins[i].Ael == '':
        ins[i].Ael = 0.0
    ins[i].nEel = float(ins[i].Ee_vil) * float(ins[i].Ael) + (float(ins[i].Evil) + float(ins[i].Etech))
    if ins[i].Aelcs == '':
        ins[i].Aelcs = 0.0
    ins[i].nEel_csil = float(ins[i].Ee_vil) * float(ins[i].Aelcs)
    if ins[i].Aga == '':
        ins[i].Aga = 0.0
    ins[i].nEga = float(ins[i].Ee_vil) * float(ins[i].Aga)
    if ins[i].Aol == '':
        ins[i].Aol = 0.0
    ins[i].nEol = float(ins[i].Ee_vil) * float(ins[i].Aol)
    if ins[i].Asz == '':
        ins[i].Asz = 0.0
    ins[i].nEsz = float(ins[i].Ee_vil) * float(ins[i].Asz)
    if ins[i].Abm == '':
        ins[i].Abm = 0.0
    ins[i].nEbm = float(ins[i].Ee_vil) * float(ins[i].Abm)
    if ins[i].Ath == '':
        ins[i].Ath = 0.0
    ins[i].nEth = float(ins[i].Ee_vil) * float(ins[i].Ath)
    
    if ins[i].Ee_vil != 0.0:
        ins[i].pote = 1.0 - (float(ins[i].Ee_vil_cs) / float(ins[i].Ee_vil))
    else:
        ins[i].pote = 0.0
    
    ins[i].Ee_vil_real = float(ins[i].Ee_vil) * float(ins[i].k)
    ins[i].Qe_vil = float(ins[i].Ee_vil) * float(ins[i].Ter_est)
    ins[i].Qe_vil_real = float(ins[i].Qe_vil) * float(ins[i].k)
    ins[i].Qe_vil_cs = float(ins[i].Ee_vil_cs) * float(ins[i].Ter_est)
    ins[i].Qe_vil_real_cs = float(ins[i].Qe_vil_cs) * float(ins[i].k)

#endregion

Epulet.writer.writerows(map(lambda x: [x], ins))