import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/work/innoregio/kataszteri_szamolhato/szarvasko_tomb.csv')
tomb = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inptel = read.dataframe('/home/jeda/work/innoregio/output/telek-szarvasko-out.csv')
telek = [csvhandler.Dict(i, inptel[0]) for i in inptel[1:]]
inpep = read.dataframe('/home/jeda/work/innoregio/output/szarvasko_epulet-out.csv')
epulet = [csvhandler.Dict(i, inpep[0]) for i in inpep[1:]]
out = '/home/jeda/work/innoregio/output/tomb-szarvasko-out.csv'
head = write.header(tomb)
##############################################################

def calculate(tomb, telek, epulet):
    print("Calculations with data in Epulet and Tomb:")
    for i in tqdm(range(len(epulet))):
        for j in range(len(tomb)):
            if epulet[i].Tombazonosito.strip() == tomb[j].Tombazonosito.strip():
                # 2
                Tipusszam = epulet[i].Tipusszam_est if epulet[i].Tipusszam == '' else epulet[i].Tipusszam
                Ter = float(epulet[i].Ter_est) if epulet[i].Ter == '' else float(epulet[i].Ter)
                if tomb[j].T_L1 == '':
                    tomb[j].T_L1 = 0.0
                if "L1" in Tipusszam:
                    tomb[j].T_L1 = float(tomb[j].T_L1) + Ter
                if tomb[j].T_L1_M == '':
                    tomb[j].T_L1_M = 0.0
                if "L1_M" in Tipusszam:
                    tomb[j].T_L1_M = float(tomb[j].T_L1_M) + Ter
                if tomb[j].T_L2 == '':
                    tomb[j].T_L2 = 0.0
                if "L2" in Tipusszam:
                    tomb[j].T_L2 = float(tomb[j].T_L2) + Ter
                if tomb[j].T_L2_M == '':
                    tomb[j].T_L2_M = 0.0
                if "L2_M" in Tipusszam:
                    tomb[j].T_L2_M = float(tomb[j].T_L2_M) + Ter
                if tomb[j].T_L3 == '':
                    tomb[j].T_L3 = 0.0
                if "L3" in Tipusszam:
                    tomb[j].T_L3 = float(tomb[j].T_L3) + Ter
                if tomb[j].T_L3_F == '':
                    tomb[j].T_L3_F = 0.0
                if "L3_F" in Tipusszam:
                    tomb[j].T_L3_F = float(tomb[j].T_L3_F) + Ter
                if tomb[j].T_L4 == '':
                    tomb[j].T_L4 = 0.0
                if "L4" in Tipusszam:
                    tomb[j].T_L4 = float(tomb[j].T_L4) + Ter
                if tomb[j].T_L4_F == '':
                    tomb[j].T_L4_F = 0.0
                if "L4_F" in Tipusszam:
                    tomb[j].T_L4_F = float(tomb[j].T_L4_F) + Ter
                if tomb[j].T_L5 == '':
                    tomb[j].T_L5 = 0.0
                if "L5" in Tipusszam:
                    tomb[j].T_L5 = float(tomb[j].T_L5) + Ter
                if tomb[j].T_L5_F == '':
                    tomb[j].T_L5_F = 0.0
                if "L5_F" in Tipusszam:
                    tomb[j].T_L5_F = float(tomb[j].T_L5_F) + Ter
                if tomb[j].T_L6 == '':
                    tomb[j].T_L6 = 0.0
                if "L6" in Tipusszam:
                    tomb[j].T_L6 = float(tomb[j].T_L6) + Ter
                if tomb[j].T_L6_M == '':
                    tomb[j].T_L6_M = 0.0
                if "L6_M" in Tipusszam:
                    tomb[j].T_L6_M = float(tomb[j].T_L6_M) + Ter
                if tomb[j].T_L7 == '':
                    tomb[j].T_L7 = 0.0
                if "L7" in Tipusszam:
                    tomb[j].T_L7 = float(tomb[j].T_L7) + Ter
                if tomb[j].T_L8 == '':
                    tomb[j].T_L8 = 0.0
                if "L8" in Tipusszam:
                    tomb[j].T_L8 = float(tomb[j].T_L8) + Ter
                if tomb[j].T_L8_M == '':
                    tomb[j].T_L8_M = 0.0
                if "L8_M" in Tipusszam:
                    tomb[j].T_L8_M = float(tomb[j].T_L8_M) + Ter
                if tomb[j].T_L9 == '':
                    tomb[j].T_L9 = 0.0
                if "L9" in Tipusszam:
                    tomb[j].T_L9 = float(tomb[j].T_L9) + Ter
                if tomb[j].T_L10_A == '':
                    tomb[j].T_L10_A = 0.0
                if "L10_A" in Tipusszam:
                    tomb[j].T_L10_A = float(tomb[j].T_L10_A) + Ter
                if tomb[j].T_L10_B == '':
                    tomb[j].T_L10_B = 0.0
                if "L10_B" in Tipusszam:
                    tomb[j].T_L10_B = float(tomb[j].T_L10_B) + Ter
                if tomb[j].T_L11_A == '':
                    tomb[j].T_L11_A = 0.0
                if "L11_A" in Tipusszam:
                    tomb[j].T_L11_A = float(tomb[j].T_L11_A) + Ter
                if tomb[j].T_L11_B == '':
                    tomb[j].T_L11_B = 0.0
                if "L11_B" in Tipusszam:
                    tomb[j].T_L11_B = float(tomb[j].T_L11_B) + Ter
                if tomb[j].T_L12_A == '':
                    tomb[j].T_L12_A = 0.0
                if "L12_A" in Tipusszam:
                    tomb[j].T_L12_A = float(tomb[j].T_L12_A) + Ter
                if tomb[j].T_L12_B == '':
                    tomb[j].T_L12_B = 0.0
                if "L12_B" in Tipusszam:
                    tomb[j].T_L12_B = float(tomb[j].T_L12_B) + Ter
                if tomb[j].T_L12_F == '':
                    tomb[j].T_L12_F = 0.0
                if "L12_F" in Tipusszam:
                    tomb[j].T_L12_F = float(tomb[j].T_L12_F) + Ter
                if tomb[j].T_L13 == '':
                    tomb[j].T_L13 = 0.0
                if "L13" in Tipusszam:
                    tomb[j].T_L13 = float(tomb[j].T_L13) + Ter
                if tomb[j].T_L13_F == '':
                    tomb[j].T_L13_F = 0.0
                if "L13_F" in Tipusszam:
                    tomb[j].T_L13_F = float(tomb[j].T_L13_F) + Ter
                if tomb[j].T_K1 == '':
                    tomb[j].T_K1 = 0.0
                if "K1" in Tipusszam:
                    tomb[j].T_K1 = float(tomb[j].T_K1) + Ter
                if tomb[j].T_K1_M == '':
                    tomb[j].T_K1_M = 0.0
                if "K1_M" in Tipusszam:
                    tomb[j].T_K1_M = float(tomb[j].T_K1_M) + Ter
                if tomb[j].T_K2 == '':
                    tomb[j].T_K2 = 0.0
                if "K2" in Tipusszam:
                    tomb[j].T_K2 = float(tomb[j].T_K2) + Ter
                if tomb[j].T_K2_F == '':
                    tomb[j].T_K2_F = 0.0
                if "K2_F" in Tipusszam:
                    tomb[j].T_K2_F = float(tomb[j].T_K2_F) + Ter
                if tomb[j].T_K3 == '':
                    tomb[j].T_K3 = 0.0
                if "K3" in Tipusszam:
                    tomb[j].T_K3 = float(tomb[j].T_K3) + Ter
                if tomb[j].T_K3_M == '':
                    tomb[j].T_K3_M = 0.0
                if "K3_M" in Tipusszam:
                    tomb[j].T_K3_M = float(tomb[j].T_K3_M) + Ter
                if tomb[j].T_K4 == '':
                    tomb[j].T_K4 = 0.0
                if "K4" in Tipusszam:
                    tomb[j].T_K4 = float(tomb[j].T_K4) + Ter
                if tomb[j].T_K4_F == '':
                    tomb[j].T_K4_F = 0.0
                if "K4_F" in Tipusszam:
                    tomb[j].T_K4_F = float(tomb[j].T_K4_F) + Ter
                if tomb[j].T_K5 == '':
                    tomb[j].T_K5 = 0.0
                if "K5" in Tipusszam:
                    tomb[j].T_K5 = float(tomb[j].T_K5) + Ter
                if tomb[j].T_K5_F == '':
                    tomb[j].T_K5_F = 0.0
                if "K5_F" in Tipusszam:
                    tomb[j].T_K5_F = float(tomb[j].T_K5_F) + Ter
                if tomb[j].T_K6 == '':
                    tomb[j].T_K6 = 0.0
                if "K6" in Tipusszam:
                    tomb[j].T_K6 = float(tomb[j].T_K6) + Ter
                if tomb[j].T_K6_M == '':
                    tomb[j].T_K6_M = 0.0
                if "K6_M" in Tipusszam:
                    tomb[j].T_K6_M = float(tomb[j].T_K6_M) + Ter
                if tomb[j].T_K7 == '':
                    tomb[j].T_K7 = 0.0
                if "K7" in Tipusszam:
                    tomb[j].T_K7 = float(tomb[j].T_K7) + Ter
                if tomb[j].T_K7_F == '':
                    tomb[j].T_K7_F = 0.0
                if "K7_F" in Tipusszam:
                    tomb[j].T_K7_F = float(tomb[j].T_K7_F) + Ter
                if tomb[j].T_K8 == '':
                    tomb[j].T_K8 = 0.0
                if "K8" in Tipusszam:
                    tomb[j].T_K8 = float(tomb[j].T_K8) + Ter
                if tomb[j].T_K8_M == '':
                    tomb[j].T_K8_M = 0.0
                if "K8_M" in Tipusszam:
                    tomb[j].T_K8_M = float(tomb[j].T_K8_M) + Ter
                if tomb[j].T_K9 == '':
                    tomb[j].T_K9 = 0.0
                if "K9" in Tipusszam:
                    tomb[j].T_K9 = float(tomb[j].T_K9) + Ter
                if tomb[j].T_K10 == '':
                    tomb[j].T_K10 = 0.0
                if "K10" in Tipusszam:
                    tomb[j].T_K10 = float(tomb[j].T_K10) + Ter
                if tomb[j].T_K10_F == '':
                    tomb[j].T_K10_F = 0.0
                if "K10_F" in Tipusszam:
                    tomb[j].T_K10_F = float(tomb[j].T_K10_F) + Ter
                if tomb[j].T_K11 == '':
                    tomb[j].T_K11 = 0.0
                if "K11" in Tipusszam:
                    tomb[j].T_K11 = float(tomb[j].T_K11) + Ter
                if tomb[j].T_K11_F == '':
                    tomb[j].T_K11_F = 0.0
                if "K11_F" in Tipusszam:
                    tomb[j].T_K11_F = float(tomb[j].T_K11_F) + Ter
                if tomb[j].T_K12 == '':
                    tomb[j].T_K12 = 0.0
                if "K12" in Tipusszam:
                    tomb[j].T_K12 = float(tomb[j].T_K12) + Ter
                if tomb[j].T_K12_M == '':
                    tomb[j].T_K12_M = 0.0
                if "K12_M" in Tipusszam:
                    tomb[j].T_K12_M = float(tomb[j].T_K12_M) + Ter
                if tomb[j].T_K13 == '':
                    tomb[j].T_K13 = 0.0
                if "K13" in Tipusszam:
                    tomb[j].T_K13 = float(tomb[j].T_K13) + Ter
                if tomb[j].T_K13_F == '':
                    tomb[j].T_K13_F = 0.0
                if "K13_F" in Tipusszam:
                    tomb[j].T_K13_F = float(tomb[j].T_K13_F) + Ter
                if tomb[j].T_K14 == '':
                    tomb[j].T_K14 = 0.0
                if "K14" in Tipusszam:
                    tomb[j].T_K14 = float(tomb[j].T_K14) + Ter
                if tomb[j].T_K14_F == '':
                    tomb[j].T_K14_F = 0.0
                if "K14_F" in Tipusszam:
                    tomb[j].T_K14_F = float(tomb[j].T_K14_F) + Ter
                if tomb[j].T_I1A == '':
                    tomb[j].T_I1A = 0.0
                if "I1A" in Tipusszam:
                    tomb[j].T_I1A = float(tomb[j].T_I1A) + Ter
                if tomb[j].T_I1B == '':
                    tomb[j].T_I1B = 0.0
                if "I1B" in Tipusszam:
                    tomb[j].T_I1B = float(tomb[j].T_I1B) + Ter
                if tomb[j].T_I2A == '':
                    tomb[j].T_I2A = 0.0
                if "I2A" in Tipusszam:
                    tomb[j].T_I2A = float(tomb[j].T_I2A) + Ter
                if tomb[j].T_I2B == '':
                    tomb[j].T_I2B = 0.0
                if "I2B" in Tipusszam:
                    tomb[j].T_I2B = float(tomb[j].T_I2B) + Ter
                if tomb[j].T_I3A == '':
                    tomb[j].T_I3A = 0.0
                if "I3A" in Tipusszam:
                    tomb[j].T_I3A = float(tomb[j].T_I3A) + Ter
                if tomb[j].T_I3B == '':
                    tomb[j].T_I3B = 0.0
                if "I3B" in Tipusszam:
                    tomb[j].T_I3B = float(tomb[j].T_I3B) + Ter
                if tomb[j].T_E == '':
                    tomb[j].T_E = 0.0
                if "I" in Tipusszam:
                    tomb[j].T_E = float(tomb[j].T_E) + Ter

    print("Calculations with data in Telek and Tomb:")
    for i in tqdm(range(len(telek))):
        for j in range(len(tomb)):
            # yeah, well it is necessary becaouse of missing data equals missing calculations in other tables, so it needs to be given a value, else the program is broken.
            if tomb[j].adat_t == '':
                tomb[j].adat_t = 0.0
            if telek[i].adat_t == '':
                telek[i].adat_t = 0.0
            if telek[i].Qt_el_real_cs == '':
                telek[i].Qt_el_real_cs = 0.0
            if telek[i].Qt_el_cs_real_cs == '':
                telek[i].Qt_el_cs_real_cs = 0.0
            if telek[i].Qt_ga_real_cs == '':
                telek[i].Qt_ga_real_cs = 0.0
            if telek[i].Qt_ol_real_cs == '':
                telek[i].Qt_ol_real_cs = 0.0
            if telek[i].Qt_sz_real_cs == '':
                telek[i].Qt_sz_real_cs = 0.0
            if telek[i].Qt_bm_real_cs == '':
                telek[i].Qt_bm_real_cs = 0.0
            if telek[i].Qt_th_real_cs == '':
                telek[i].Qt_th_real_cs = 0.0
            if telek[i].Qt_el_real == '':
                telek[i].Qt_el_real = 0.0
            if telek[i].Qt_el_cs_real == '':
                telek[i].Qt_el_cs_real = 0.0
            if telek[i].Qt_ga_real == '':
                telek[i].Qt_ga_real = 0.0
            if telek[i].Qt_ol_real == '':
                telek[i].Qt_ol_real = 0.0
            if telek[i].Qt_sz_real == '':
                telek[i].Qt_sz_real = 0.0
            if telek[i].Qt_bm_real == '':
                telek[i].Qt_bm_real = 0.0
            if telek[i].Qt_th_real == '':
                telek[i].Qt_th_real = 0.0
            # main cycle    
            if telek[i].Tombazonosito.strip() == tomb[j].Tombazonosito.strip():
                # 1
                tomb[j].adat_t = float(tomb[j].adat_t) + float(telek[i].adat_t)
                if tomb[j].adat_t == 0:
                    tomb[j].adat_T = 0
                else:
                    tomb[j].adat_T = 1
                # 3
                if tomb[j].QT_vil_cs == '':
                    tomb[j].QT_vil_cs = 0.0
                tomb[j].QT_vil_cs = float(tomb[j].QT_vil_cs) + float(telek[i].Qt_vil_cs)
                # 4
                if tomb[j].QT_vil_real_cs == '':
                    tomb[j].QT_vil_real_cs = 0.0
                tomb[j].QT_vil_real_cs = float(tomb[j].QT_vil_real_cs) + float(telek[i].Qt_vil_real_cs)
                # 5
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
                # 6
                if tomb[j].QT_vil == '':
                    tomb[j].QT_vil = 0.0
                tomb[j].QT_vil = float(tomb[j].QT_vil) + float(telek[i].Qt_vil)
                # 7
                if tomb[j].QT_vil_real == '':
                    tomb[j].QT_vil_real = 0.0
                tomb[j].QT_vil_real = float(tomb[j].QT_vil_real) + float(telek[i].Qt_vil_real)
                # 8
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
                # 9
                if tomb[j].deltaQT == '':
                    tomb[j].deltaQT = 0.0
                tomb[j].deltaQT = float(tomb[j].deltaQT) + float(telek[i].deltaQt)
                # 10
                if tomb[j].TFCO2_T == '':
                    tomb[j].TFCO2_T = 0.0
                tomb[j].TFCO2_T = float(tomb[j].TFCO2_T) + float(telek[i].TFCO2_t)
                # 11
                if tomb[j].TFCO2_T_cs == '':
                    tomb[j].TFCO2_T_cs = 0.0
                tomb[j].TFCO2_T_cs = float(tomb[j].TFCO2_T_cs) + float(telek[i].TFCO2_t_cs)
                # 12
                if tomb[j].TT_t == '':
                    tomb[j].TT_t = 0.0
                tomb[j].TT_t = float(tomb[j].TT_t) + float(telek[i].Tt_t)
                if tomb[j].TT_e == '':
                    tomb[j].TT_e = 0.0
                tomb[j].TT_e = float(tomb[j].TT_e) + float(telek[i].Tt_e)
    
    print("Calculations with data in Tomb:")
    for i in tqdm(range(len(tomb))):
        # 14 and 15 in nested form
        if float(tomb[i].TT_t) != 0.0:
            tomb[i].ET_vil_t_cs = float(tomb[i].QT_vil_cs) / float(tomb[i].TT_t)
            tomb[i].ET_vil_real_t_cs = float(tomb[i].QT_vil_real_cs) / float(tomb[i].TT_t)
            tomb[i].ET_vil_t = float(tomb[i].QT_vil) / float(tomb[i].TT_t)
            tomb[i].ET_vil_real_t = float(tomb[i].QT_vil_real) / float(tomb[i].TT_t)
            tomb[i].deltaET_t = float(tomb[i].deltaQT) / float(tomb[i].TT_t)
            if float(tomb[i].ET_vil_t) != 0.0:
                tomb[i].potT = 1 - float(tomb[i].ET_vil_t_cs) / float(tomb[i].ET_vil_t)

        if float(tomb[i].TT_e) != 0.0:
            tomb[i].ET_vil_e_cs = float(tomb[i].QT_vil_cs) / float(tomb[i].TT_e)
            tomb[i].ET_vil_real_e_cs = float(tomb[i].QT_vil_real_cs) / float(tomb[i].TT_e)
            tomb[i].ET_vil_e = float(tomb[i].QT_vil) / float(tomb[i].TT_e)
            tomb[i].ET_vil_real_e = float(tomb[i].QT_vil_real) / float(tomb[i].TT_e)
            tomb[i].deltaET_e = float(tomb[i].deltaQT) / float(tomb[i].TT_e)
            if float(tomb[i].ET_vil_e) != 0.0:
                tomb[i].potT = 1 - float(tomb[i].ET_vil_e_cs) / float(tomb[i].ET_vil_e)
        # 13
        tomb[i].deltaQT_el_real = float(tomb[i].QT_el_real) - float(tomb[i].QT_el_real_cs)
        tomb[i].deltaQT_el_cs_real = float(tomb[i].QT_el_cs_real) - float(tomb[i].QT_el_cs_real_cs)
        tomb[i].deltaQT_ga_real = float(tomb[i].QT_ga_real) - float(tomb[i].QT_ga_real_cs)
        tomb[i].deltaQT_ol_real = float(tomb[i].QT_ol_real) - float(tomb[i].QT_ol_real_cs)
        tomb[i].deltaQT_sz_real = float(tomb[i].QT_sz_real) - float(tomb[i].QT_sz_real_cs)
        tomb[i].deltaQT_bm_real = float(tomb[i].QT_bm_real) - float(tomb[i].QT_bm_real_cs)
        tomb[i].deltaQT_th_real = float(tomb[i].QT_th_real) - float(tomb[i].QT_th_real_cs)
        # 17
        tomb[i].deltaTFCO2_T = float(tomb[i].TFCO2_T) - float(tomb[i].TFCO2_T_cs)
        # 16
        if float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L1) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult kis csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L1_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo kis csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L2) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult nagy csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L2_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo nagy csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L3) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott epult csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L3_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1980-89 kozott epult csaladi hazakeval megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L4) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990-2001 kozott epult csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L4_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1990-2001 kozott epult csaladi hazakeval megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L5) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '2002 utan epult csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L5_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'A 2002 utan epult csaladi hazakeval megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett csaladi haz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L6) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '2002 elott epult kis tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L6_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo kis tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L7) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '2002 utan epult tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L8) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1946 elott epult nagy tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L8_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo nagy tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L9) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1946-2001 kozott epult nagy tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L10_A) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 elott, blokkos epítesi moddal epult tarsashaz, fűtetlen kozos kozlekedovel.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L10_B) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 elott, blokkos epítesi moddal epult tarsashaz, fűtott kozos kozlekedovel.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L11_A) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott, ontottfalas epítesi moddal epult tarsashaz, fűtetlen kozos kozlekedovel.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L11_B) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott, ontottfalas epítesi moddal epult tarsashaz, fűtott kozos kozlekedovel.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L12_A) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott, ontottfalas epítesi moddal epult tarsashaz, fűtetlen kozos kozlekedovel.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L12_B) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott, ontottfalas epítesi moddal epult tarsashaz, fűtott kozos kozlekedovel.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L12_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1980-89 kozott, ontottfalas epítesi moddal epult tarsashazakeval megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L13) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 elott, paneles epítesi moddal epult tarsashaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_L13_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1990 elott, paneles epítesi moddal epult tarsashazakeval megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett tarsashaz.'
        
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K1) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult egeszsegugyi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K1_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo egeszsegugyi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K2) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 utan epult egeszsegugyi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K2_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1980 utan epult  egeszsegugyi epuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett egeszsegugyi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K3) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult irodaepulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K3_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo irodaepulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K4) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott epult irodahaz.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K4_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1980-89 kozott epult irodaepuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett irodaepulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K5) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 utan epult irodaepulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K5_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1990 utan epult irodaepuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett irodaepulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K6) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult kereskedelmi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K6_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo kereskedelmi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K7) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 utan epult kereskedelmi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K7_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1980 utan epult kereskedelmi epuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett kereskedelmi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K8) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1946 elott epult kulturalis epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K8_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo kulturalis epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K9) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1946-79 kozott epult kulturalis epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K10) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott epult kulturalis epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K10_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1980-89 kozott epult kulturalis epuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett kulturalis epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K11) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 utan epult kulturalis epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K11_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1990 utan epult kulturalis epuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett kulturalis epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K12) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult oktatasi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K12_M) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Műemleki/egyeb vedettseg alatt allo oktatasi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K13) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott epult oktatasi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K13_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1980-89 kozott epult oktatasi epuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett oktatasi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K14) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 utan epult oktatasi epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_K14_F) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Az 1990 utan epult oktatasi epuletekevel megegyezo energetikai teljesítmenyű, de regebbi epítesű, energetikai korszerűsítesen atesett oktatasi epulet.'
        
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_I1A) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult, fűtott ipari epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_I1B) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980 elott epult, temperalt (alacsony fűtesi igenyű) ipari epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_I2A) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott epult, fűtott ipari epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_I2B) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1980-89 kozott epult, temperalt (alacsony fűtesi igenyű) ipari epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_I3A) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 utan epult, fűtott ipari epulet.'
        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_I3B) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = '1990 utan epult, fűtott ipari epulet.'

        elif float(tomb[i].TT_e) != 0.0 and (float(tomb[i].T_E) / float(tomb[i].TT_e)) > 0.4:
            tomb[i].tomb_leiras = 'Egyedi tipusu epulet.'
        else:
            if tomb[i].adat_T == 0:
                tomb[i].tomb_leiras = 'Tömb energetikai jellemzői nem ismertek.'
            else:
                tomb[i].tomb_leiras = 'Vegyes típusu epuletekbol allo tomb'

    print("Tomb done.")
    return tomb

def writer(output, head, data):
    print("Writing Tomb-out")
    write.writer(output, head, data)
    print("Done.")  

# for debugging purposes:
if __name__ == '__main__':
    calculate(tomb, telek, epulet)
    writer(out, head, tomb)
    print(" ")
