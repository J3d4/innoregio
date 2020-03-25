import csvhandler
import time
from tqdm import tqdm

read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/telek.csv')
ins = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inpep = read.dataframe('/home/jeda/Work/innoregio/output/epulet-out.csv')
insep = [csvhandler.Dict(i, inpep[0]) for i in inpep[1:]]

def calculations():
    print("Calculate Telek with Epulet:")
    for i in tqdm(range(len(insep))):
        time.sleep(0.0000000001)
        for j in range(len(ins)):
            if insep[i].Helyrajziszam == ins[j].Helyrajziszam:
                ins[j].Qt_vil_cs = float(ins[j].Qt_vil_cs) + float(insep[i].Qe_vil_cs)
                ins[j].Qt_vil_real_cs = float(ins[j].Qt_vil_real_cs) + float(insep[i].Qe_vil_real_cs)
                if ins[j].Qt_el_real_cs == '':
                    ins[j].Qt_el_real_cs = 0.0
                ins[j].Qt_el_real_cs = float(ins[j].Qt_el_real_cs) + float(insep[i].Qel_real_cs)
                if ins[j].Qt_el_cs_real_cs == '':
                    ins[j].Qt_el_cs_real_cs = 0.0
                ins[j].Qt_el_cs_real_cs = float(ins[j].Qt_el_cs_real_cs) + float(insep[i].Qel_cs_real_cs)
                if ins[j].Qt_ga_real_cs == '':
                    ins[j].Qt_ga_real_cs = 0.0
                ins[j].Qt_ga_real_cs = float(ins[j].Qt_ga_real_cs) + float(insep[i].Qga_real_cs)
                if ins[j].Qt_ol_real_cs == '':
                    ins[j].Qt_ol_real_cs = 0.0
                ins[j].Qt_ol_real_cs = float(ins[j].Qt_ol_real_cs) + float(insep[i].Qol_real_cs)
                if ins[j].Qt_sz_real_cs == '':
                    ins[j].Qt_sz_real_cs = 0.0
                ins[j].Qt_sz_real_cs = float(ins[j].Qt_sz_real_cs) + float(insep[i].Qsz_real_cs)
                if ins[j].Qt_bm_real_cs == '':
                    ins[j].Qt_bm_real_cs = 0.0
                ins[j].Qt_bm_real_cs = float(ins[j].Qt_bm_real_cs) + float(insep[i].Qbm_real_cs)
                if ins[j].Qt_th_real_cs == '':
                    ins[j].Qt_th_real_cs = 0.0
                ins[j].Qt_th_real_cs = float(ins[j].Qt_th_real_cs) + float(insep[i].Qth_real_cs)
                ins[j].Dt_cs = float(ins[j].Dt_cs) + float(insep[i].De_cs)
                ins[j].Qt_vil = float(ins[j].Qt_vil) + float(insep[i].Qe_vil)
                ins[j].Qt_vil_real = float(ins[j].Qt_vil_real) + float(insep[i].Qe_vil_real)
                if ins[j].Qt_el_real == '':
                    ins[j].Qt_el_real = 0.0
                ins[j].Qt_el_real = float(ins[j].Qt_el_real) + float(insep[i].Qel_real)
                if ins[j].Qt_el_cs_real == '':
                    ins[j].Qt_el_cs_real = 0.0
                ins[j].Qt_el_cs_real = float(ins[j].Qt_el_cs_real) + float(insep[i].Qel_cs_real)
                if ins[j].Qt_ga_real == '':
                    ins[j].Qt_ga_real = 0.0
                ins[j].Qt_ga_real = float(ins[j].Qt_ga_real) + float(insep[i].Qga_real)
                if ins[j].Qt_ol_real == '':
                    ins[j].Qt_ol_real = 0.0
                ins[j].Qt_ol_real = float(ins[j].Qt_ol_real) + float(insep[i].Qol_real)
                if ins[j].Qt_sz_real == '':
                    ins[j].Qt_sz_real = 0.0
                ins[j].Qt_sz_real = float(ins[j].Qt_sz_real) + float(insep[i].Qsz_real)
                if ins[j].Qt_bm_real == '':
                    ins[j].Qt_bm_real = 0.0
                ins[j].Qt_bm_real = float(ins[j].Qt_bm_real) + float(insep[i].Qbm_real)
                if ins[j].Qt_th_real == '':
                    ins[j].Qt_th_real = 0.0
                ins[j].Qt_th_real = float(ins[j].Qt_th_real) + float(insep[i].Qth_real)
                ins[j].Dt = float(ins[j].Dt) + float(insep[i].De)
                ins[j].deltaQt = float(ins[j].deltaQt) + float(insep[i].deltaQe)
                if ins[j].TFCO2_t_cs == '':
                    ins[j].TFCO2_t_cs = 0.0
                ins[j].TFCO2_t_cs = float(ins[j].TFCO2_t_cs) + float(insep[i].TFCO2_e_cs)
                if ins[j].TFCO2_t == '':
                    ins[j].TFCO2_t = 0.0
                ins[j].TFCO2_t = float(ins[j].TFCO2_t) + float(insep[i].TFCO2_e)
                if ins[j].Tt_e == '':
                    ins[j].Tt_e = 0.0
                ins[j].Tt_e = float(ins[j].Tt_e) + float(insep[i].Ter_est)

                if insep[i].Tipusszam == 'p':
                    ins[j].adat_t = 1
                ins[j].adat_t = 0
    
    print("Calculations with data in Telek:")
    for i in tqdm(range(len(ins))):
        time.sleep(0.0000000001)

        ins[i].Et_vil_e_cs = float(ins[i].Qt_vil_cs) / float(ins[i].Tt_e)
        ins[i].Et_vil_t_cs = float(ins[i].Qt_vil_cs) / float(ins[i].Tt_t)
        ins[i].Et_vil_real_e_cs = float(ins[i].Qt_vil_real_cs) / float(ins[i].Tt_e)
        ins[i].Et_vil_real_t_cs = float(ins[i].Qt_vil_real_cs) / float(ins[i].Tt_t)
        ins[i].Et_vil_e = float(ins[i].Qt_vil) / float(ins[i].Tt_e)
        ins[i].Et_vil_t = float(ins[i].Qt_vil) / float(ins[i].Tt_t)
        ins[i].Et_vil_real_e = float(ins[i].Qt_vil_real) / float(ins[i].Tt_e)
        ins[i].Et_vil_real_t = float(ins[i].Qt_vil_real) / float(ins[i].Tt_t)
        ins[i].deltaEt_e = float(ins[i].deltaQt) / float(ins[i].Tt_e)
        ins[i].deltaEt_t = float(ins[i].deltaQt) / float(ins[i].Tt_t)
        ins[i].deltaTFCO2_t = float(ins[i].TFCO2_t) - float(ins[i].TFCO2_t_cs)
        ins[i].pott = 1 - (float(ins[i].Et_vil_cs) / float(ins[i].Et_vil))

    print("Telek done.")

# for debugging purposes:
if __name__ == '__main__':
    calculations()
    print(" ")