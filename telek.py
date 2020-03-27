import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/telek.csv')
telek = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inpep = read.dataframe('/home/jeda/Work/innoregio/output/epulet-out.csv')
epulet = [csvhandler.Dict(i, inpep[0]) for i in inpep[1:]]
##############################################################

def calculate(telek, epulet):
    print("Calculations with data in Epulet and Telek::")
    for i in tqdm(range(len(epulet))):
        for j in range(len(telek)):
            if epulet[i].Helyrajziszam == telek[j].Helyrajziszam:
                telek[j].Qt_vil_cs = float(telek[j].Qt_vil_cs) + float(epulet[i].Qe_vil_cs)
                telek[j].Qt_vil_real_cs = float(telek[j].Qt_vil_real_cs) + float(epulet[i].Qe_vil_real_cs)
                if telek[j].Qt_el_real_cs == '':
                    telek[j].Qt_el_real_cs = 0.0
                telek[j].Qt_el_real_cs = float(telek[j].Qt_el_real_cs) + float(epulet[i].Qel_real_cs)
                if telek[j].Qt_el_cs_real_cs == '':
                    telek[j].Qt_el_cs_real_cs = 0.0
                telek[j].Qt_el_cs_real_cs = float(telek[j].Qt_el_cs_real_cs) + float(epulet[i].Qel_cs_real_cs)
                if telek[j].Qt_ga_real_cs == '':
                    telek[j].Qt_ga_real_cs = 0.0
                telek[j].Qt_ga_real_cs = float(telek[j].Qt_ga_real_cs) + float(epulet[i].Qga_real_cs)
                if telek[j].Qt_ol_real_cs == '':
                    telek[j].Qt_ol_real_cs = 0.0
                telek[j].Qt_ol_real_cs = float(telek[j].Qt_ol_real_cs) + float(epulet[i].Qol_real_cs)
                if telek[j].Qt_sz_real_cs == '':
                    telek[j].Qt_sz_real_cs = 0.0
                telek[j].Qt_sz_real_cs = float(telek[j].Qt_sz_real_cs) + float(epulet[i].Qsz_real_cs)
                if telek[j].Qt_bm_real_cs == '':
                    telek[j].Qt_bm_real_cs = 0.0
                telek[j].Qt_bm_real_cs = float(telek[j].Qt_bm_real_cs) + float(epulet[i].Qbm_real_cs)
                if telek[j].Qt_th_real_cs == '':
                    telek[j].Qt_th_real_cs = 0.0
                telek[j].Qt_th_real_cs = float(telek[j].Qt_th_real_cs) + float(epulet[i].Qth_real_cs)
                telek[j].Dt_cs = float(telek[j].Dt_cs) + float(epulet[i].De_cs)
                telek[j].Qt_vil = float(telek[j].Qt_vil) + float(epulet[i].Qe_vil)
                telek[j].Qt_vil_real = float(telek[j].Qt_vil_real) + float(epulet[i].Qe_vil_real)
                if telek[j].Qt_el_real == '':
                    telek[j].Qt_el_real = 0.0
                telek[j].Qt_el_real = float(telek[j].Qt_el_real) + float(epulet[i].Qel_real)
                if telek[j].Qt_el_cs_real == '':
                    telek[j].Qt_el_cs_real = 0.0
                telek[j].Qt_el_cs_real = float(telek[j].Qt_el_cs_real) + float(epulet[i].Qel_cs_real)
                if telek[j].Qt_ga_real == '':
                    telek[j].Qt_ga_real = 0.0
                telek[j].Qt_ga_real = float(telek[j].Qt_ga_real) + float(epulet[i].Qga_real)
                if telek[j].Qt_ol_real == '':
                    telek[j].Qt_ol_real = 0.0
                telek[j].Qt_ol_real = float(telek[j].Qt_ol_real) + float(epulet[i].Qol_real)
                if telek[j].Qt_sz_real == '':
                    telek[j].Qt_sz_real = 0.0
                telek[j].Qt_sz_real = float(telek[j].Qt_sz_real) + float(epulet[i].Qsz_real)
                if telek[j].Qt_bm_real == '':
                    telek[j].Qt_bm_real = 0.0
                telek[j].Qt_bm_real = float(telek[j].Qt_bm_real) + float(epulet[i].Qbm_real)
                if telek[j].Qt_th_real == '':
                    telek[j].Qt_th_real = 0.0
                telek[j].Qt_th_real = float(telek[j].Qt_th_real) + float(epulet[i].Qth_real)
                telek[j].Dt = float(telek[j].Dt) + float(epulet[i].De)
                telek[j].deltaQt = float(telek[j].deltaQt) + float(epulet[i].deltaQe)
                if telek[j].TFCO2_t_cs == '':
                    telek[j].TFCO2_t_cs = 0.0
                telek[j].TFCO2_t_cs = float(telek[j].TFCO2_t_cs) + float(epulet[i].TFCO2_e_cs)
                if telek[j].TFCO2_t == '':
                    telek[j].TFCO2_t = 0.0
                telek[j].TFCO2_t = float(telek[j].TFCO2_t) + float(epulet[i].TFCO2_e)
                if telek[j].Tt_e == '':
                    telek[j].Tt_e = 0.0
                telek[j].Tt_e = float(telek[j].Tt_e) + float(epulet[i].Ter_est)
                
                telek[j].adat_t = 0
                if epulet[i].Tipusszam == 'p':
                    telek[j].adat_t = 1
    
    print("Calculations with data in Telek:")
    for i in tqdm(range(len(telek))):
        if telek[i].Tt_e == '':
            telek[i].Tt_e = 0.0
        
        if float(telek[i].Tt_e) == 0.0:
            telek[i].Et_vil_e_cs = 0.0
            telek[i].Et_vil_real_e_cs = 0.0
            telek[i].Et_vil_e = 0.0
            telek[i].Et_vil_real_e = 0.0
            telek[i].deltaEt_e = 0.0
        
        if float(telek[i].Tt_t) == 0.0:
            telek[i].Et_vil_t_cs = 0.0
            telek[i].Et_vil_real_t_cs = 0.0
            telek[i].Et_vil_t = 0.0
            telek[i].Et_vil_real_t = 0.0
            telek[i].deltaEt_t = 0.0
        
        if float(telek[i].Tt_e) != 0.0:
            telek[i].Et_vil_e_cs = float(telek[i].Qt_vil_cs) / float(telek[i].Tt_e)            
            telek[i].Et_vil_real_e_cs = float(telek[i].Qt_vil_real_cs) / float(telek[i].Tt_e)            
            telek[i].Et_vil_e = float(telek[i].Qt_vil) / float(telek[i].Tt_e)            
            telek[i].Et_vil_real_e = float(telek[i].Qt_vil_real) / float(telek[i].Tt_e)            
            telek[i].deltaEt_e = float(telek[i].deltaQt) / float(telek[i].Tt_e)            
        
        if float(telek[i].Tt_t) != 0.0:
            telek[i].Et_vil_t_cs = float(telek[i].Qt_vil_cs) / float(telek[i].Tt_t)
            telek[i].Et_vil_real_t_cs = float(telek[i].Qt_vil_real_cs) / float(telek[i].Tt_t)
            telek[i].Et_vil_t = float(telek[i].Qt_vil) / float(telek[i].Tt_t)
            telek[i].Et_vil_real_t = float(telek[i].Qt_vil_real) / float(telek[i].Tt_t)
            telek[i].deltaEt_t = float(telek[i].deltaQt) / float(telek[i].Tt_t)
        
        if float(telek[i].TFCO2_t_cs) == 0.0:
            telek[i].deltaTFCO2_t = 0.0
        
        if float(telek[i].TFCO2_t_cs) != 0.0:
            telek[i].deltaTFCO2_t = float(telek[i].TFCO2_t) - float(telek[i].TFCO2_t_cs)

        if telek[i].Et_vil_e == '':
            telek[i].Et_vil_e = 0.0

        if float(telek[i].Et_vil_t) == 0.0 or float(telek[i].Et_vil_e) == 0.0:
            telek[i].pott = 0.0

        if float(telek[i].Et_vil_t) != 0.0:
            telek[i].pott = 1 - (float(telek[i].Et_vil_t_cs) / float(telek[i].Et_vil_t))
        
        if float(telek[i].Et_vil_e) != 0.0:
            telek[i].pott = 1 - (float(telek[i].Et_vil_e_cs) / float(telek[i].Et_vil_e))         

    print("Telek done.")
    return telek

def writer(output, head, data):
    print("Writing Telek-out")
    write.writer(output, head, data)
    print("Done.")  

# for debugging purposes:
if __name__ == '__main__':
    calculate(telek, epulet)
    print(" ")