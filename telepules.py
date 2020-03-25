import csvhandler
import time
from tqdm import tqdm

read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/telepules.csv')
ins = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]

def calculations():
    print("Calculate Telepules:")
    for i in tqdm(range(len(ins))):
        time.sleep(0.0000000001)

    print("Telepules done.")

# for debugging purposes:
if __name__ == '__main__':
    calculations()
    print(" ")