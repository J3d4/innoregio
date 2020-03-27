import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/epulet.csv')
epulet = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
out = '/home/jeda/Work/innoregio/output/epulet-out.csv'
head = write.header(epulet)
##############################################################

def calculate(epulet):
    print("Calculations with epulet in Epuletek:")
    for i in tqdm(range(len(epulet))):
        epulet[i].Ee = float(epulet[i].E0) * float(epulet[i].a)
        if epulet[i].Sz == '':
            epulet[i].Sz = 0.0
        epulet[i].Tbr = float(epulet[i].Sz) * float(epulet[i].te)
        epulet[i].Ter_est = float(epulet[i].Tbr) * float(epulet[i].Tn_Tbr)
        epulet[i].deltaEe = float(epulet[i].Ee) - float(epulet[i].Ee_cs)
        if epulet[i].Ter == '' or epulet[i].Ter == 0.0:
            epulet[i].deltaQe = float(epulet[i].deltaEe) * float(epulet[i].Ter_est)    
            epulet[i].Ter = epulet[i].Ter_est
        else:
            epulet[i].deltaQe = float(epulet[i].deltaEe) * float(epulet[i].Ter)
        if epulet[i].Epulet_funkcio == 'Lakoepulet':
            epulet[i].Ee_vil_cs = float(epulet[i].Ee_cs)
            epulet[i].Ee_vil = float(epulet[i].Ee)
        else:
            epulet[i].Ee_vil_cs = float(epulet[i].Ee_cs) - float(epulet[i].Evil_cs)
            epulet[i].Ee_vil = float(epulet[i].Ee) - float(epulet[i].Evil)
        epulet[i].Ee_vil_real_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].k)

        if epulet[i].Ael_cs == '':
            epulet[i].Ael_cs = 0.0
        if epulet[i].Etech == '':
            epulet[i].Etech = 0.0
        epulet[i].Eel_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Ael_cs) + (float(epulet[i].Evil_cs) + float(epulet[i].Etech))
        if epulet[i].Aelcs_cs == '':
            epulet[i].Aelcs_cs = 0.0
        epulet[i].Eel_cs_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Aelcs_cs)
        epulet[i].Ega_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Aga_est_cs)
        epulet[i].Eol_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Aol_est_cs)
        epulet[i].Esz_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Asz_est_cs)
        epulet[i].Ebm_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Abm_est_cs)
        epulet[i].Eth_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Ath_est_cs)

        if epulet[i].Ael == '':
            epulet[i].Ael = 0.0
        epulet[i].nEel = float(epulet[i].Ee_vil) * float(epulet[i].Ael) + (float(epulet[i].Evil) + float(epulet[i].Etech))
        if epulet[i].Aelcs == '':
            epulet[i].Aelcs = 0.0
        epulet[i].nEel_csil = float(epulet[i].Ee_vil) * float(epulet[i].Aelcs)
        if epulet[i].Aga == '':
            epulet[i].Aga = 0.0
        epulet[i].nEga = float(epulet[i].Ee_vil) * float(epulet[i].Aga)
        if epulet[i].Aol == '':
            epulet[i].Aol = 0.0
        epulet[i].nEol = float(epulet[i].Ee_vil) * float(epulet[i].Aol)
        if epulet[i].Asz == '':
            epulet[i].Asz = 0.0
        epulet[i].nEsz = float(epulet[i].Ee_vil) * float(epulet[i].Asz)
        if epulet[i].Abm == '':
            epulet[i].Abm = 0.0
        epulet[i].nEbm = float(epulet[i].Ee_vil) * float(epulet[i].Abm)
        if epulet[i].Ath == '':
            epulet[i].Ath = 0.0
        epulet[i].nEth = float(epulet[i].Ee_vil) * float(epulet[i].Ath)

        if epulet[i].Ee_vil != 0.0:
            epulet[i].pote = 1.0 - (float(epulet[i].Ee_vil_cs) / float(epulet[i].Ee_vil))
        else:
            epulet[i].pote = 0.0

        epulet[i].Ee_vil_real = float(epulet[i].Ee_vil) * float(epulet[i].k)
        epulet[i].Qe_vil = float(epulet[i].Ee_vil) * float(epulet[i].Ter_est)
        epulet[i].Qe_vil_real = float(epulet[i].Qe_vil) * float(epulet[i].k)
        epulet[i].Qe_vil_cs = float(epulet[i].Ee_vil_cs) * float(epulet[i].Ter_est)
        epulet[i].Qe_vil_real_cs = float(epulet[i].Qe_vil_cs) * float(epulet[i].k)

        epulet[i].Qel = float(epulet[i].nEel) * float(epulet[i].Ter_est)
        epulet[i].Qel_csil = float(epulet[i].nEel_csil) * float(epulet[i].Ter_est)
        epulet[i].Qga = float(epulet[i].nEga) * float(epulet[i].Ter_est)
        epulet[i].Qol = float(epulet[i].nEol) * float(epulet[i].Ter_est)
        epulet[i].Qsz = float(epulet[i].nEsz) * float(epulet[i].Ter_est)
        epulet[i].Qbm = float(epulet[i].nEbm) * float(epulet[i].Ter_est)
        epulet[i].Qth = float(epulet[i].nEth) * float(epulet[i].Ter_est)

        epulet[i].Qel_cs = float(epulet[i].Eel_cs) * float(epulet[i].Ter_est)
        epulet[i].Qel_cs_cs = float(epulet[i].Eel_cs_cs) * float(epulet[i].Ter_est)
        epulet[i].Qga_cs = float(epulet[i].Ega_cs) * float(epulet[i].Ter_est)
        epulet[i].Qol_cs = float(epulet[i].Eol_cs) * float(epulet[i].Ter_est)
        epulet[i].Qsz_cs = float(epulet[i].Esz_cs) * float(epulet[i].Ter_est)
        epulet[i].Qbm_cs = float(epulet[i].Ebm_cs) * float(epulet[i].Ter_est)
        epulet[i].Qth_cs = float(epulet[i].Eth_cs) * float(epulet[i].Ter_est)

        epulet[i].Qel_real = float(epulet[i].Qel) / float(epulet[i].eel) * float(epulet[i].k)
        epulet[i].Qel_cs_real = float(epulet[i].Qel_cs) / float(epulet[i].eelcs) * float(epulet[i].k)
        epulet[i].Qga_real = float(epulet[i].Qga) / float(epulet[i].ega) * float(epulet[i].k)
        epulet[i].Qol_real = float(epulet[i].Qol) / float(epulet[i].eol) * float(epulet[i].k)
        epulet[i].Qsz_real = float(epulet[i].Qsz) / float(epulet[i].esz) * float(epulet[i].k)
        epulet[i].Qbm_real = float(epulet[i].Qbm) / float(epulet[i].ebm) * float(epulet[i].k)
        epulet[i].Qth_real = float(epulet[i].Qth) / float(epulet[i].eth) * float(epulet[i].k)

        epulet[i].Qel_real_cs = float(epulet[i].Qel_cs) / float(epulet[i].eel) * float(epulet[i].k)
        epulet[i].Qel_cs_real_cs = float(epulet[i].Qel_cs_cs) / float(epulet[i].eelcs) * float(epulet[i].k)
        epulet[i].Qga_real_cs = float(epulet[i].Qga_cs) / float(epulet[i].ega) * float(epulet[i].k)
        epulet[i].Qol_real_cs = float(epulet[i].Qol_cs) / float(epulet[i].eol) * float(epulet[i].k)
        epulet[i].Qsz_real_cs = float(epulet[i].Qsz_cs) / float(epulet[i].esz) * float(epulet[i].k)
        epulet[i].Qbm_real_cs = float(epulet[i].Qbm_cs) / float(epulet[i].ebm) * float(epulet[i].k)
        epulet[i].Qth_real_cs = float(epulet[i].Qth_cs) / float(epulet[i].eth) * float(epulet[i].k)
        
        if epulet[i].d_el == '' or epulet[i].d_el == 0.0 or epulet[i].d_el == 0:
            epulet[i].d_el = epulet[i].delest
        if epulet[i].delcs == '' or epulet[i].delcs == 0.0 or epulet[i].delcs == 0:
            epulet[i].delcs = epulet[i].delcsest
        if epulet[i].dga == '' or epulet[i].dga == 0.0 or epulet[i].dga == 0:
            epulet[i].dga = epulet[i].dgaest
        if epulet[i].dol == '' or epulet[i].dol == 0.0 or epulet[i].dol == 0:
            epulet[i].dol = epulet[i].dolest
        if epulet[i].dsz == '' or epulet[i].dsz == 0.0 or epulet[i].dsz == 0:
            epulet[i].dsz = epulet[i].dszest
        if epulet[i].dbm == '' or epulet[i].dbm == 0.0 or epulet[i].dbm == 0:
            epulet[i].dbm = epulet[i].dbmest
        if epulet[i].dth == '' or epulet[i].dth == 0.0 or epulet[i].dth == 0:
            epulet[i].dth = epulet[i].dthest
        
        if epulet[i].Qel_real_cs == '':
            epulet[i].Qel_real_cs = 0.0
        if epulet[i].d_el == '':
            epulet[i].d_el = 0.0
        if epulet[i].Qel_cs_real_cs == '':
            epulet[i].Qel_cs_real_cs = 0.0
        if epulet[i].delcs == '':
            epulet[i].delcs = 0.0
        if epulet[i].Qga_real_cs == '':
            epulet[i].Qga_real_cs = 0.0
        if epulet[i].dga == '':
            epulet[i].dga = 0.0
        if epulet[i].Qol_real_cs == '':
            epulet[i].Qol_real_cs = 0.0
        if epulet[i].dol == '':
            epulet[i].dol = 0.0
        if epulet[i].Qsz_real_cs == '':
            epulet[i].Qsz_real_cs = 0.0
        if epulet[i].dsz == '':
            epulet[i].dsz = 0.0
        if epulet[i].Qbm_real_cs == '':
            epulet[i].Qbm_real_cs = 0.0
        if epulet[i].dbm == '':
            epulet[i].dbm = 0.0
        if epulet[i].Qth_real_cs == '':
            epulet[i].Qth_real_cs = 0.0
        if epulet[i].dth == '':
            epulet[i].dth = 0.0

        epulet[i].De_cs = (
            (float(epulet[i].Qel_real_cs) * float(epulet[i].d_el)) + 
            (float(epulet[i].Qel_cs_real_cs) * float(epulet[i].delcs)) +
            (float(epulet[i].Qga_real_cs) * float(epulet[i].dga)) +
            (float(epulet[i].Qol_real_cs) * float(epulet[i].dol)) +
            (float(epulet[i].Qsz_real_cs) * float(epulet[i].dsz)) +
            (float(epulet[i].Qbm_real_cs) * float(epulet[i].dbm)) +
            (float(epulet[i].Qth_real_cs) * float(epulet[i].dth)))
        
        epulet[i].De = (
            (float(epulet[i].Qel_real) * float(epulet[i].d_el)) + 
            (float(epulet[i].Qel_cs_real) * float(epulet[i].delcs)) +
            (float(epulet[i].Qga_real) * float(epulet[i].dga)) +
            (float(epulet[i].Qol_real) * float(epulet[i].dol)) +
            (float(epulet[i].Qsz_real) * float(epulet[i].dsz)) +
            (float(epulet[i].Qbm_real) * float(epulet[i].dbm)) +
            (float(epulet[i].Qth_real) * float(epulet[i].dth)))
        
        if epulet[i].fCO2_el == '':
            epulet[i].fCO2_el = 0.0
        if epulet[i].fCO2_el_cs == '':
            epulet[i].fCO2_el_cs = 0.0
        if epulet[i].fCO2_ga == '':
            epulet[i].fCO2_ga = 0.0
        if epulet[i].fCO2_ol == '':
            epulet[i].fCO2_ol = 0.0
        if epulet[i].fCO2_sz == '':
            epulet[i].fCO2_sz = 0.0
        if epulet[i].fCO2_bm == '':
            epulet[i].fCO2_bm = 0.0
        if epulet[i].fCO2_th == '':
            epulet[i].fCO2_th = 0.0

        epulet[i].TFCO2_e = (
            (float(epulet[i].Qel_real) * float(epulet[i].fCO2_el)) + 
            (float(epulet[i].Qel_cs_real) * float(epulet[i].fCO2_el_cs)) +
            (float(epulet[i].Qga_real) * float(epulet[i].fCO2_ga)) +
            (float(epulet[i].Qol_real) * float(epulet[i].fCO2_ol)) +
            (float(epulet[i].Qsz_real) * float(epulet[i].fCO2_sz)) +
            (float(epulet[i].Qbm_real) * float(epulet[i].fCO2_bm)) +
            (float(epulet[i].Qth_real) * float(epulet[i].fCO2_th)))
        
        epulet[i].TFCO2_e_cs = (
            (float(epulet[i].Qel_real_cs) * float(epulet[i].fCO2_el)) + 
            (float(epulet[i].Qel_cs_real_cs) * float(epulet[i].fCO2_el_cs)) +
            (float(epulet[i].Qga_real_cs) * float(epulet[i].fCO2_ga)) +
            (float(epulet[i].Qol_real_cs) * float(epulet[i].fCO2_ol)) +
            (float(epulet[i].Qsz_real_cs) * float(epulet[i].fCO2_sz)) +
            (float(epulet[i].Qbm_real_cs) * float(epulet[i].fCO2_bm)) +
            (float(epulet[i].Qth_real_cs) * float(epulet[i].fCO2_th)))
        
        epulet[i].deltaTFCO2_e = epulet[i].TFCO2_e - epulet[i].TFCO2_e_cs
    
    print("Epulet done.")
    return epulet

def writer(output, head, data):
    print("Writing Epulet-out")
    write.writer(output, head, data)
    print("Done.")           

# for debugging purposes:
if __name__ == '__main__':
    calculate(epulet)
    print(" ")