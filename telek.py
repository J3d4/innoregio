import csvhandler

read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/telek.csv')
ins = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]

def calculations():
    for i in range(len(ins)):
       ins[i].Ee

if __name__ == '__main__':
    calculations()
    write = csvhandler.Write()
    out = '/home/jeda/Work/innoregio/output/telek-out.csv'
    head = write.header(ins)
    write.writer(out, head, ins)