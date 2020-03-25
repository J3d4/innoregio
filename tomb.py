import csvhandler
import time
from tqdm import tqdm

read = csvhandler.Read()
inp = read.dataframe('/home/jeda/Work/innoregio/input/tomb.csv')
ins = [csvhandler.Dict(i, inp[0]) for i in inp[1:]]

def calculations():
    print("Calculate Tomb:")
    for i in tqdm(range(len(ins))):
        time.sleep(0.0000000001)
    
    print("Tomb done.")

# for debugging purposes:
if __name__ == '__main__':
    calculations()
    print(" ")