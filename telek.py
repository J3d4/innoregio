import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/work/innoregio/input/telek-test.csv')
telek = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inpep = read.dataframe('/home/jeda/work/innoregio/output/epulet-test-out.csv')
epulet = [csvhandler.Dict(i, inpep[0]) for i in inpep[1:]]
out = '/home/jeda/work/innoregio/output/telek-test-out.csv'
head = write.header(telek)
##############################################################

def calculate(telek, epulet):
    print("Calculations with data in Epulet and Telek::")
    for i in tqdm(range(len(epulet))):
        for j in range(len(telek)):
            if epulet[i].Helyrajziszam.strip() == telek[j].Helyrajziszam.strip():
                # 1
                Epulet_funkcio = epulet[i].Epulet_funkcio_est if epulet[i].Epulet_funkcio == '' else epulet[i].Epulet_funkcio
                if 'p' in Epulet_funkcio:
                    telek[j].adat_t = 1
                else:
                    telek[j].adat_t = 0
                # 2
                if telek[j].Qt_vil_cs == '':
                    telek[j].Qt_vil_cs = 0.0
                telek[j].Qt_vil_cs = float(telek[j].Qt_vil_cs) + float(epulet[i].Qe_vil_cs)
                # 3
                if telek[j].Qt_vil_real_cs == '':
                    telek[j].Qt_vil_real_cs = 0
                telek[j].Qt_vil_real_cs = float(telek[j].Qt_vil_real_cs) + float(epulet[i].Qe_vil_real_cs)
                # 4
                Qel_real_cs = float(epulet[i].Qel_real_cs_est) if epulet[i].Qel_real_cs == '' else float(epulet[i].Qel_real_cs_est)
                Qel_cs_real_cs = float(epulet[i].Qel_cs_real_cs_est) if epulet[i].Qel_cs_real_cs == '' else float(epulet[i].Qel_cs_real_cs_est)
                Qga_real_cs = float(epulet[i].Qga_real_cs_est) if epulet[i].Qga_real_cs == '' else float(epulet[i].Qga_real_cs_est)
                Qol_real_cs = float(epulet[i].Qol_real_cs_est) if epulet[i].Qol_real_cs == '' else float(epulet[i].Qol_real_cs_est)
                Qsz_real_cs = float(epulet[i].Qsz_real_cs_est) if epulet[i].Qsz_real_cs == '' else float(epulet[i].Qsz_real_cs_est)
                Qbm_real_cs = float(epulet[i].Qbm_real_cs_est) if epulet[i].Qbm_real_cs == '' else float(epulet[i].Qbm_real_cs_est)
                Qth_real_cs = float(epulet[i].Qth_real_cs_est) if epulet[i].Qth_real_cs == '' else float(epulet[i].Qth_real_cs_est)

                if telek[j].Qt_el_real_cs == '':
                    telek[j].Qt_el_real_cs = 0.0
                telek[j].Qt_el_real_cs = float(telek[j].Qt_el_real_cs) + Qel_real_cs
                if telek[j].Qt_el_cs_real_cs == '':
                    telek[j].Qt_el_cs_real_cs = 0.0
                telek[j].Qt_el_cs_real_cs = float(telek[j].Qt_el_cs_real_cs) + Qel_cs_real_cs
                if telek[j].Qt_ga_real_cs == '':
                    telek[j].Qt_ga_real_cs = 0.0
                telek[j].Qt_ga_real_cs = float(telek[j].Qt_ga_real_cs) + Qga_real_cs
                if telek[j].Qt_ol_real_cs == '':
                    telek[j].Qt_ol_real_cs = 0.0
                telek[j].Qt_ol_real_cs = float(telek[j].Qt_ol_real_cs) + Qol_real_cs
                if telek[j].Qt_sz_real_cs == '':
                    telek[j].Qt_sz_real_cs = 0.0
                telek[j].Qt_sz_real_cs = float(telek[j].Qt_sz_real_cs) + Qsz_real_cs
                if telek[j].Qt_bm_real_cs == '':
                    telek[j].Qt_bm_real_cs = 0.0
                telek[j].Qt_bm_real_cs = float(telek[j].Qt_bm_real_cs) + Qbm_real_cs
                if telek[j].Qt_th_real_cs == '':
                    telek[j].Qt_th_real_cs = 0.0
                telek[j].Qt_th_real_cs = float(telek[j].Qt_th_real_cs) + Qth_real_cs
                # 5
                if telek[j].Dt_cs == '':
                    telek[j].Dt_cs = 0
                telek[j].Dt_cs = float(telek[j].Dt_cs) + float(epulet[i].De_cs)
                # 6
                Ter = float(epulet[i].Ter_est) if epulet[i].Ter == '' else float(epulet[i].Ter)
                if telek[j].Tt_e == '':
                    telek[j].Tt_e = 0.0
                telek[j].Tt_e = float(telek[j].Tt_e) + float(Ter)
                # 7
                if telek[j].Dt == '':
                    telek[j].Dt = 0
                telek[j].Dt = float(telek[j].Dt) + float(epulet[i].De)
                # 8
                Qel_real = float(epulet[i].Qel_real_est) if epulet[i].Qel_real == '' else float(epulet[i].Qel_real_est)
                Qel_cs_real = float(epulet[i].Qel_cs_real_est) if epulet[i].Qel_cs_real == '' else float(epulet[i].Qel_cs_real_est)
                Qga_real = float(epulet[i].Qga_real_est) if epulet[i].Qga_real == '' else float(epulet[i].Qga_real_est)
                Qol_real = float(epulet[i].Qol_real_est) if epulet[i].Qol_real == '' else float(epulet[i].Qol_real_est)
                Qsz_real = float(epulet[i].Qsz_real_est) if epulet[i].Qsz_real == '' else float(epulet[i].Qsz_real_est)
                Qbm_real = float(epulet[i].Qbm_real_est) if epulet[i].Qbm_real == '' else float(epulet[i].Qbm_real_est)
                Qth_real = float(epulet[i].Qth_real_est) if epulet[i].Qth_real == '' else float(epulet[i].Qth_real_est)

                if telek[j].Qt_el_real == '':
                    telek[j].Qt_el_real = 0.0
                telek[j].Qt_el_real = float(telek[j].Qt_el_real) + Qel_real
                if telek[j].Qt_el_cs_real == '':
                    telek[j].Qt_el_cs_real = 0.0
                telek[j].Qt_el_cs_real = float(telek[j].Qt_el_cs_real) + Qel_cs_real
                if telek[j].Qt_ga_real == '':
                    telek[j].Qt_ga_real = 0.0
                telek[j].Qt_ga_real = float(telek[j].Qt_ga_real) + Qga_real
                if telek[j].Qt_ol_real == '':
                    telek[j].Qt_ol_real = 0.0
                telek[j].Qt_ol_real = float(telek[j].Qt_ol_real) + Qol_real
                if telek[j].Qt_sz_real == '':
                    telek[j].Qt_sz_real = 0.0
                telek[j].Qt_sz_real = float(telek[j].Qt_sz_real) + Qsz_real
                if telek[j].Qt_bm_real == '':
                    telek[j].Qt_bm_real = 0.0
                telek[j].Qt_bm_real = float(telek[j].Qt_bm_real) + Qbm_real
                if telek[j].Qt_th_real == '':
                    telek[j].Qt_th_real = 0.0
                telek[j].Qt_th_real = float(telek[j].Qt_th_real) + Qth_real
                # 9
                if telek[j].Qt_vil == '':
                    telek[j].Qt_vil = 0
                telek[j].Qt_vil = float(telek[j].Qt_vil) + float(epulet[i].Qe_vil)
                # 10
                if telek[j].Qt_vil_real == '':
                    telek[j].Qt_vil_real = 0
                telek[j].Qt_vil_real = float(telek[j].Qt_vil_real) + float(epulet[i].Qe_vil_real)
                # 11
                if telek[j].deltaQt == '':
                    telek[j].deltaQt = 0
                telek[j].deltaQt = float(telek[j].deltaQt) + float(epulet[i].deltaQe)
                # 12
                if telek[j].TFCO2_t_cs == '':
                    telek[j].TFCO2_t_cs = 0.0
                telek[j].TFCO2_t_cs = float(telek[j].TFCO2_t_cs) + float(epulet[i].TFCO2_e_cs)
                # 13
                if telek[j].TFCO2_t == '':
                    telek[j].TFCO2_t = 0.0
                telek[j].TFCO2_t = float(telek[j].TFCO2_t) + float(epulet[i].TFCO2_e)
                
    print("Calculations with data in Telek:")
    for i in tqdm(range(len(telek))):
        # for bad data input 
        if telek[i].Tt_e == '':
            telek[i].Tt_e = 0.0
        if telek[i].Tt_t == '':
            telek[i].Tt_t = 0.0 
        # 14-5-6-7-8
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
        # 14-5-6-7-8 end
        
        # 19
        telek[i].deltaTFCO2_t = float(telek[i].TFCO2_t) - float(telek[i].TFCO2_t_cs)
        # 20
        if float(telek[i].Et_vil_t) != 0.0:
            telek[i].pott = 1 - (float(telek[i].Et_vil_t_cs) / float(telek[i].Et_vil_t))
        elif float(telek[i].Et_vil_e) != 0.0:
            telek[i].pott = 1 - (float(telek[i].Et_vil_e_cs) / float(telek[i].Et_vil_e)) 
        else:
            telek[i].pott = 0.0        

    print("Telek done.")
    return telek

def writer(output, head, data):
    print("Writing Telek-out")
    write.writer(output, head, data)
    print("Done.")  

# for debugging purposes:
if __name__ == '__main__':
    calculate(telek, epulet)
    writer(out, head, telek)
    print(" ")
