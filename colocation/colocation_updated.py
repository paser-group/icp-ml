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
import time 
import datetime 
import csv

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime( '%Y-%m-%d %H:%M:%S' ) 
  return strToret
  
def index_2d(myList, item):
    for i, x in enumerate(myList):
        if item in x:
            return (i, x.index(item))

def calculateSmellProp(arm_df, file_count, smell_count_df, output_file):
    print('*'*25)
    df_list = list(csv.reader(open(output_file))) 
    
    for row in arm_df.itertuples():
        len_itemset = len(list( row[2]) ) 
        if len_itemset == 2:
            colocated_list = list(row[2])
            x_item = colocated_list[0]
            y_item = colocated_list[1]
            
            smell_df = smell_count_df[smell_count_df[0] == x_item]
            smell_count = smell_df.iloc[0][1]
            colocated_smell_count = row[1]   * file_count 
            smell_prop  = round(float(colocated_smell_count)/float(smell_count), 4) * 100 
            print('X:{}, X ^ Y:{}, SMELL_COUNT:{}, COLOCATE_SMELL_COUNT:{}, SMELL_PROP:{}'.format( x_item, list(row[2]) , smell_count, colocated_smell_count, smell_prop ) )
#             print(index_2d(df_list, colocated_list[0])[1]) # row number
#             print(index_2d(df_list, colocated_list[1])[1]) # col number
#             print(df_list[index_2d(df_list, colocated_list[1])[1]][index_2d(df_list, colocated_list[0])[1]]) # cell number
            df_list[index_2d(df_list, x_item)[1]][index_2d(df_list, y_item)[1]] = smell_prop
            print('*'*25)
            
            smell_df = smell_count_df[smell_count_df[0] == y_item]
            smell_count = smell_df.iloc[0][1]
            colocated_smell_count = row[1]   * file_count 
            smell_prop  = round(float(colocated_smell_count)/float(smell_count), 4) * 100 
            print('Y:{}, X ^ Y:{}, COLOCATE_SMELL_COUNT:{}, SMELL_COUNT:{}, SMELL_PROP:{}'.format( y_item, list(row[2]) , colocated_smell_count, smell_count, smell_prop ) )
            df_list[index_2d(df_list, y_item)[1]][index_2d(df_list, x_item)[1]] = smell_prop
            print('*'*25)
            
                
    for row_index, row in enumerate(df_list):
        for col_index, item in enumerate(row):
            if not df_list[row_index][col_index]:
                df_list[row_index][col_index] = 'X'  
                
  
    df = pd.DataFrame( df_list ) 
    df.to_csv(output_file, header=None, index=False)  
    print('*'*25)  


        
def doColocation(arm_list_of_list, tx_cnt, smell_cnt_df, output_file):
    te = TransactionEncoder()
    te_ary = te.fit(arm_list_of_list).transform(arm_list_of_list)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=0.0001, use_colnames=True)   ## do not change: min_support=0.0001 
    calculateSmellProp(frequent_itemsets, tx_cnt, smell_cnt_df, output_file) 



def findColocation(input_file, output_file):
    arm_list = []
    file_df = pd.read_csv(input_file) 
    file_names = np.unique( file_df['FILEPATH'].tolist() )
    smell_names = np.unique( file_df['TYPE'].tolist() )
    file_count = len(file_names) 
    
    smell_count_list = []
    for smell_name in smell_names:
         smell_df = file_df[file_df['TYPE']==smell_name]
         smell_count = len(smell_df) 
         the_tup = ( smell_name, smell_count)
         smell_count_list.append( the_tup )
        
    smell_count_df = pd.DataFrame( smell_count_list ) 
    
    for file_name in file_names:
        per_file_df = file_df[file_df['FILEPATH']==file_name]
        icp_list    = per_file_df['TYPE'].tolist()
        arm_list.append(icp_list) 
        
        
    print('~'*100)         
    print('~'*100)         
    doColocation( arm_list , file_count, smell_count_df, output_file) 



if __name__=='__main__': 
    print('*'*100 )
    t1 = time.time()
    print('Started at:', giveTimeStamp() )
    print('*'*100 )


    input_file_modelzoo = 'output/COLOCATION_MODELZOO_INPUT.csv'
    input_file_gitlab = 'output/COLOCATION_GITLAB_INPUT.csv'
    input_file_github = 'output/COLOCATION_GITHUB_INPUT.csv'
    
    output_file_modelzoo = 'output/COLOCATION_MODELZOO_OUTPUT.csv'
    output_file_gitlab = 'output/COLOCATION_GITLAB_OUTPUT.csv'
    output_file_github = 'output/COLOCATION_GITHUB_OUTPUT.csv'
    
    print('~'*100) 
    print("----------------MODELZOO--------------------")
    findColocation(input_file_modelzoo, output_file_modelzoo)
    
    print('~'*100) 
    print("----------------GITLAB--------------------")
    findColocation(input_file_gitlab, output_file_gitlab)
    
    print('~'*100) 
    print("----------------GITHUB--------------------")
    findColocation(input_file_github, output_file_github)

