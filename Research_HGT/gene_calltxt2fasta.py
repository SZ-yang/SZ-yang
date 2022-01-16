import sys
import pandas as pd

inputfile= sys.argv[1]
outputfile = sys.argv[2]


df = pd.read_csv(inputfile, sep = "\t", names = ["gene_call_id", "seq"])
real_df = df

def splice(seq):
    i = 0
    ls = []
    while i < len(seq)+1:
        if len(seq)-i > 60:
            ls.append(seq[i:i+60])
            i += 60
        else:
            ls.append(seq[i:len(seq)+1])
            i += 60
    return ls 

fa_file = open(outputfile, "w")
for j in range(real_df.shape[0]):
    gene_name = str(real_df.iloc[j]["gene_call_id"])
    seq = real_df.iloc[j]["seq"]
    ls_seq = splice(seq)
    fa_file.write(">"+gene_name+'\n')
    for aa in ls_seq:
        fa_file.write(aa+"\n")
fa_file.close()
