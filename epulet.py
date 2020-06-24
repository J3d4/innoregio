import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/vegleges/epulet.csv')
epulet = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
out = '/home/jeda/Work/innoregio/vegleges/epulet_veg.csv'
head = write.header(epulet)
##############################################################
# epulet szinten a evil* e0 stb szamolasok tipus alapjan, implementalni!!! Epulettipusokhoz rendelt adatok.xlsK
def calculate(epulet):
    print("Calculations with epulet in Epuletek:")
    for i in tqdm(range(len(epulet))):
        # must be first for declaring the Ee variable correctly
        # to not broke the calculations, if they got value change it accordingly
        epulet[i].Etech_est = 0
        epulet[i].delest_lak = 0
        epulet[i].delcsest_lak = 0
        epulet[i].dgaest_lak = 0
        epulet[i].dolest_lak = 0
        epulet[i].dszest_lak = 0
        epulet[i].dbmest_lak = 0
        epulet[i].dthest_lak = 0
        epulet[i].fCO2_el_est = 0
        epulet[i].fCO2_el_cs_est = 0
        epulet[i].fCO2_ga_est = 0
        epulet[i].fCO2_ol_est = 0
        epulet[i].fCO2_sz_est = 0
        epulet[i].fCO2_bm_est = 0
        epulet[i].fCO2_th_est = 0
        # setting static data in (like "k" and "a" values)
        epulet[i].eel = 2.5
        epulet[i].eelcs = 1.8
        epulet[i].ega = 1
        epulet[i].eol = 1
        epulet[i].esz = 1
        epulet[i].ebm = 0.6
        epulet[i].eth = 1.26
        epulet[i].a = 1
        epulet[i].k = 1
        epulet[i].Aga_est = 1
        epulet[i].Aga_est_cs = 1
        epulet[i].Abm_est = 0
        epulet[i].Abm_est_cs = 0
        epulet[i].Ael_est = 0
        epulet[i].Ael_est_cs = 0
        epulet[i].Aelcs_est = 0
        epulet[i].Aelcs_est_cs = 0
        epulet[i].Aol_est = 0
        epulet[i].Aol_est_cs = 0
        epulet[i].Asz_est = 0
        epulet[i].Asz_est_cs = 0
        epulet[i].Ath_est = 0
        epulet[i].Ath_est_cs = 0
        if "Szarvas" in epulet[i].Telepules:
            epulet[i].Aga_est = 0.5
            epulet[i].Abm_est = 0.5
            epulet[i].Aga_est_cs = 0.5
            epulet[i].Abm_est_cs = 0.5

        # just some data cleaning to do.
        if "e" in epulet[i].Tipusszam_est:
            epulet[i].Tipusszam_est = "X"
        if "p" in epulet[i].Tipusszam_est:
            epulet[i].Tipusszam_est = "X"
        if "e" in epulet[i].Tipusszam:
            epulet[i].Tipusszam = "X"
        if "p" in epulet[i].Tipusszam:
            epulet[i].Tipusszam = "X"
        # region tipushozzarendeles
        Tipusszam = epulet[i].Tipusszam_est.strip() if epulet[i].Tipusszam == '' else epulet[i].Tipusszam.strip()
        if Tipusszam == "L1":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 450
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L1/M":
            epulet[i].Tn_Tbr = 0.65
            epulet[i].E0 = 450
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 315
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L2":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 400
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L2/M":
            epulet[i].Tn_Tbr = 0.65
            epulet[i].E0 = 400
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 280
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L3":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 330
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L3/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 330
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L4":
            if "Szarvas" in epulet[i].Telepules:
                epulet[i].a = 1.2
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 220
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L4/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 220
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L5":
            if "Szarvas" in epulet[i].Telepules:
                epulet[i].a = 1.2
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L5/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L6":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 320
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L6/M":
            epulet[i].Tn_Tbr = 0.65
            epulet[i].E0 = 320
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 225
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L7":
            if "Szarvas" in epulet[i].Telepules:
                epulet[i].a = 1.3
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 120
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L8":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 340
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L8/M":
            epulet[i].Tn_Tbr = 0.65
            epulet[i].E0 = 340
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 240
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L9":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 300
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L10/A":
            epulet[i].Tn_Tbr = 0.65
            epulet[i].E0 = 240
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L10/B":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 240
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L11/A":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 240
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L11/B":
            epulet[i].Tn_Tbr = 0.85
            epulet[i].E0 = 240
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L12/A":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L12/B":
            epulet[i].Tn_Tbr = 0.85
            epulet[i].E0 = 170
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L12/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L13":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 210
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8
        elif Tipusszam == "L13/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 210
            epulet[i].Evil_est = 10
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 8

        elif Tipusszam == "K1":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 310
            epulet[i].Evil_est = 14.6
            epulet[i].Ee_cs_est = 150
            epulet[i].Evil_cs_est = 11.7
        elif Tipusszam == "K1/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 310
            epulet[i].Evil_est = 14.6
            epulet[i].Ee_cs_est = 200
            epulet[i].Evil_cs_est = 11.7
        elif Tipusszam == "K2":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 200
            epulet[i].Evil_est = 14.6
            epulet[i].Ee_cs_est = 110
            epulet[i].Evil_cs_est = 11.7
        elif Tipusszam == "K2/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 200
            epulet[i].Evil_est = 14.6
            epulet[i].Ee_cs_est = 110
            epulet[i].Evil_cs_est = 11.7   
        elif Tipusszam == "K3":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 250
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 110
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K3/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 250
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 160
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K4":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 80
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K4/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 80
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K5":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 150
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 80
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K5/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 150
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 80
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K6":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 260
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 100
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K6/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 260
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 160
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K7":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 230
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 150
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K7/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 230
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 150
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "K8":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 160
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 60
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K8/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 160
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 100
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K9":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 230
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 60
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K10":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 160
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 50
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K10/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 160
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 50
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K11":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 130
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 50
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K11/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 130
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 50
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K12":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 240
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 90
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K12/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 240
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 150
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K13":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 60
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K13/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 170
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 60
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K14":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 140
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 60
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "K14/F":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 140
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 60
            epulet[i].Evil_cs_est = 7.2

        elif Tipusszam == "I1A":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 460
            epulet[i].Evil_est = 17.5
            epulet[i].Ee_cs_est = 160
            epulet[i].Evil_cs_est = 14
        elif Tipusszam == "I1B":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 100
            epulet[i].Evil_est = 8.75
            epulet[i].Ee_cs_est = 100
            epulet[i].Evil_cs_est = 8.75
        elif Tipusszam == "I2A":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 350
            epulet[i].Evil_est = 17.5
            epulet[i].Ee_cs_est = 160
            epulet[i].Evil_cs_est = 14
        elif Tipusszam == "I2B":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 60
            epulet[i].Evil_est = 8.75
            epulet[i].Ee_cs_est = 60
            epulet[i].Evil_cs_est = 8.75
        elif Tipusszam == "I3A":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 210
            epulet[i].Evil_est = 25
            epulet[i].Ee_cs_est = 160
            epulet[i].Evil_cs_est = 20
        elif Tipusszam == "I3B":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 35
            epulet[i].Evil_est = 12.5
            epulet[i].Ee_cs_est = 35
            epulet[i].Evil_cs_est = 12.5
        
        elif Tipusszam == "E/I1":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 35
            epulet[i].Evil_est = 12.5
            epulet[i].Ee_cs_est = 35
            epulet[i].Evil_cs_est = 12.5
        elif Tipusszam == "E/I2":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 210
            epulet[i].Evil_est = 25
            epulet[i].Ee_cs_est = 160
            epulet[i].Evil_cs_est = 20
        elif Tipusszam == "E/I3":
            epulet[i].Tn_Tbr = 0.95
            epulet[i].E0 = 210
            epulet[i].Evil_est = 25
            epulet[i].Ee_cs_est = 160
            epulet[i].Evil_cs_est = 20
        elif Tipusszam == "E/K1":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 250
            epulet[i].Evil_est = 15.8
            epulet[i].Ee_cs_est = 100
            epulet[i].Evil_cs_est = 11.1
        elif Tipusszam == "E/K1/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 250
            epulet[i].Evil_est = 15.8
            epulet[i].Ee_cs_est = 100
            epulet[i].Evil_cs_est = 11.1
        elif Tipusszam == "E/K2/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 130
            epulet[i].Evil_est = 9
            epulet[i].Ee_cs_est = 100
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "E/K3":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 500
            epulet[i].Evil_est = 31.5
            epulet[i].Ee_cs_est = 110
            epulet[i].Evil_cs_est = 22
        elif Tipusszam == "E/K4":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 120
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 80
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "E/K5/M":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 120
            epulet[i].Evil_est = 7.2
            epulet[i].Ee_cs_est = 120
            epulet[i].Evil_cs_est = 7.2
        elif Tipusszam == "E/K6":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 330
            epulet[i].Evil_est = 31.5
            epulet[i].Ee_cs_est = 110
            epulet[i].Evil_cs_est = 22
        elif Tipusszam == "E/K7":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 150
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 100
            epulet[i].Evil_cs_est = 15.4
        elif Tipusszam == "E/K8":
            epulet[i].Tn_Tbr = 0.75
            epulet[i].E0 = 210
            epulet[i].Evil_est = 19.25
            epulet[i].Ee_cs_est = 150
            epulet[i].Evil_cs_est = 15.4
        else:
            epulet[i].Tn_Tbr = 0
            epulet[i].E0 = 0
            epulet[i].Evil_est = 0
            epulet[i].Ee_cs_est = 0
            epulet[i].Evil_cs_est = 0
        # endregion
        # x
        if epulet[i].Sz == '':
            epulet[i].Sz = 0.0
        epulet[i].Tbr = float(epulet[i].Sz) * float(epulet[i].te)
        if epulet[i].Tbr == '':
            epulet[i].Tbr = 0.0
        if epulet[i].Tn_Tbr == '':
            epulet[i].Tn_Tbr = 0.0
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
        # ez majd "p" "e" lesz a kataszteriben
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
        
        epulet[i].Ee_vil_cs = Ee_cs if Epulet_funkcio.strip() == 'Lakoepulet' else Ee_cs - Evil_cs
        epulet[i].Ee_vil = Ee if Epulet_funkcio.strip() == 'Lakoepulet' else Ee - Evil
        
        # alpha(n) validation check:
        if float(Ael + Aelcs + Aga + Aol + Asz + Abm + Ath) > 0.99:
            epulet[i].Szum_A = True
        else:
            epulet[i].Szum_A = False
        if float(Ael_cs + Aelcs_cs + Aga_cs + Aol_cs + Asz_cs + Abm_cs + Ath_cs) > 0.99:
            epulet[i].Szum_A_cs = True
        else:
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
        epulet[i].Qel_cs_real_est = float(epulet[i].Qel_csil) / float(epulet[i].eelcs) * k
        epulet[i].Qga_real_est = float(epulet[i].Qga) / float(epulet[i].ega) * k
        epulet[i].Qol_real_est = float(epulet[i].Qol) / float(epulet[i].eol) * k
        epulet[i].Qsz_real_est = float(epulet[i].Qsz) / float(epulet[i].esz) * k
        epulet[i].Qbm_real_est = float(epulet[i].Qbm) / float(epulet[i].ebm) * k
        epulet[i].Qth_real_est = float(epulet[i].Qth) / float(epulet[i].eth) * k
        # 17
        epulet[i].Qel_real_cs_est = float(epulet[i].Qel_cs) / float(epulet[i].eel) * k
        epulet[i].Qel_cs_real_cs_est = float(epulet[i].Qel_cs_cs) / float(epulet[i].eelcs) * k
        epulet[i].Qga_real_cs_est = float(epulet[i].Qga_cs) / float(epulet[i].ega) * k
        epulet[i].Qol_real_cs_est = float(epulet[i].Qol_cs) / float(epulet[i].eol) * k
        epulet[i].Qsz_real_cs_est = float(epulet[i].Qsz_cs) / float(epulet[i].esz) * k
        epulet[i].Qbm_real_cs_est = float(epulet[i].Qbm_cs) / float(epulet[i].ebm) * k
        epulet[i].Qth_real_cs_est = float(epulet[i].Qth_cs) / float(epulet[i].eth) * k    
        # it must be done in order to calculate De and De_cs correctly
        Qel_real = float(epulet[i].Qel_real_est) if epulet[i].Qel_real == '' else float(epulet[i].Qel_real)
        Qel_cs_real = float(epulet[i].Qel_cs_real_est) if epulet[i].Qel_cs_real == '' else float(epulet[i].Qel_cs_real)
        Qga_real = float(epulet[i].Qga_real_est) if epulet[i].Qga_real == '' else float(epulet[i].Qga_real)
        Qol_real = float(epulet[i].Qol_real_est) if epulet[i].Qol_real == '' else float(epulet[i].Qol_real)
        Qsz_real = float(epulet[i].Qsz_real_est) if epulet[i].Qsz_real == '' else float(epulet[i].Qsz_real)
        Qbm_real = float(epulet[i].Qbm_real_est) if epulet[i].Qbm_real == '' else float(epulet[i].Qbm_real)
        Qth_real = float(epulet[i].Qth_real_est) if epulet[i].Qth_real == '' else float(epulet[i].Qth_real)

        Qel_real_cs = float(epulet[i].Qel_real_cs_est) if epulet[i].Qel_real_cs == '' else float(epulet[i].Qel_real_cs)
        Qel_cs_real_cs = float(epulet[i].Qel_cs_real_cs_est) if epulet[i].Qel_cs_real_cs == '' else float(epulet[i].Qel_cs_real_cs)
        Qga_real_cs = float(epulet[i].Qga_real_cs_est) if epulet[i].Qga_real_cs == '' else float(epulet[i].Qga_real_cs)
        Qol_real_cs = float(epulet[i].Qol_real_cs_est) if epulet[i].Qol_real_cs == '' else float(epulet[i].Qol_real_cs)
        Qsz_real_cs = float(epulet[i].Qsz_real_cs_est) if epulet[i].Qsz_real_cs == '' else float(epulet[i].Qsz_real_cs)
        Qbm_real_cs = float(epulet[i].Qbm_real_cs_est) if epulet[i].Qbm_real_cs == '' else float(epulet[i].Qbm_real_cs)
        Qth_real_cs = float(epulet[i].Qth_real_cs_est) if epulet[i].Qth_real_cs == '' else float(epulet[i].Qth_real_cs)
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
