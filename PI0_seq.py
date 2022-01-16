import sys
import pandas as pd

inputfile1 = sys.argv[1] #gene_calls_seq.txt
inputfile2 = sys.argv[2] #total_genecall_OG_PI.tsv
outputfile = sys.argv[3] #gene_calls_noOG_seq.txt

gene_seq_df = pd.read_csv(inputfile1, sep="\t", names = ["gene_call_id", "seq"])
total_gene_df = pd.read_csv(inputfile2, sep="\t", names=["gene_callers_id", "contig", "OG", "PI", "start", "stop","length", "counts", "direction"])

def gene_seq_dic_generator(df):
    dic = {}
    for row in range(df.shape[0]):
        gene = df.iloc[row]["gene_call_id"]
        seq = df.iloc[row]["seq"]
        dic[gene] = seq
    return dic


gene_seq_dic = gene_seq_dic_generator(gene_seq_df)
PI0_seq_df = pd.DataFrame(columns=["gene_call_id", "seq"])
i = 0
for row in range(total_gene_df.shape[0]):
    PI = total_gene_df.iloc[row]["PI"]
    gci = total_gene_df.iloc[row]["gene_callers_id"]
    if PI == 0:
        ls = [gci,gene_seq_dic[gci]]
        PI0_seq_df.loc[i]= ls
        i += 1

PI0_seq_df.to_csv(outputfile, sep="\t", header=None, index=None)
print("PI0_seq.py select the genecalls of PI=0 (no OG group) and related sequences")
print("Author: Shizhao Yang sy2821 Date: Dec/27/2021")
print("")
print("-------------------------------------------------------------")
print("inputfile1: {}".format(inputfile1))
print("inputfile2: {}".format(inputfile2))
print("")
print("-------------------------------------------------------------")
print("outputfile: {}".format(outputfile))
print("number of genecalls without OG: {}".format(PI0_seq_df.shape[0]))
print("")
print("job done!")