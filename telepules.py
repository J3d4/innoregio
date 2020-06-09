import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/work/innoregio/vegleges/telepules.csv')
telepules = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inptomb = read.dataframe('/home/jeda/work/innoregio/vegleges/tomb_veg.csv')
tomb = [csvhandler.Dict(i, inptomb[0]) for i in inptomb[1:]]
out = '/home/jeda/work/innoregio/vegleges/telepules_veg.csv'
head = write.header(telepules)
##############################################################

def calculate(telepules, tomb):
    print("Calculations with data in Tomb and Telepules:")
    for i in tqdm(range(len(tomb))):
        for j in range(len(telepules)):
            # telepules folyamatabra kiegeszites szamolasai:
            QK_el_minus = telepules[j].QK_el_minus_est if telepules[j].QK_el_minus == '' else telepules[j].QK_el_minus
            if QK_el_minus == '':
                QK_el_minus = 0
            QK_el_cs_minus = telepules[j].QK_el_cs_minus_est if telepules[j].QK_el_cs_minus == '' else telepules[j].QK_el_cs_minus
            if QK_el_cs_minus == '':
                QK_el_cs_minus = 0
            QK_ga_minus = telepules[j].QK_ga_minus_est if telepules[j].QK_ga_minus == '' else telepules[j].QK_ga_minus
            if QK_ga_minus == '':
                QK_ga_minus = 0
            QK_ol_minus = telepules[j].QK_ol_minus_est if telepules[j].QK_ol_minus == '' else telepules[j].QK_ol_minus
            if QK_ol_minus == '':
                QK_ol_minus = 0
            QK_sz_minus = telepules[j].QK_sz_minus_est if telepules[j].QK_sz_minus == '' else telepules[j].QK_sz_minus
            if QK_sz_minus == '':
                QK_sz_minus = 0
            QK_bm_minus = telepules[j].QK_bm_minus_est if telepules[j].QK_bm_minus == '' else telepules[j].QK_bm_minus
            if QK_bm_minus == '':
                QK_bm_minus = 0
            QK_th_minus = telepules[j].QK_th_minus_est if telepules[j].QK_th_minus == '' else telepules[j].QK_th_minus
            if QK_th_minus == '':
                QK_th_minus = 0
            
            QK_el_plus = telepules[j].QK_el_plus_est if telepules[j].QK_el_plus == '' else telepules[j].QK_el_plus
            if QK_el_plus == '':
                QK_el_plus = 0
            QK_el_cs_plus = telepules[j].QK_el_cs_plus_est if telepules[j].QK_el_cs_plus == '' else telepules[j].QK_el_cs_plus
            if QK_el_cs_plus == '':
                QK_el_cs_plus = 0
            QK_ga_plus = telepules[j].QK_ga_plus_est if telepules[j].QK_ga_plus == '' else telepules[j].QK_ga_plus
            if QK_ga_plus == '':
                QK_ga_plus = 0
            QK_ol_plus = telepules[j].QK_ol_plus_est if telepules[j].QK_ol_plus == '' else telepules[j].QK_ol_plus
            if QK_ol_plus == '':
                QK_ol_plus = 0
            QK_sz_plus = telepules[j].QK_sz_plus_est if telepules[j].QK_sz_plus == '' else telepules[j].QK_sz_plus
            if QK_sz_plus == '':
                QK_sz_plus = 0
            QK_bm_plus = telepules[j].QK_bm_plus_est if telepules[j].QK_bm_plus == '' else telepules[j].QK_bm_plus
            if QK_bm_plus == '':
                QK_bm_plus = 0
            QK_th_plus = telepules[j].QK_th_plus_est if telepules[j].QK_th_plus == '' else telepules[j].QK_th_plus
            if QK_th_plus == '':
                QK_th_plus = 0
            
            telepules[j].QK_plus = (
                QK_el_plus +
                QK_el_cs_plus +
                QK_ga_plus +
                QK_ol_plus +
                QK_sz_plus +
                QK_bm_plus +
                QK_th_plus
            )
            telepules[j].QK_minus = (
                QK_el_minus +
                QK_el_cs_minus +
                QK_ga_minus +
                QK_ol_minus +
                QK_sz_minus +
                QK_bm_minus +
                QK_th_minus
            )
            if tomb[i].Telepules.strip() == telepules[j].Telepules.strip():
                # telepules folyamatabra kiegeszites szamolasai:
                if telepules[j].QK_el_real == '':
                    telepules[j].QK_el_real = 0
                telepules[j].QK_el_real = float(telepules[j].QK_el_real) + (float(tomb[i].QT_el_real) + QK_el_plus - QK_el_minus)
                if telepules[j].QK_el_cs_real == '':
                    telepules[j].QK_el_cs_real = 0
                telepules[j].QK_el_cs_real = float(telepules[j].QK_el_cs_real) + (float(tomb[i].QT_el_cs_real) + QK_el_cs_plus - QK_el_cs_minus)
                if telepules[j].QK_ga_real == '':
                    telepules[j].QK_ga_real = 0
                telepules[j].QK_ga_real = float(telepules[j].QK_ga_real) + (float(tomb[i].QT_ga_real) + QK_ga_plus - QK_ga_minus)
                if telepules[j].QK_ol_real == '':
                    telepules[j].QK_ol_real = 0
                telepules[j].QK_ol_real = float(telepules[j].QK_ol_real) + (float(tomb[i].QT_ol_real) + QK_ol_plus - QK_ol_minus)
                if telepules[j].QK_sz_real == '':
                    telepules[j].QK_sz_real = 0
                telepules[j].QK_sz_real = float(telepules[j].QK_sz_real) + (float(tomb[i].QT_sz_real) + QK_sz_plus - QK_sz_minus)
                if telepules[j].QK_bm_real == '':
                    telepules[j].QK_bm_real = 0
                telepules[j].QK_bm_real = float(telepules[j].QK_bm_real) + (float(tomb[i].QT_bm_real) + QK_bm_plus - QK_bm_minus)
                if telepules[j].QK_th_real == '':
                    telepules[j].QK_th_real = 0
                telepules[j].QK_th_real = float(telepules[j].QK_th_real) + (float(tomb[i].QT_th_real) + QK_th_plus - QK_th_minus)
                # alap telepules szamitasok:
                if telepules[j].QK_vil_cs == '':
                    telepules[j].QK_vil_cs = 0.0
                telepules[j].QK_vil_cs = float(telepules[j].QK_vil_cs) + float(tomb[i].QT_vil_cs)
                if telepules[j].QK_vil_real_cs == '':
                    telepules[j].QK_vil_real_cs = 0.0
                telepules[j].QK_vil_real_cs = float(telepules[j].QK_vil_real_cs) + float(tomb[i].QT_vil_real_cs)
                if telepules[j].QK_el_real_cs == '':
                    telepules[j].QK_el_real_cs = 0.0
                telepules[j].QK_el_real_cs = float(telepules[j].QK_el_real_cs) + float(tomb[i].QT_el_real_cs)
                if telepules[j].QK_el_cs_real_cs == '':
                    telepules[j].QK_el_cs_real_cs = 0.0
                telepules[j].QK_el_cs_real_cs = float(telepules[j].QK_el_cs_real_cs) + float(tomb[i].QT_el_cs_real_cs)
                if telepules[j].QK_ga_real_cs == '':
                    telepules[j].QK_ga_real_cs = 0.0
                telepules[j].QK_ga_real_cs = float(telepules[j].QK_ga_real_cs) + float(tomb[i].QT_ga_real_cs)
                if telepules[j].QK_ol_real_cs == '':
                    telepules[j].QK_ol_real_cs = 0.0
                telepules[j].QK_ol_real_cs = float(telepules[j].QK_ol_real_cs) + float(tomb[i].QT_ol_real_cs)
                if telepules[j].QK_sz_real_cs == '':
                    telepules[j].QK_sz_real_cs = 0.0
                telepules[j].QK_sz_real_cs = float(telepules[j].QK_sz_real_cs) + float(tomb[i].QT_sz_real_cs)
                if telepules[j].QK_bm_real_cs == '':
                    telepules[j].QK_bm_real_cs = 0.0
                telepules[j].QK_bm_real_cs = float(telepules[j].QK_bm_real_cs) + float(tomb[i].QT_bm_real_cs)
                if telepules[j].QK_th_real_cs == '':
                    telepules[j].QK_th_real_cs = 0.0
                telepules[j].QK_th_real_cs = float(telepules[j].QK_th_real_cs) + float(tomb[i].QT_th_real_cs)
                
                if telepules[j].QK_vil == '':
                    telepules[j].QK_vil = 0.0
                telepules[j].QK_vil = float(telepules[j].QK_vil) + float(tomb[i].QT_vil)
                if telepules[j].QK_vil_real == '':
                    telepules[j].QK_vil_real = 0.0
                telepules[j].QK_vil_real = float(telepules[j].QK_vil_real) + float(tomb[i].QT_vil_real)
                
                if telepules[j].deltaQK == '':
                    telepules[j].deltaQK = 0.0
                telepules[j].deltaQK = float(telepules[j].deltaQK) + float(tomb[i].deltaQT)
                if telepules[j].TFCO2_K == '':
                    telepules[j].TFCO2_K = 0.0
                telepules[j].TFCO2_K = float(telepules[j].TFCO2_K) + float(tomb[i].TFCO2_T)
                if telepules[j].TFCO2_K_cs == '':
                    telepules[j].TFCO2_K_cs = 0.0
                telepules[j].TFCO2_K_cs = float(telepules[j].TFCO2_K_cs) + float(tomb[i].TFCO2_T_cs)

                if telepules[j].TK_e == '':
                    telepules[j].TK_e = 0.0
                telepules[j].TK_e = float(telepules[j].TK_e) + float(tomb[i].TT_e)
                if telepules[j].TK_t == '':
                    telepules[j].TK_t = 0.0
                telepules[j].TK_t = float(telepules[j].TK_t) + float(tomb[i].TT_t)

    print("Calculations with data in Telepules:")
    for i in tqdm(range(len(telepules))):
        if telepules[i].TK_t == '':
            telepules[i].TK_t = 0.0
        if float(telepules[i].TK_t) != 0.0:
            telepules[i].EK_vil_t_cs = float(telepules[i].QK_vil_cs) / float(telepules[i].TK_t)
            telepules[i].EK_vil_real_t_cs = float(telepules[i].QK_vil_real_cs) / float(telepules[i].TK_t)
            telepules[i].EK_vil_t = float(telepules[i].QK_vil) / float(telepules[i].TK_t)
            telepules[i].EK_vil_real_t = float(telepules[i].QK_vil_real) / float(telepules[i].TK_t)
            telepules[i].deltaEK_t = float(telepules[i].deltaQK) / float(telepules[i].TK_t)
            if float(telepules[i].EK_vil_t) != 0.0:
                telepules[i].potK = 1 - float(telepules[i].EK_vil_t_cs) / float(telepules[i].EK_vil_t)

        if telepules[i].TK_e == '':
            telepules[i].TK_e = 0.0
        if float(telepules[i].TK_e) != 0.0:
            telepules[i].EK_vil_e_cs = float(telepules[i].QK_vil_cs) / float(telepules[i].TK_e)
            telepules[i].EK_vil_real_e_cs = float(telepules[i].QK_vil_real_cs) / float(telepules[i].TK_e)
            telepules[i].EK_vil_e = float(telepules[i].QK_vil) / float(telepules[i].TK_e)
            telepules[i].EK_vil_real_e = float(telepules[i].QK_vil_real) / float(telepules[i].TK_e)
            telepules[i].deltaEK_e = float(telepules[i].deltaQK) / float(telepules[i].TK_e)
            if float(telepules[i].EK_vil_e) != 0.0:
                telepules[i].potK = 1 - float(telepules[i].EK_vil_e_cs) / float(telepules[i].EK_vil_e)
        
        telepules[i].deltaQK_el_real = float(telepules[i].QK_el_real) - float(telepules[i].QK_el_real_cs)
        telepules[i].deltaQK_el_cs_real = float(telepules[i].QK_el_cs_real) - float(telepules[i].QK_el_cs_real_cs)
        telepules[i].deltaQK_ga_real = float(telepules[i].QK_ga_real) - float(telepules[i].QK_ga_real_cs)
        telepules[i].deltaQK_ol_real = float(telepules[i].QK_ol_real) - float(telepules[i].QK_ol_real_cs)
        telepules[i].deltaQK_sz_real = float(telepules[i].QK_sz_real) - float(telepules[i].QK_sz_real_cs)
        telepules[i].deltaQK_bm_real = float(telepules[i].QK_bm_real) - float(telepules[i].QK_bm_real_cs)
        telepules[i].deltaQK_th_real = float(telepules[i].QK_th_real) - float(telepules[i].QK_th_real_cs)
        telepules[i].deltaTFCO2_K = float(telepules[i].TFCO2_K) - float(telepules[i].TFCO2_K_cs)

    print("Telepules done.")
    return telepules

def writer(output, head, data):
    print("Writing Telepules-out")
    write.writer(output, head, data)
    print("Done.")  

# for debugging purposes:
if __name__ == '__main__':
    calculate(telepules, tomb)
    writer(out, head, telepules)
    print(" ")
