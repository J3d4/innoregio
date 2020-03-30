import csvhandler
from tqdm import tqdm

write = csvhandler.Write()
# only for debugging purposes, use main.py to run the program.
read = csvhandler.Read()
inp = read.dataframe('/home/jeda/work/innoregio/input/telepules.csv')
telepules = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]
inptomb = read.dataframe('/home/jeda/work/innoregio/input/tomb.csv')
tomb = [csvhandler.Dict(i, inptomb[0]) for i in inptomb[1:]]
##############################################################

def calculate(telepules, tomb):
    print("Calculate Telepules:")
    for i in tqdm(range(len(telepules))):
        telepules[i].Telepules
        # please insert calculations here:

    print("Telepules done.")
    return telepules

def writer(output, head, data):
    print("Writing Telepules-out")
    write.writer(output, head, data)
    print("Done.")  

# for debugging purposes:
if __name__ == '__main__':
    calculate(telepules, tomb)
    print(" ")