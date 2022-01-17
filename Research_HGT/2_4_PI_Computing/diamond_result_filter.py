import sys
import pandas as pd

inputfile= sys.argv[1]
outputfile = sys.argv[2]

df = pd.read_csv(inputfile, sep = "\t", \
    names =['qseqid', 'qlen', 'qstart', 'qend', 'sseqid', 'slen', 'sstart', 'send', 'evalue', 'length', 'pident'])

filtered_df = pd.DataFrame(columns=['qseqid', 'qlen', 'qstart', 'qend', 'sseqid', 'slen', 'sstart', 'send', 'evalue', 'length', 'pident'])

gene_name = df.iloc[0]['qseqid']
i = 1
filtered_df.loc[0] = df.loc[0]
for row in range(df.shape[0]):
    current_name = df.iloc[row]['qseqid']
    if current_name != gene_name:
        filtered_df.loc[i] = df.loc[row]
        gene_name = current_name
        i+=1 

def list_gen(df, col_name):
    rows = df.shape[0] 
    target_col = col_name
    ls = []
    for i in range(rows):
        temp = df[target_col][i]
        if temp not in ls:
            ls.append(temp)
    return ls

gene_ls = list_gen(df, 'qseqid')
if len(gene_ls)==filtered_df.shape[0]:
    print("filtering {} ".format(inputfile))
    print("number of annotated gene: {}".format(len(gene_ls)))
    filtered_df.to_csv(outputfile, sep = "\t", header = None, index= None)
    print("diamond_result_filtering done!")