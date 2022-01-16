import sys
import pandas as pd


inputfile1 = sys.argv[1]
inputfile2 = sys.argv[2]
inputfile3 = sys.argv[3]
outputfile = sys.argv[4]


OG_PI_df = pd.read_csv(inputfile1, sep="\t", names=["gene_callers_id", "OG", "PI"])
genecalls_df = pd.read_csv(inputfile2, sep="\t", \
    names=["gene_callers_id", "contig", "start", "stop", "direction", "partial", "call_type", "source", "version", "aa_sequence"])
counts_df = pd.read_csv(inputfile3, sep="\t", names=[ "contig", "start", "stop", "counts"])


def gene_OG_PI_generator(df):
    dic = {}
    for row in range(df.shape[0]):
        OG_PI_ls=[df.iloc[row]["OG"],df.iloc[row]["PI"]]
        gene_call_id = df.iloc[row]["gene_callers_id"]
        dic[gene_call_id]=OG_PI_ls
    return dic

gene_OG_PI_dic=gene_OG_PI_generator(OG_PI_df)
total_gene_df = pd.DataFrame(columns=["gene_callers_id", "contig", "OG", "PI", "start", "stop","length", "counts", "direction"])


i = 0
for row in range(genecalls_df.shape[0]):
    gene_call_id = genecalls_df.iloc[row]["gene_callers_id"]
    gene_contig = genecalls_df.iloc[row]["contig"]
    gene_start = genecalls_df.iloc[row]["start"]
    gene_stop = genecalls_df.iloc[row]["stop"]
    gene_len = gene_stop - gene_start
    direct = genecalls_df.iloc[row]["direction"]
    counts = counts_df.iloc[row]["counts"]
    #PI!=0
    if gene_call_id in gene_OG_PI_dic.keys():
        OG_id= gene_OG_PI_dic[gene_call_id][0]
        PI_val = gene_OG_PI_dic[gene_call_id][1]
    #PI=0
    else:
        OG_id, PI_val = 'NA', 0
    
    
    ls = [gene_call_id, gene_contig, OG_id, PI_val, gene_start, gene_stop, gene_len, counts, direct]
    total_gene_df.loc[i] = ls
    i+=1




total_gene_df.to_csv(outputfile, sep="\t", header=None, index=None)

print("total_genecall_PI.py combines the information of gene_calls")
print("Author: Shizhao Yang sy2821 Date: Dec/25/2021")
print("")
print("-------------------------------------------------------------")
print("input file1: annotated gene_calls with related OG and PI ")
print(inputfile1)
print("number of annotated gene_calls(PI!=0): {}".format(OG_PI_df.shape))

print("input file2: total gene_calls with related info")
print(inputfile2)
print("number of all gene_calls: {}".format(genecalls_df.shape))

print("input file3: gene_calls counts")
print(inputfile3)
print("number of all gene_calls with counts: {}".format(counts_df.shape))
print("-------------------------------------------------------------")
if total_gene_df.shape[0]==genecalls_df.shape[0]:
    print("job done !")
    print(outputfile)
    print("")
else:
    print("job failed")
