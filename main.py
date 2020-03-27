import epulet as Epulet
import telek as Telek
import tomb as Tomb
import telepules as Telepules
import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
read = csvhandler.Read()

epuletin = '/home/jeda/Work/innoregio/input/epulet.csv'
epuletout = '/home/jeda/Work/innoregio/output/epulet-out.csv'
# Epulet and Epulet-out csv calculatable data frame initialization.
inepulet = read.dataframe(epuletin)
epulet = [csvhandler.Dict(i, inepulet[0]) for i in inepulet[1:]]
inepuletout = read.dataframe(epuletout)
outepulet = [csvhandler.Dict(i, inepuletout[0]) for i in inepuletout[1:]]
# Epulet calling
Epulet.calculate(epulet)
epulethead = write.header(epulet)
Epulet.writer(epuletout, epulethead, epulet)

telekin = '/home/jeda/Work/innoregio/input/telek.csv'
telekout = '/home/jeda/Work/innoregio/output/telek-out.csv'
# Telek and Telek-out csv calculatable data frame initialization.
intelek = read.dataframe(telekin)
telek = [csvhandler.Dict(i, intelek[0]) for i in intelek[1:]]
intelekout = read.dataframe(telekout)
outtelek = [csvhandler.Dict(i, intelekout[0]) for i in intelekout[1:]]
# Telek calling
Telek.calculate(telek, outepulet)
telekhead = write.header(telek)
Telek.writer(telekout, telekhead, telek)

tombin = '/home/jeda/Work/innoregio/input/tomb.csv'
tombout = '/home/jeda/Work/innoregio/output/tomb-out.csv'
# Tomb and Tomb-out csv calculatable data frame initialization.
intomb = read.dataframe(tombin)
tomb = [csvhandler.Dict(i, intomb[0]) for i in intomb[1:]]
intombout = read.dataframe(tombout)
outtomb = [csvhandler.Dict(i, intombout[0]) for i in intombout[1:]]
# Tomb calling
Tomb.calculate(tomb, outtelek, outepulet)
tombhead = write.header(tomb)
Tomb.writer(tombout, tombhead, tomb)

telepulesin = '/home/jeda/Work/innoregio/input/telepules.csv'
telepulesout = '/home/jeda/Work/innoregio/output/telepules-out.csv'
# Telepules csv calculatable data frame initialization.
intelepules = read.dataframe(telepulesin)
telepules = [csvhandler.Dict(i, intelepules[0]) for i in intelepules[1:]]
# Tomb calling
Telepules.calculate(telepules, outtomb)
telepuleshead = write.header(telepules)
Telepules.writer(telepulesout, telepuleshead, telepules)