import csvhandler
import epulet
import telek
import tomb
import telepules

epulet.calculations()
telek.calculations()
tomb.calculations()
telepules.calculations()

write = csvhandler.Write()

epuletout = '/home/jeda/Work/innoregio/output/epulet-out.csv'
telekout = '/home/jeda/Work/innoregio/output/telek-out.csv'
tombout = '/home/jeda/Work/innoregio/output/tomb-out.csv'
telepulesout = '/home/jeda/Work/innoregio/output/telepules-out.csv'
    
epulethead = write.header(epulet.ins)
telekhead = write.header(telek.ins)
tombhead = write.header(tomb.ins)
telepuleshead = write.header(telepules.ins)

print("Writing...")
print("Epulet-out")
write.writer(epuletout, epulethead, epulet.ins)
print("Done.")
print("Telek-out")
write.writer(telekout, telekhead, telek.ins)
print("Done.")
print("Tomb-out")
write.writer(tombout, tombhead, tomb.ins)
print("Done.")
print("Telepules-out")
write.writer(telepulesout, telepuleshead, telepules.ins)
print("Done.")