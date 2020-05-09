import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/work/innoregio/input/epulet-test.csv')
epulet = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
out = '/home/jeda/work/innoregio/output/epulet-test-out.csv'
head = write.header(epulet)
##############################################################

def calculate(epulet):
    print("Calculations with epulet in Epuletek:")
    for i in tqdm(range(len(epulet))):
        # must be first for declaring the Ee variable correctly
        # x
        if epulet[i].Sz == '':
            epulet[i].Sz = 0.0
        epulet[i].Tbr = float(epulet[i].Sz) * float(epulet[i].te)
        epulet[i].Ter_est = float(epulet[i].Tbr) * float(epulet[i].Tn_Tbr)
        # -1 epulet tipus declaration sequence
        if "L" in epulet[i].Tipusszam_est:
            epulet[i].Epulet_funkcio_est = "Lakoepulet" 
        elif "K" in epulet[i].Tipusszam_est:
            epulet[i].Epulet_funkcio_est = "Kozepulet" 
        elif "I" in epulet[i].Tipusszam_est:
            epulet[i].Epulet_funkcio_est = "Ipari-uzemi epulet" 
        elif "0" in epulet[i].Tipusszam_est:
            epulet[i].Epulet_funkcio_est = "Egyeb futetlen epulet" 
        elif "X" in epulet[i].Tipusszam_est:
            epulet[i].Epulet_funkcio_est = "Nincs adat" 
        elif epulet[i].Tipusszam_est == '':
            epulet[i].Epulet_funkcio_est = ""

        if "L" in epulet[i].Tipusszam:
            epulet[i].Epulet_funkcio = "Lakoepulet" 
        elif "K" in epulet[i].Tipusszam:
            epulet[i].Epulet_funkcio = "Kozepulet" 
        elif "I" in epulet[i].Tipusszam:
            epulet[i].Epulet_funkcio = "Ipari-uzemi epulet" 
        elif "0" in epulet[i].Tipusszam:
            epulet[i].Epulet_funkcio = "Egyeb futetlen epulet" 
        elif "X" in epulet[i].Tipusszam:
            epulet[i].Epulet_funkcio = "Nincs adat"
        elif epulet[i].Tipusszam == '':
            epulet[i].Epulet_funkcio = ""
        # 0
        epulet[i].Ee_est = float(epulet[i].E0) * float(epulet[i].a)

        # region switchable variables (est or not est):
        Epulet_funkcio = epulet[i].Epulet_funkcio_est if epulet[i].Epulet_funkcio == '' else epulet[i].Epulet_funkcio
        k = float(epulet[i].k_est) if epulet[i].k == '' else float(epulet[i].k)
        Etech = float(epulet[i].Etech_est) if epulet[i].Etech == '' else float(epulet[i].Etech)
        Ter = float(epulet[i].Ter_est) if epulet[i].Ter == '' else float(epulet[i].Ter)
        Ee = float(epulet[i].Ee_est) if epulet[i].Ee == '' else float(epulet[i].Ee)
        Ee_cs = float(epulet[i].Ee_cs_est) if epulet[i].Ee_cs == '' else float(epulet[i].Ee_cs)
        Evil = float(epulet[i].Evil_est) if epulet[i].Evil == '' else float(epulet[i].Evil)
        Evil_cs = float(epulet[i].Evil_cs_est) if epulet[i].Evil_cs == '' else float(epulet[i].Evil_cs)
        # d(n)lak
        d_el_lak = float(epulet[i].delest_lak) if epulet[i].d_el_lak == '' else float(epulet[i].d_el_lak)
        delcs_lak = float(epulet[i].delcsest_lak) if epulet[i].delcs_lak == '' else float(epulet[i].delcs_lak)
        dga_lak = float(epulet[i].dgaest_lak) if epulet[i].dga_lak == '' else float(epulet[i].dga_lak)
        dol_lak = float(epulet[i].dolest_lak) if epulet[i].dol_lak == '' else float(epulet[i].dol_lak)
        dsz_lak = float(epulet[i].dszest_lak) if epulet[i].dsz_lak == '' else float(epulet[i].dsz_lak)
        dbm_lak = float(epulet[i].dbmest_lak) if epulet[i].dbm_lak == '' else float(epulet[i].dbm_lak)
        dth_lak = float(epulet[i].dthest_lak) if epulet[i].dth_lak == '' else float(epulet[i].dth_lak)
        # 1
        if Epulet_funkcio == 'Lakoepulet':
            epulet[i].delest = d_el_lak
            epulet[i].delcsest = delcs_lak
            epulet[i].dgaest = dga_lak
            epulet[i].dolest = dol_lak
            epulet[i].dszest = dsz_lak
            epulet[i].dbmest = dbm_lak
            epulet[i].dthest = dth_lak
        else:
            epulet[i].delest = 0
            epulet[i].delcsest = 0
            epulet[i].dgaest = 0
            epulet[i].dolest = 0
            epulet[i].dszest = 0
            epulet[i].dbmest = 0
            epulet[i].dthest = 0
        # d(n)
        d_el = float(epulet[i].delest) if epulet[i].d_el == '' else float(epulet[i].d_el)
        delcs = float(epulet[i].delcsest) if epulet[i].delcs == '' else float(epulet[i].delcs)
        dga = float(epulet[i].dgaest) if epulet[i].dga == '' else float(epulet[i].dga)
        dol = float(epulet[i].dolest) if epulet[i].dol == '' else float(epulet[i].dol)
        dsz = float(epulet[i].dszest) if epulet[i].dsz == '' else float(epulet[i].dsz)
        dbm = float(epulet[i].dbmest) if epulet[i].dbm == '' else float(epulet[i].dbm)
        dth = float(epulet[i].dthest) if epulet[i].dth == '' else float(epulet[i].dth)
        # alpha(n) and alpha(n)*
        Ael = float(epulet[i].Ael_est) if epulet[i].Ael == '' else float(epulet[i].Ael)
        Aelcs = float(epulet[i].Aelcs_est) if epulet[i].Aelcs == '' else float(epulet[i].Aelcs)
        Aga = float(epulet[i].Aga_est) if epulet[i].Aga == '' else float(epulet[i].Aga)
        Aol = float(epulet[i].Aol_est) if epulet[i].Aol == '' else float(epulet[i].Aol)
        Asz = float(epulet[i].Asz_est) if epulet[i].Asz == '' else float(epulet[i].Asz)
        Abm = float(epulet[i].Abm_est) if epulet[i].Abm == '' else float(epulet[i].Abm)
        Ath = float(epulet[i].Ath_est) if epulet[i].Ath == '' else float(epulet[i].Ath)

        Ael_cs = float(epulet[i].Ael_est_cs) if epulet[i].Ael_cs == '' else float(epulet[i].Ael_cs)
        Aelcs_cs = float(epulet[i].Aelcs_est_cs) if epulet[i].Aelcs_cs == '' else float(epulet[i].Aelcs_cs)
        Aga_cs = float(epulet[i].Aga_est_cs) if epulet[i].Aga_cs == '' else float(epulet[i].Aga_cs)
        Aol_cs = float(epulet[i].Aol_est_cs) if epulet[i].Aol_cs == '' else float(epulet[i].Aol_cs)
        Asz_cs = float(epulet[i].Asz_est_cs) if epulet[i].Asz_cs == '' else float(epulet[i].Asz_cs)
        Abm_cs = float(epulet[i].Abm_est_cs) if epulet[i].Abm_cs == '' else float(epulet[i].Abm_cs)
        Ath_cs = float(epulet[i].Ath_est_cs) if epulet[i].Ath_cs == '' else float(epulet[i].Ath_cs)
        # foc2(n)
        fCO2_el = float(epulet[i].fCO2_el_est) if epulet[i].fCO2_el == '' else float(epulet[i].fCO2_el)
        fCO2_el_cs = float(epulet[i].fCO2_el_cs_est) if epulet[i].fCO2_el_cs == '' else float(epulet[i].fCO2_el_cs)
        fCO2_ga = float(epulet[i].fCO2_ga_est) if epulet[i].fCO2_ga == '' else float(epulet[i].fCO2_ga)
        fCO2_ol = float(epulet[i].fCO2_ol_est) if epulet[i].fCO2_ol == '' else float(epulet[i].fCO2_ol)
        fCO2_sz = float(epulet[i].fCO2_sz_est) if epulet[i].fCO2_sz == '' else float(epulet[i].fCO2_sz)
        fCO2_bm = float(epulet[i].fCO2_bm_est) if epulet[i].fCO2_bm == '' else float(epulet[i].fCO2_bm)
        fCO2_th = float(epulet[i].fCO2_th_est) if epulet[i].fCO2_th == '' else float(epulet[i].fCO2_th)
        # endregion
        
        epulet[i].Ee_vil_cs = Ee_cs if Epulet_funkcio == 'Lakoepulet' else Ee_cs - Evil_cs
        epulet[i].Ee_vil = Ee if Epulet_funkcio == 'Lakoepulet' else Ee_cs - Evil
        
        # alpha(n) validation check:
        if float(Ael + Aelcs + Aga + Aol + Asz + Abm + Ath) > 0.9:
            epulet[i].Szum_A = True
        epulet[i].Szum_A = False
        if float(Ael_cs + Aelcs_cs + Aga_cs + Aol_cs + Asz_cs + Abm_cs + Ath_cs) > 0.9:
            epulet[i].Szum_A_cs = True
        epulet[i].Szum_A_cs = False
        # 5
        epulet[i].Ee_vil_real_cs = float(epulet[i].Ee_vil_cs) * k
        # 3
        epulet[i].deltaEe = Ee - Ee_cs
        # 4
        epulet[i].deltaQe = float(epulet[i].deltaEe) * Ter
        # 6
        epulet[i].Eel_cs = float(epulet[i].Ee_vil_cs) * Ael_cs + (Evil_cs + Etech)
        epulet[i].Eel_cs_cs = float(epulet[i].Ee_vil_cs) * Aelcs_cs
        epulet[i].Ega_cs = float(epulet[i].Ee_vil_cs) * Aga_cs
        epulet[i].Eol_cs = float(epulet[i].Ee_vil_cs) * Aol_cs
        epulet[i].Esz_cs = float(epulet[i].Ee_vil_cs) * Asz_cs
        epulet[i].Ebm_cs = float(epulet[i].Ee_vil_cs) * Abm_cs
        epulet[i].Eth_cs = float(epulet[i].Ee_vil_cs) * Ath_cs
        # 7
        epulet[i].nEel = float(epulet[i].Ee_vil) * Ael + (Evil + Etech)
        epulet[i].nEel_csil = float(epulet[i].Ee_vil) * Aelcs
        epulet[i].nEga = float(epulet[i].Ee_vil) * Aga
        epulet[i].nEol = float(epulet[i].Ee_vil) * Aol
        epulet[i].nEsz = float(epulet[i].Ee_vil) * Asz
        epulet[i].nEbm = float(epulet[i].Ee_vil) * Abm
        epulet[i].nEth = float(epulet[i].Ee_vil) * Ath
        # 8
        if epulet[i].Ee_vil != 0.0:
            epulet[i].pote = 1.0 - (float(epulet[i].Ee_vil_cs) / float(epulet[i].Ee_vil))
        else:
            epulet[i].pote = 0.0
        # 9
        epulet[i].Ee_vil_real = float(epulet[i].Ee_vil) * k
        # 10
        epulet[i].Qe_vil = float(epulet[i].Ee_vil) * Ter
        # 12
        epulet[i].Qe_vil_real = float(epulet[i].Qe_vil) * k
        # 11
        epulet[i].Qe_vil_cs = float(epulet[i].Ee_vil_cs) * Ter
        # 13
        epulet[i].Qe_vil_real_cs = float(epulet[i].Qe_vil_cs) * k
        # 15
        epulet[i].Qel = float(epulet[i].nEel) * Ter
        epulet[i].Qel_csil = float(epulet[i].nEel_csil) * Ter
        epulet[i].Qga = float(epulet[i].nEga) * Ter
        epulet[i].Qol = float(epulet[i].nEol) * Ter
        epulet[i].Qsz = float(epulet[i].nEsz) * Ter
        epulet[i].Qbm = float(epulet[i].nEbm) * Ter
        epulet[i].Qth = float(epulet[i].nEth) * Ter
        # 14
        epulet[i].Qel_cs = float(epulet[i].Eel_cs) * Ter
        epulet[i].Qel_cs_cs = float(epulet[i].Eel_cs_cs) * Ter
        epulet[i].Qga_cs = float(epulet[i].Ega_cs) * Ter
        epulet[i].Qol_cs = float(epulet[i].Eol_cs) * Ter
        epulet[i].Qsz_cs = float(epulet[i].Esz_cs) * Ter
        epulet[i].Qbm_cs = float(epulet[i].Ebm_cs) * Ter
        epulet[i].Qth_cs = float(epulet[i].Eth_cs) * Ter
        # 16
        epulet[i].Qel_real_est = float(epulet[i].Qel) / float(epulet[i].eel) * k
        epulet[i].Qel_cs_real_est = float(epulet[i].Qel_cs) / float(epulet[i].eelcs) * k
        epulet[i].Qga_real_est = float(epulet[i].Qga) / float(epulet[i].ega) * k
        epulet[i].Qol_real_est = float(epulet[i].Qol) / float(epulet[i].eol) * k
        epulet[i].Qsz_real_est = float(epulet[i].Qsz) / float(epulet[i].esz) * k
        epulet[i].Qbm_real_est = float(epulet[i].Qbm) / float(epulet[i].ebm) * k
        epulet[i].Qth_real_est = float(epulet[i].Qth) / float(epulet[i].eth) * k
        # 17
        epulet[i].Qel_real_cs_est = float(epulet[i].Qel_csil) / float(epulet[i].eel) * k
        epulet[i].Qel_cs_real_cs_est = float(epulet[i].Qel_cs_cs) / float(epulet[i].eelcs) * k
        epulet[i].Qga_real_cs_est = float(epulet[i].Qga_cs) / float(epulet[i].ega) * k
        epulet[i].Qol_real_cs_est = float(epulet[i].Qol_cs) / float(epulet[i].eol) * k
        epulet[i].Qsz_real_cs_est = float(epulet[i].Qsz_cs) / float(epulet[i].esz) * k
        epulet[i].Qbm_real_cs_est = float(epulet[i].Qbm_cs) / float(epulet[i].ebm) * k
        epulet[i].Qth_real_cs_est = float(epulet[i].Qth_cs) / float(epulet[i].eth) * k    
        # it must be done in order to calc De and De_cs correctly
        Qel_real = epulet[i].Qel_real_est if epulet[i].Qel_real == '' else float(epulet[i].Qel_real_est)
        Qel_cs_real = epulet[i].Qel_cs_real_est if epulet[i].Qel_cs_real == '' else float(epulet[i].Qel_cs_real_est)
        Qga_real = epulet[i].Qga_real_est if epulet[i].Qga_real == '' else float(epulet[i].Qga_real_est)
        Qol_real = epulet[i].Qol_real_est if epulet[i].Qol_real == '' else float(epulet[i].Qol_real_est)
        Qsz_real = epulet[i].Qsz_real_est if epulet[i].Qsz_real == '' else float(epulet[i].Qsz_real_est)
        Qbm_real = epulet[i].Qbm_real_est if epulet[i].Qbm_real == '' else float(epulet[i].Qbm_real_est)
        Qth_real = epulet[i].Qth_real_est if epulet[i].Qth_real == '' else float(epulet[i].Qth_real_est)

        Qel_real_cs = epulet[i].Qel_real_cs_est if epulet[i].Qel_real_cs == '' else float(epulet[i].Qel_real_cs_est)
        Qel_cs_real_cs = epulet[i].Qel_cs_real_cs_est if epulet[i].Qel_cs_real_cs == '' else float(epulet[i].Qel_cs_real_cs_est)
        Qga_real_cs = epulet[i].Qga_real_cs_est if epulet[i].Qga_real_cs == '' else float(epulet[i].Qga_real_cs_est)
        Qol_real_cs = epulet[i].Qol_real_cs_est if epulet[i].Qol_real_cs == '' else float(epulet[i].Qol_real_cs_est)
        Qsz_real_cs = epulet[i].Qsz_real_cs_est if epulet[i].Qsz_real_cs == '' else float(epulet[i].Qsz_real_cs_est)
        Qbm_real_cs = epulet[i].Qbm_real_cs_est if epulet[i].Qbm_real_cs == '' else float(epulet[i].Qbm_real_cs_est)
        Qth_real_cs = epulet[i].Qth_real_cs_est if epulet[i].Qth_real_cs == '' else float(epulet[i].Qth_real_cs_est)
        # De calculations:
        
        # 18
        epulet[i].De_cs = (
            (Qel_real_cs * d_el) + 
            (Qel_cs_real_cs * delcs) +
            (Qga_real_cs * dga) +
            (Qol_real_cs * dol) +
            (Qsz_real_cs * dsz) +
            (Qbm_real_cs * dbm) +
            (Qth_real_cs * dth))
        # 19   
        epulet[i].De = (
            (Qel_real * d_el) + 
            (Qel_cs_real * delcs) +
            (Qga_real * dga) +
            (Qol_real * dol) +
            (Qsz_real * dsz) +
            (Qbm_real * dbm) +
            (Qth_real * dth))
        
        # 20
        epulet[i].TFCO2_e = (
            (Qel_real * fCO2_el) + 
            (Qel_cs_real * fCO2_el_cs) +
            (Qga_real * fCO2_ga) +
            (Qol_real * fCO2_ol) +
            (Qsz_real * fCO2_sz) +
            (Qbm_real * fCO2_bm) +
            (Qth_real * fCO2_th))
        
        epulet[i].TFCO2_e_cs = (
            (Qel_real_cs * fCO2_el) + 
            (Qel_cs_real_cs * fCO2_el_cs) +
            (Qga_real_cs * fCO2_ga) +
            (Qol_real_cs * fCO2_ol) +
            (Qsz_real_cs * fCO2_sz) +
            (Qbm_real_cs * fCO2_bm) +
            (Qth_real_cs * fCO2_th))
        
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
    writer(out, head, epulet)
    print(" ")
