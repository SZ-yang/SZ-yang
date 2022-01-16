import sys
import pandas as pd

inputfile1 = sys.argv[1]
inputfile2 = sys.argv[2]
outputfile1 = sys.argv[3]
outputfile2 = sys.argv[4]

#df: 2_members.tsv, 
#gene_df: DIAMOND_SRR8427257_filtered_output.tsv
df = pd.read_csv(inputfile1, sep = '\t', names = ["{}".format(i) for i in range(6)])
gene_df = pd.read_csv(inputfile2, sep="\t",\
    names =['qseqid', 'qlen', 'qstart', 'qend', 'sseqid', 'slen', 'sstart', 'send', 'evalue', 'length', 'pident'])

#generate COG dictionary
#COG_dic: {key=COG_id, value=[gene_id]}
#COG_specie_dic: {key=COG_id, value=number of species}
def COG_dics_Generator(df):
    COG_dic = {}
    COG_specie_dic ={}
    for row in range(df.shape[0]):
        specie_num = df.iloc[row, 3]
        gene_str = df.iloc[row, 4]
        gene_ls = gene_str.split(",")
        if len(gene_ls) == df.iloc[row, 2]:
            cog_name = df.iloc[row, 1]
            COG_dic[cog_name] = gene_ls
            COG_specie_dic[cog_name] = specie_num
    return COG_dic, COG_specie_dic

def total_num_specie_Generator(df):
    specie_ls=[]
    for row in range(df.shape[0]):
        specie_str = df.iloc[row, 5]
        cur_specie_ls = specie_str.split(",")
        specie_ls+=cur_specie_ls
    specie_set=set(specie_ls)
    total_num_specie=len(specie_set)
    return total_num_specie

total_num_specie = total_num_specie_Generator(df)
COG_dic, COG_specie_dic = COG_dics_Generator(df)

#COG_PI_dic: {key=COG_id, value=PI}
COG_PI_dic = {}
for Cog in COG_dic.keys():
    current_num_genes=COG_specie_dic[Cog]
    PI = format(current_num_genes /total_num_specie , '.8f')
    PI = float(PI)
    COG_PI_dic[Cog] = PI

#gene_COG_dic: 
gene_COG_dic = {}
for row in range(gene_df.shape[0]):
    gene_call_id = gene_df.iloc[row]['qseqid']
    anno_gene_id = gene_df.iloc[row]['sseqid']
    for og in COG_dic.keys():
        if anno_gene_id in COG_dic[og]:
            if gene_call_id in gene_COG_dic.keys():
                gene_COG_dic[gene_call_id].append(og)
            else:
                gene_COG_dic[gene_call_id]=[og]

#generate gene_COG_list df
outputdf1 = pd.DataFrame(columns=["gene_call_id", "COG_ls"])
i = 0
for gene_caller_id in gene_COG_dic.keys():
    COG_ls = gene_COG_dic[gene_caller_id]
    COG_str = ",".join(COG_ls)
    ls = [gene_caller_id, COG_str]
    outputdf1.loc[i] = ls
    i += 1
print("{}".format(total_num_specie))
outputdf1.to_csv(outputfile1, sep="\t", header=None, index=None)
print("gene_COG_list_convertation done")

#assign COG with the highest PI to the gene_calls
print("assign COG with the highest PI to the gene_calls begin")
highest_PI_df = pd.DataFrame(columns=["gene_call_id", "COG", "PI"])
n=0
for gci in gene_COG_dic.keys():
    COG_list = gene_COG_dic[gci]
    COG_highest_PI = ""
    highest_PI = -1
    for j in COG_list:
        cur_PI = COG_PI_dic[j]
        if cur_PI > highest_PI:
            highest_PI = cur_PI
            COG_highest_PI = j
    cur_ls = [gci, COG_highest_PI, highest_PI]
    highest_PI_df.loc[n] = cur_ls
    n += 1

highest_PI_df.to_csv(outputfile2, sep="\t", header=None, index=None)
print("OG with highest PI done")