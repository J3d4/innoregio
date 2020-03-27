import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/tomb.csv')
tomb = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inptel = read.dataframe('/home/jeda/Work/innoregio/output/telek-out.csv')
telek = [csvhandler.Dict(i, inptel[0]) for i in inptel[1:]]
inpep = read.dataframe('/home/jeda/Work/innoregio/output/epulet-out.csv')
epulet = [csvhandler.Dict(i, inpep[0]) for i in inpep[1:]]
##############################################################

def calculate(tomb, telek, epulet):
    print("Calculations with data in Epulet and Tomb:")
    for i in tqdm(range(len(epulet))):
        for j in range(len(tomb)):
            if epulet[i].Tombazonosito == tomb[j].Tombazonosito:
                if "L1" in epulet[i].Tipusszam:
                    tomb[j].T_L1 = float(tomb[j].T_L1) + float(epulet[i].Ter_est)
                if "L1_M" in epulet[i].Tipusszam:
                    tomb[j].T_L1_M = float(tomb[j].T_L1_M) + float(epulet[i].Ter_est)
                if "L2" in epulet[i].Tipusszam:
                    tomb[j].T_L2 = float(tomb[j].T_L2) + float(epulet[i].Ter_est)
                if "L2_M" in epulet[i].Tipusszam:
                    tomb[j].T_L2_M = float(tomb[j].T_L2_M) + float(epulet[i].Ter_est)
                if "L3" in epulet[i].Tipusszam:
                    tomb[j].T_L3 = float(tomb[j].T_L3) + float(epulet[i].Ter_est)
                if "L3_F" in epulet[i].Tipusszam:
                    tomb[j].T_L3_F = float(tomb[j].T_L3_F) + float(epulet[i].Ter_est)
                if "L4" in epulet[i].Tipusszam:
                    tomb[j].T_L4 = float(tomb[j].T_L4) + float(epulet[i].Ter_est)
                if "L4_F" in epulet[i].Tipusszam:
                    tomb[j].T_L4_F = float(tomb[j].T_L4_F) + float(epulet[i].Ter_est)
                if "L5" in epulet[i].Tipusszam:
                    tomb[j].T_L5 = float(tomb[j].T_L5) + float(epulet[i].Ter_est)
                if "L5_F" in epulet[i].Tipusszam:
                    tomb[j].T_L5_F = float(tomb[j].T_L5_F) + float(epulet[i].Ter_est)
                if "L6" in epulet[i].Tipusszam:
                    tomb[j].T_L6 = float(tomb[j].T_L6) + float(epulet[i].Ter_est)
                if "L6_M" in epulet[i].Tipusszam:
                    tomb[j].T_L6_M = float(tomb[j].T_L6_M) + float(epulet[i].Ter_est)
                if "L7" in epulet[i].Tipusszam:
                    tomb[j].T_L7 = float(tomb[j].T_L7) + float(epulet[i].Ter_est)
                if "L8" in epulet[i].Tipusszam:
                    tomb[j].T_L8 = float(tomb[j].T_L8) + float(epulet[i].Ter_est)
                if "L8_M" in epulet[i].Tipusszam:
                    tomb[j].T_L8_M = float(tomb[j].T_L8_M) + float(epulet[i].Ter_est)
                if "L9" in epulet[i].Tipusszam:
                    tomb[j].T_L9 = float(tomb[j].T_L9) + float(epulet[i].Ter_est)
                if "L10_A" in epulet[i].Tipusszam:
                    tomb[j].T_L10_A = float(tomb[j].T_L10_A) + float(epulet[i].Ter_est)
                if "L10_B" in epulet[i].Tipusszam:
                    tomb[j].T_L10_B = float(tomb[j].T_L10_B) + float(epulet[i].Ter_est)
                if "L11_A" in epulet[i].Tipusszam:
                    tomb[j].T_L11_A = float(tomb[j].T_L11_A) + float(epulet[i].Ter_est)
                if "L11_B" in epulet[i].Tipusszam:
                    tomb[j].T_L11_B = float(tomb[j].T_L11_B) + float(epulet[i].Ter_est)
                if "L12_A" in epulet[i].Tipusszam:
                    tomb[j].T_L12_A = float(tomb[j].T_L12_A) + float(epulet[i].Ter_est)
                if "L12_B" in epulet[i].Tipusszam:
                    tomb[j].T_L12_B = float(tomb[j].T_L12_B) + float(epulet[i].Ter_est)
                if "L12_F" in epulet[i].Tipusszam:
                    tomb[j].T_L12_F = float(tomb[j].T_L12_F) + float(epulet[i].Ter_est)
                if "L13" in epulet[i].Tipusszam:
                    tomb[j].T_L13 = float(tomb[j].T_L13) + float(epulet[i].Ter_est)
                if "L13_F" in epulet[i].Tipusszam:
                    tomb[j].T_L13_F = float(tomb[j].T_L13_F) + float(epulet[i].Ter_est)
                if "K1" in epulet[i].Tipusszam:
                    tomb[j].T_K1 = float(tomb[j].T_K1) + float(epulet[i].Ter_est)
                if "K1_M" in epulet[i].Tipusszam:
                    tomb[j].T_K1_M = float(tomb[j].T_K1_M) + float(epulet[i].Ter_est)
                if "K2" in epulet[i].Tipusszam:
                    tomb[j].T_K2 = float(tomb[j].T_K2) + float(epulet[i].Ter_est)
                if "K2_F" in epulet[i].Tipusszam:
                    tomb[j].T_K2_F = float(tomb[j].T_K2_F) + float(epulet[i].Ter_est)
                if "K3" in epulet[i].Tipusszam:
                    tomb[j].T_K3 = float(tomb[j].T_K3) + float(epulet[i].Ter_est)
                if "K3_M" in epulet[i].Tipusszam:
                    tomb[j].T_K3_M = float(tomb[j].T_K3_M) + float(epulet[i].Ter_est)
                if "K4" in epulet[i].Tipusszam:
                    tomb[j].T_K4 = float(tomb[j].T_K4) + float(epulet[i].Ter_est)
                if "K4_F" in epulet[i].Tipusszam:
                    tomb[j].T_K4_F = float(tomb[j].T_K4_F) + float(epulet[i].Ter_est)
                if "K5" in epulet[i].Tipusszam:
                    tomb[j].T_K5 = float(tomb[j].T_K5) + float(epulet[i].Ter_est)
                if "K5_F" in epulet[i].Tipusszam:
                    tomb[j].T_K5_F = float(tomb[j].T_K5_F) + float(epulet[i].Ter_est)
                if "K6" in epulet[i].Tipusszam:
                    tomb[j].T_K6 = float(tomb[j].T_K6) + float(epulet[i].Ter_est)
                if "K6_M" in epulet[i].Tipusszam:
                    tomb[j].T_K6_M = float(tomb[j].T_K6_M) + float(epulet[i].Ter_est)
                if "K7" in epulet[i].Tipusszam:
                    tomb[j].T_K7 = float(tomb[j].T_K7) + float(epulet[i].Ter_est)
                if "K7_F" in epulet[i].Tipusszam:
                    tomb[j].T_K7_F = float(tomb[j].T_K7_F) + float(epulet[i].Ter_est)
                if "K8" in epulet[i].Tipusszam:
                    tomb[j].T_K8 = float(tomb[j].T_K8) + float(epulet[i].Ter_est)
                if "K8_M" in epulet[i].Tipusszam:
                    tomb[j].T_K8_M = float(tomb[j].T_K8_M) + float(epulet[i].Ter_est)
                if "K9" in epulet[i].Tipusszam:
                    tomb[j].T_K9 = float(tomb[j].T_K9) + float(epulet[i].Ter_est)
                if "K10" in epulet[i].Tipusszam:
                    tomb[j].T_K10 = float(tomb[j].T_K10) + float(epulet[i].Ter_est)
                if "K10_F" in epulet[i].Tipusszam:
                    tomb[j].T_K10_F = float(tomb[j].T_K10_F) + float(epulet[i].Ter_est)
                if "K11" in epulet[i].Tipusszam:
                    tomb[j].T_K11 = float(tomb[j].T_K11) + float(epulet[i].Ter_est)
                if "K11_F" in epulet[i].Tipusszam:
                    tomb[j].T_K11_F = float(tomb[j].T_K11_F) + float(epulet[i].Ter_est)
                if "K12" in epulet[i].Tipusszam:
                    tomb[j].T_K12 = float(tomb[j].T_K12) + float(epulet[i].Ter_est)
                if "K12_M" in epulet[i].Tipusszam:
                    tomb[j].T_K12_M = float(tomb[j].T_K12_M) + float(epulet[i].Ter_est)
                if "K13" in epulet[i].Tipusszam:
                    tomb[j].T_K13 = float(tomb[j].T_K13) + float(epulet[i].Ter_est)
                if "K13_F" in epulet[i].Tipusszam:
                    tomb[j].T_K13_F = float(tomb[j].T_K13_F) + float(epulet[i].Ter_est)
                if "K14" in epulet[i].Tipusszam:
                    tomb[j].T_K14 = float(tomb[j].T_K14) + float(epulet[i].Ter_est)
                if "K14_F" in epulet[i].Tipusszam:
                    tomb[j].T_K14_F = float(tomb[j].T_K14_F) + float(epulet[i].Ter_est)
                if "I1A" in epulet[i].Tipusszam:
                    tomb[j].T_I1A = float(tomb[j].T_I1A) + float(epulet[i].Ter_est)
                if "I1B" in epulet[i].Tipusszam:
                    tomb[j].T_I1B = float(tomb[j].T_I1B) + float(epulet[i].Ter_est)
                if "I2A" in epulet[i].Tipusszam:
                    tomb[j].T_I2A = float(tomb[j].T_I2A) + float(epulet[i].Ter_est)
                if "I2B" in epulet[i].Tipusszam:
                    tomb[j].T_I2B = float(tomb[j].T_I2B) + float(epulet[i].Ter_est)
                if "I3A" in epulet[i].Tipusszam:
                    tomb[j].T_I3A = float(tomb[j].T_I3A) + float(epulet[i].Ter_est)
                if "I3B" in epulet[i].Tipusszam:
                    tomb[j].T_I3B = float(tomb[j].T_I3B) + float(epulet[i].Ter_est)
                if "I1A" in epulet[i].Tipusszam:
                    tomb[j].T_I1A = float(tomb[j].T_I1A) + float(epulet[i].Ter_est)
                if "I" in epulet[i].Tipusszam:
                    tomb[j].T_E = float(tomb[j].T_E) + float(epulet[i].Ter_est)

    print("Calculations with data in Telek and Tomb:")
    for i in tqdm(range(len(telek))):
        for j in range(len(tomb)):
            if telek[i].Tombazonosito == tomb[j].Tombazonosito:
                
                tomb[j].adat_T = float(tomb[j].adat_T) + float(telek[i].adat_t)
                
                tomb[j].QT_vil_cs = float(tomb[j].QT_vil_cs) + float(telek[i].Qt_vil_cs)
                tomb[j].QT_vil_real_cs = float(tomb[j].QT_vil_real_cs) + float(telek[i].Qt_vil_real_cs)
                if tomb[j].QT_el_real_cs == '':
                    tomb[j].QT_el_real_cs = 0.0
                tomb[j].QT_el_real_cs = float(tomb[j].QT_el_real_cs) + float(telek[i].Qt_el_real_cs)
                if tomb[j].QT_el_cs_real_cs == '':
                    tomb[j].QT_el_cs_real_cs = 0.0
                tomb[j].QT_el_cs_real_cs = float(tomb[j].QT_el_cs_real_cs) + float(telek[i].Qt_el_cs_real_cs)
                if tomb[j].QT_ga_real_cs == '':
                    tomb[j].QT_ga_real_cs = 0.0
                tomb[j].QT_ga_real_cs = float(tomb[j].QT_ga_real_cs) + float(telek[i].Qt_ga_real_cs)
                if tomb[j].QT_ol_real_cs == '':
                    tomb[j].QT_ol_real_cs = 0.0
                tomb[j].QT_ol_real_cs = float(tomb[j].QT_ol_real_cs) + float(telek[i].Qt_ol_real_cs)
                if tomb[j].QT_sz_real_cs == '':
                    tomb[j].QT_sz_real_cs = 0.0
                tomb[j].QT_sz_real_cs = float(tomb[j].QT_sz_real_cs) + float(telek[i].Qt_sz_real_cs)
                if tomb[j].QT_bm_real_cs == '':
                    tomb[j].QT_bm_real_cs = 0.0
                tomb[j].QT_bm_real_cs = float(tomb[j].QT_bm_real_cs) + float(telek[i].Qt_bm_real_cs)
                if tomb[j].QT_th_real_cs == '':
                    tomb[j].QT_th_real_cs = 0.0
                tomb[j].QT_th_real_cs = float(tomb[j].QT_th_real_cs) + float(telek[i].Qt_th_real_cs)
                
                tomb[j].QT_vil = float(tomb[j].QT_vil) + float(telek[i].Qt_vil)
                tomb[j].QT_vil_real = float(tomb[j].QT_vil_real) + float(telek[i].Qt_vil_real)
                if tomb[j].QT_el_real == '':
                    tomb[j].QT_el_real = 0.0
                tomb[j].QT_el_real = float(tomb[j].QT_el_real) + float(telek[i].Qt_el_real)
                if tomb[j].QT_el_cs_real == '':
                    tomb[j].QT_el_cs_real = 0.0
                tomb[j].QT_el_cs_real = float(tomb[j].QT_el_cs_real) + float(telek[i].Qt_el_cs_real)
                if tomb[j].QT_ga_real == '':
                    tomb[j].QT_ga_real = 0.0
                tomb[j].QT_ga_real = float(tomb[j].QT_ga_real) + float(telek[i].Qt_ga_real)
                if tomb[j].QT_ol_real == '':
                    tomb[j].QT_ol_real = 0.0
                tomb[j].QT_ol_real = float(tomb[j].QT_ol_real) + float(telek[i].Qt_ol_real)
                if tomb[j].QT_sz_real == '':
                    tomb[j].QT_sz_real = 0.0
                tomb[j].QT_sz_real = float(tomb[j].QT_sz_real) + float(telek[i].Qt_sz_real)
                if tomb[j].QT_bm_real == '':
                    tomb[j].QT_bm_real = 0.0
                tomb[j].QT_bm_real = float(tomb[j].QT_bm_real) + float(telek[i].Qt_bm_real)
                if tomb[j].QT_th_real == '':
                    tomb[j].QT_th_real = 0.0
                tomb[j].QT_th_real = float(tomb[j].QT_th_real) + float(telek[i].Qt_th_real)
                
                tomb[j].deltaQT = float(tomb[j].deltaQT) + float(telek[i].deltaQt)
                if tomb[j].TFCO2_T == '':
                    tomb[j].TFCO2_T = 0.0
                tomb[j].TFCO2_T = float(tomb[j].TFCO2_T) + float(telek[i].TFCO2_t)
                if tomb[j].TFCO2_T_cs == '':
                    tomb[j].TFCO2_T_cs = 0.0
                tomb[j].TFCO2_T_cs = float(tomb[j].TFCO2_T_cs) + float(telek[i].TFCO2_t_cs)
                if float(telek[i].adat_t) == 1.0:
                    tomb[j].TT_t = float(tomb[j].TT_t) + float(telek[i].Tt_t)
                    if tomb[j].TT_e == '':
                        tomb[j].TT_e = 0.0
                    tomb[j].TT_e = float(tomb[j].TT_e) + float(telek[i].Tt_e)
    
    print("Calculations with data in Tomb:")
    for i in tqdm(range(len(tomb))):
        if float(tomb[i].TT_t) != 0.0:
            tomb[i].ET_vil_t_cs = float(tomb[i].QT_vil_cs) / float(tomb[i].TT_t)
            tomb[i].ET_vil_real_t_cs = float(tomb[i].QT_vil_real_cs) / float(tomb[i].TT_t)
            tomb[i].ET_vil_t = float(tomb[i].QT_vil) / float(tomb[i].TT_t)
            tomb[i].ET_vil_real_t = float(tomb[i].QT_vil_real) / float(tomb[i].TT_t)
            tomb[i].deltaET_t = float(tomb[i].deltaQT) / float(tomb[i].TT_t)
            if float(tomb[i].ET_vil_t) != 0.0:
                tomb[i].potT = 1 - float(tomb[i].ET_vil_t_cs) / float(tomb[i].ET_vil_t)
        
        if tomb[i].TT_e == '':
            tomb[i].TT_e = 0.0
        if float(tomb[i].TT_e) != 0.0:
            tomb[i].ET_vil_e_cs = float(tomb[i].QT_vil_cs) / float(tomb[i].TT_e)
            tomb[i].ET_vil_real_e_cs = float(tomb[i].QT_vil_real_cs) / float(tomb[i].TT_e)
            tomb[i].ET_vil_e = float(tomb[i].QT_vil) / float(tomb[i].TT_e)
            tomb[i].ET_vil_real_e = float(tomb[i].QT_vil_real) / float(tomb[i].TT_e)
            tomb[i].deltaET_e = float(tomb[i].deltaQT) / float(tomb[i].TT_e)
            if float(tomb[i].ET_vil_e) != 0.0:
                tomb[i].potT = 1 - float(tomb[i].ET_vil_e_cs) / float(tomb[i].ET_vil_e)

        tomb[i].deltaQT_el_real = float(tomb[i].QT_el_real) - float(tomb[i].QT_el_real_cs)
        tomb[i].deltaQT_el_cs_real = float(tomb[i].QT_el_cs_real) - float(tomb[i].QT_el_cs_real_cs)
        tomb[i].deltaQT_ga_real = float(tomb[i].QT_ga_real) - float(tomb[i].QT_ga_real_cs)
        tomb[i].deltaQT_ol_real = float(tomb[i].QT_ol_real) - float(tomb[i].QT_ol_real_cs)
        tomb[i].deltaQT_sz_real = float(tomb[i].QT_sz_real) - float(tomb[i].QT_sz_real_cs)
        tomb[i].deltaQT_bm_real = float(tomb[i].QT_bm_real) - float(tomb[i].QT_bm_real_cs)
        tomb[i].deltaQT_th_real = float(tomb[i].QT_th_real) - float(tomb[i].QT_th_real_cs)
        tomb[i].deltaQT_TFCO2_T = float(tomb[i].TFCO2_T) - float(tomb[i].TFCO2_T_cs)

        # please insert calc for tömb_leiras here:

    print("Tomb done.")
    return tomb

def writer(output, head, data):
    print("Writing Tomb-out")
    write.writer(output, head, data)
    print("Done.")  

# for debugging purposes:
if __name__ == '__main__':
    calculate(tomb, telek, epulet)
    print(" ")