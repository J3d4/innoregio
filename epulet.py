import csvhandler
import time
from tqdm import tqdm

read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/epulet.csv')
ins = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]

def calculations():
    print("Calculations with data in Epuletek:")
    for i in tqdm(range(len(ins))):
        time.sleep(0.0000000001) 

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

        ins[i].Qel = float(ins[i].nEel) * float(ins[i].Ter_est)
        ins[i].Qel_csil = float(ins[i].nEel_csil) * float(ins[i].Ter_est)
        ins[i].Qga = float(ins[i].nEga) * float(ins[i].Ter_est)
        ins[i].Qol = float(ins[i].nEol) * float(ins[i].Ter_est)
        ins[i].Qsz = float(ins[i].nEsz) * float(ins[i].Ter_est)
        ins[i].Qbm = float(ins[i].nEbm) * float(ins[i].Ter_est)
        ins[i].Qth = float(ins[i].nEth) * float(ins[i].Ter_est)

        ins[i].Qel_cs = float(ins[i].Eel_cs) * float(ins[i].Ter_est)
        ins[i].Qel_cs_cs = float(ins[i].Eel_cs_cs) * float(ins[i].Ter_est)
        ins[i].Qga_cs = float(ins[i].Ega_cs) * float(ins[i].Ter_est)
        ins[i].Qol_cs = float(ins[i].Eol_cs) * float(ins[i].Ter_est)
        ins[i].Qsz_cs = float(ins[i].Esz_cs) * float(ins[i].Ter_est)
        ins[i].Qbm_cs = float(ins[i].Ebm_cs) * float(ins[i].Ter_est)
        ins[i].Qth_cs = float(ins[i].Eth_cs) * float(ins[i].Ter_est)

        ins[i].Qel_real = float(ins[i].Qel) / float(ins[i].eel) * float(ins[i].k)
        ins[i].Qel_cs_real = float(ins[i].Qel_cs) / float(ins[i].eelcs) * float(ins[i].k)
        ins[i].Qga_real = float(ins[i].Qga) / float(ins[i].ega) * float(ins[i].k)
        ins[i].Qol_real = float(ins[i].Qol) / float(ins[i].eol) * float(ins[i].k)
        ins[i].Qsz_real = float(ins[i].Qsz) / float(ins[i].esz) * float(ins[i].k)
        ins[i].Qbm_real = float(ins[i].Qbm) / float(ins[i].ebm) * float(ins[i].k)
        ins[i].Qth_real = float(ins[i].Qth) / float(ins[i].eth) * float(ins[i].k)

        ins[i].Qel_real_cs = float(ins[i].Qel_cs) / float(ins[i].eel) * float(ins[i].k)
        ins[i].Qel_cs_real_cs = float(ins[i].Qel_cs_cs) / float(ins[i].eelcs) * float(ins[i].k)
        ins[i].Qga_real_cs = float(ins[i].Qga_cs) / float(ins[i].ega) * float(ins[i].k)
        ins[i].Qol_real_cs = float(ins[i].Qol_cs) / float(ins[i].eol) * float(ins[i].k)
        ins[i].Qsz_real_cs = float(ins[i].Qsz_cs) / float(ins[i].esz) * float(ins[i].k)
        ins[i].Qbm_real_cs = float(ins[i].Qbm_cs) / float(ins[i].ebm) * float(ins[i].k)
        ins[i].Qth_real_cs = float(ins[i].Qth_cs) / float(ins[i].eth) * float(ins[i].k)
        
        if ins[i].d_el == '' or ins[i].d_el == 0.0 or ins[i].d_el == 0:
            ins[i].d_el = ins[i].delest
        if ins[i].delcs == '' or ins[i].delcs == 0.0 or ins[i].delcs == 0:
            ins[i].delcs = ins[i].delcsest
        if ins[i].dga == '' or ins[i].dga == 0.0 or ins[i].dga == 0:
            ins[i].dga = ins[i].dgaest
        if ins[i].dol == '' or ins[i].dol == 0.0 or ins[i].dol == 0:
            ins[i].dol = ins[i].dolest
        if ins[i].dsz == '' or ins[i].dsz == 0.0 or ins[i].dsz == 0:
            ins[i].dsz = ins[i].dszest
        if ins[i].dbm == '' or ins[i].dbm == 0.0 or ins[i].dbm == 0:
            ins[i].dbm = ins[i].dbmest
        if ins[i].dth == '' or ins[i].dth == 0.0 or ins[i].dth == 0:
            ins[i].dth = ins[i].dthest
        
        if ins[i].Qel_real_cs == '':
            ins[i].Qel_real_cs = 0.0
        if ins[i].d_el == '':
            ins[i].d_el = 0.0
        if ins[i].Qel_cs_real_cs == '':
            ins[i].Qel_cs_real_cs = 0.0
        if ins[i].delcs == '':
            ins[i].delcs = 0.0
        if ins[i].Qga_real_cs == '':
            ins[i].Qga_real_cs = 0.0
        if ins[i].dga == '':
            ins[i].dga = 0.0
        if ins[i].Qol_real_cs == '':
            ins[i].Qol_real_cs = 0.0
        if ins[i].dol == '':
            ins[i].dol = 0.0
        if ins[i].Qsz_real_cs == '':
            ins[i].Qsz_real_cs = 0.0
        if ins[i].dsz == '':
            ins[i].dsz = 0.0
        if ins[i].Qbm_real_cs == '':
            ins[i].Qbm_real_cs = 0.0
        if ins[i].dbm == '':
            ins[i].dbm = 0.0
        if ins[i].Qth_real_cs == '':
            ins[i].Qth_real_cs = 0.0
        if ins[i].dth == '':
            ins[i].dth = 0.0

        ins[i].De_cs = (
            (float(ins[i].Qel_real_cs) * float(ins[i].d_el)) + 
            (float(ins[i].Qel_cs_real_cs) * float(ins[i].delcs)) +
            (float(ins[i].Qga_real_cs) * float(ins[i].dga)) +
            (float(ins[i].Qol_real_cs) * float(ins[i].dol)) +
            (float(ins[i].Qsz_real_cs) * float(ins[i].dsz)) +
            (float(ins[i].Qbm_real_cs) * float(ins[i].dbm)) +
            (float(ins[i].Qth_real_cs) * float(ins[i].dth)))
        
        ins[i].De = (
            (float(ins[i].Qel_real) * float(ins[i].d_el)) + 
            (float(ins[i].Qel_cs_real) * float(ins[i].delcs)) +
            (float(ins[i].Qga_real) * float(ins[i].dga)) +
            (float(ins[i].Qol_real) * float(ins[i].dol)) +
            (float(ins[i].Qsz_real) * float(ins[i].dsz)) +
            (float(ins[i].Qbm_real) * float(ins[i].dbm)) +
            (float(ins[i].Qth_real) * float(ins[i].dth)))
        
        if ins[i].fCO2_el == '':
            ins[i].fCO2_el = 0.0
        if ins[i].fCO2_el_cs == '':
            ins[i].fCO2_el_cs = 0.0
        if ins[i].fCO2_ga == '':
            ins[i].fCO2_ga = 0.0
        if ins[i].fCO2_ol == '':
            ins[i].fCO2_ol = 0.0
        if ins[i].fCO2_sz == '':
            ins[i].fCO2_sz = 0.0
        if ins[i].fCO2_bm == '':
            ins[i].fCO2_bm = 0.0
        if ins[i].fCO2_th == '':
            ins[i].fCO2_th = 0.0

        ins[i].TFCO2_e = (
            (float(ins[i].Qel_real) * float(ins[i].fCO2_el)) + 
            (float(ins[i].Qel_cs_real) * float(ins[i].fCO2_el_cs)) +
            (float(ins[i].Qga_real) * float(ins[i].fCO2_ga)) +
            (float(ins[i].Qol_real) * float(ins[i].fCO2_ol)) +
            (float(ins[i].Qsz_real) * float(ins[i].fCO2_sz)) +
            (float(ins[i].Qbm_real) * float(ins[i].fCO2_bm)) +
            (float(ins[i].Qth_real) * float(ins[i].fCO2_th)))
        
        ins[i].TFCO2_e_cs = (
            (float(ins[i].Qel_real_cs) * float(ins[i].fCO2_el)) + 
            (float(ins[i].Qel_cs_real_cs) * float(ins[i].fCO2_el_cs)) +
            (float(ins[i].Qga_real_cs) * float(ins[i].fCO2_ga)) +
            (float(ins[i].Qol_real_cs) * float(ins[i].fCO2_ol)) +
            (float(ins[i].Qsz_real_cs) * float(ins[i].fCO2_sz)) +
            (float(ins[i].Qbm_real_cs) * float(ins[i].fCO2_bm)) +
            (float(ins[i].Qth_real_cs) * float(ins[i].fCO2_th)))
        
        ins[i].deltaTFCO2_e = ins[i].TFCO2_e - ins[i].TFCO2_e_cs
    
    print("Epulet done.")
               
# for debugging purposes:
if __name__ == '__main__':
    calculations()
    print(" ")