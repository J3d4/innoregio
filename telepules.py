import csvhandler
import operator as op
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/work/innoregio/input/telepules-test.csv')
telepules = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inptomb = read.dataframe('/home/jeda/work/innoregio/output/tomb-test-out.csv')
tomb = [csvhandler.Dict(i, inptomb[0]) for i in inptomb[1:]]
out = '/home/jeda/work/innoregio/output/telepules-test-out.csv'
head = write.header(telepules)
##############################################################

def calculate(telepules, tomb):
    print("Calculations with data in Tomb and Telepules:")
    for i in tqdm(range(len(tomb))):
        for j in range(len(telepules)):
            if tomb[i].Telepules.strip() == telepules[j].Telepules.strip():
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
                if telepules[j].QK_el_real == '':
                    telepules[j].QK_el_real = 0.0
                telepules[j].QK_el_real = float(telepules[j].QK_el_real) + float(tomb[i].QT_el_real)
                if telepules[j].QK_el_cs_real == '':
                    telepules[j].QK_el_cs_real = 0.0
                telepules[j].QK_el_cs_real = float(telepules[j].QK_el_cs_real) + float(tomb[i].QT_el_cs_real)
                if telepules[j].QK_ga_real == '':
                    telepules[j].QK_ga_real = 0.0
                telepules[j].QK_ga_real = float(telepules[j].QK_ga_real) + float(tomb[i].QT_ga_real)
                if telepules[j].QK_ol_real == '':
                    telepules[j].QK_ol_real = 0.0
                telepules[j].QK_ol_real = float(telepules[j].QK_ol_real) + float(tomb[i].QT_ol_real)
                if telepules[j].QK_sz_real == '':
                    telepules[j].QK_sz_real = 0.0
                telepules[j].QK_sz_real = float(telepules[j].QK_sz_real) + float(tomb[i].QT_sz_real)
                if telepules[j].QK_bm_real == '':
                    telepules[j].QK_bm_real = 0.0
                telepules[j].QK_bm_real = float(telepules[j].QK_bm_real) + float(tomb[i].QT_bm_real)
                if telepules[j].QK_th_real == '':
                    telepules[j].QK_th_real = 0.0
                telepules[j].QK_th_real = float(telepules[j].QK_th_real) + float(tomb[i].QT_th_real)

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
        if float(telepules[i].TK_t) != 0.0:
            telepules[i].EK_vil_t_cs = float(telepules[i].QK_vil_cs) / float(telepules[i].TK_t)
            telepules[i].EK_vil_real_t_cs = float(telepules[i].QK_vil_real_cs) / float(telepules[i].TK_t)
            telepules[i].EK_vil_t = float(telepules[i].QK_vil) / float(telepules[i].TK_t)
            telepules[i].EK_vil_real_t = float(telepules[i].QK_vil_real) / float(telepules[i].TK_t)
            telepules[i].deltaEK_t = float(telepules[i].deltaQK) / float(telepules[i].TK_t)
            if float(telepules[i].EK_vil_t) != 0.0:
                telepules[i].potK = 1 - float(telepules[i].EK_vil_t_cs) / float(telepules[i].EK_vil_t)

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
