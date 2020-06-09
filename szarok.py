        # d(n) est or not est validation check
        d_el = float(epulet[i].delest) if epulet[i].d_el == 0 else float(epulet[i].d_el)
        delcs = float(epulet[i].delcsest) if epulet[i].delcs == 0 else float(epulet[i].delcs)
        dga = float(epulet[i].dgaest) if epulet[i].dga == 0 else float(epulet[i].dga)
        dol = float(epulet[i].dolest) if epulet[i].dol == 0 else float(epulet[i].dol)
        dsz = float(epulet[i].dszest) if epulet[i].dsz == 0 else float(epulet[i].dsz)
        dbm = float(epulet[i].dbmest) if epulet[i].dbm == 0 else float(epulet[i].dbm)
        dth = float(epulet[i].dthest) if epulet[i].dth == 0 else float(epulet[i].dth)

        if Epulet_funkcio == 'Lakoepulet':
            # 1
            if epulet[i].d_el == '':
                epulet[i].delest = d_el_lak
            else:
                epulet[i].d_el = d_el_lak
            if epulet[i].delcs == '':
                epulet[i].delcsest = delcs_lak
            else:
                epulet[i].delcs = delcs_lak
            if epulet[i].dga == '':
                epulet[i].dgaest = dga_lak
            else:
                epulet[i].dga = dga_lak
            if epulet[i].dol == '':
                epulet[i].dolest = dol_lak
            else:
                epulet[i].dol = dol_lak
            if epulet[i].dsz == '':
                epulet[i].dszest = dsz_lak
            else:
                epulet[i].dsz = dsz_lak
            if epulet[i].dbm == '':
                epulet[i].dbmest = dbm_lak
            else:
                epulet[i].dbm = dbm_lak
            if epulet[i].dth == '':
                epulet[i].dthest = dth_lak
            else:
                epulet[i].dth = dth_lak
        else:
            # 1
            epulet[i].d_el = 0
            epulet[i].delest = 0
            epulet[i].delcs = 0
            epulet[i].delcsest = 0
            epulet[i].dga = 0
            epulet[i].dgaest = 0
            epulet[i].dol = 0
            epulet[i].dolest = 0
            epulet[i].dsz = 0
            epulet[i].dszest = 0
            epulet[i].dbm = 0
            epulet[i].dbmest = 0
            epulet[i].dth = 0
            epulet[i].dthest = 0
            # nem tudom ez kell e a tomb TTTTT szamitasahoz:
            if float(telek[i].adat_t) == 1.0:

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
