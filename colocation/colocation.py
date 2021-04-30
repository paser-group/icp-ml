'''
Find out which categories colocate and their frequency 
'''
# reff: http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/association_rules/
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import numpy as np 
from collections import Counter           


def multiColocationARM(arm_df, file_count, tot_smell_count):
    print('*'*25)
    print('File analysis ... ')
    print('*'*25)
    for row in arm_df.itertuples():
        len_itemset = len(list( row[2]) ) 
        if len_itemset > 1:
            print('TYPE:{}, PERC:{}'.format( list(row[2]) , round( row[1]  , 5) * 100 ) )
            print('*'*25)
    dict_itemsets = dict( arm_df.to_dict() ) 
    # print(dict_itemsets) 
    support_dict = dict_itemsets['support']
    itemset_dict = dict_itemsets['itemsets']    
    identifiers  = support_dict.keys()
    len_items_dict, colocation_dict, file_dict  = {}, {}, {}
    for ID in identifiers:
        support_val = support_dict[ID]
        itemset_val = itemset_dict[ID]
        itemset_len = len(itemset_val) 
        # support count for security smell
        if itemset_len > 1:
            if itemset_len not in len_items_dict:
                len_items_dict[itemset_len] = [support_val] 
                colocation_dict[itemset_len] = [itemset_val]
            else: 
                len_items_dict[itemset_len] = len_items_dict[itemset_len]   +  [support_val]        
                colocation_dict[itemset_len] = colocation_dict[itemset_len] + [itemset_val] 
        # support count for files 
    print('*'*25)
    print('Smell  analysis ... ')
    for row in arm_df.itertuples():
        len_itemset = len(list( row[2]) ) 
        if len_itemset > 1:
            smell_count = row[1]   * file_count 
            smell_prop  = round(float(smell_count)/float(tot_smell_count), 5) * 100 
            print('TYPE:{}, SMELL_COUNT:{}, SMELL_PROP:{}'.format( list(row[2]) , smell_count, smell_prop ) )
            print('*'*25)
    print('*'*25)    

    return len_items_dict, colocation_dict 


        
def doColocation(arm_list_of_list, tx_cnt, smell_cnt):
    te = TransactionEncoder()
    te_ary = te.fit(arm_list_of_list).transform(arm_list_of_list)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=0.0001, use_colnames=True)   ## do not change: min_support=0.0001 
    multiColocationARM(frequent_itemsets, tx_cnt, smell_cnt) 



def findColocation(file_name):
    arm_list = []
    file_df = pd.read_csv(file_name) 
    file_names = np.unique( file_df['FILEPATH'].tolist() )
    file_count = len(file_names) 
    smell_count = len(file_df['TYPE'].tolist()) 
    
    for file_name in file_names:
        per_file_df = file_df[file_df['FILEPATH']==file_name]
        icp_list    = per_file_df['TYPE'].tolist()
        arm_list.append(icp_list) 
    print('~'*100)         
    print('~'*100)         
    doColocation( arm_list , file_count, smell_count  ) 


if __name__=='__main__':

    dataset_file_modelzoo = 'output/COLOCATION_MODELZOO_INPUT.csv'
    dataset_file_gitlab = 'output/COLOCATION_GITLAB_INPUT.csv'
    dataset_file_github = 'output/COLOCATION_GITHUB_INPUT.csv'
    
    
    print('~'*100) 
    print("----------------MODELZOO--------------------")
    findColocation(dataset_file_modelzoo)
    
    print('~'*100) 
    print("----------------GITLAB--------------------")
    findColocation(dataset_file_gitlab)
    
    print('~'*100) 
    print("----------------GITHUB--------------------")
    findColocation(dataset_file_github)

