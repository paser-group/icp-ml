
import numpy as np 
import os 
import pandas as pd 
import time 
import datetime 
import statistics


def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime( '%Y-%m-%d %H:%M:%S' ) 
  return strToret

def Average(Mylist): 
    return sum(Mylist) / len(Mylist)
    
def Median(Mylist): 
    return statistics.median(Mylist)
    
def reportProp( res_file ):
    res_df = pd.read_csv(res_file) 
    fields2explore = ['CWE_61_COUNT', 'CWE_77_COUNT', 'CWE_78_COUNT', \
        'CWE_79_COUNT', 'CWE_89_COUNT', 'CWE_91_COUNT', 'CWE_220_COUNT', 'CWE_242_COUNT', 'CWE_259_COUNT', \
        'CWE_269_COUNT', 'CWE_285_COUNT', 'CWE_295_COUNT', 'CWE_319_COUNT', 'CWE_326_COUNT', 'CWE_338_COUNT', \
        'CWE_377_COUNT', 'CWE_477_COUNT', 'CWE_489_COUNT', 'CWE_601_COUNT', 'CWE_676_COUNT', \
        'CWE_755_COUNT', 'CWE_798_COUNT', 'TOTAL_EVENT_COUNT']
                     
    for field in fields2explore:
        field_res_list = res_df[res_df['CATEGORY'] == field ]   
        prop_val_list = field_res_list['PROP_VAL'].tolist() 
#         print(prop_val_list)
        average_prop_metric = Average(prop_val_list)        
        print('CATEGORY:{}, AVG_PROP_VAL:{}'.format( field, average_prop_metric  ))
        print('-'*50)     
        median_prop_metric = Median(prop_val_list)        
        print('CATEGORY:{}, MEDIAN_PROP_VAL:{}'.format( field, median_prop_metric  ))
        print('-'*50)          
    
    
def reportDensity( res_file ):
    res_df = pd.read_csv(res_file) 
    fields2explore = ['CWE_61_COUNT', 'CWE_77_COUNT', 'CWE_78_COUNT', \
        'CWE_79_COUNT', 'CWE_89_COUNT', 'CWE_91_COUNT', 'CWE_220_COUNT', 'CWE_242_COUNT', 'CWE_259_COUNT', \
        'CWE_269_COUNT', 'CWE_285_COUNT', 'CWE_295_COUNT', 'CWE_319_COUNT', 'CWE_326_COUNT', 'CWE_338_COUNT', \
        'CWE_377_COUNT', 'CWE_477_COUNT', 'CWE_489_COUNT', 'CWE_601_COUNT', 'CWE_676_COUNT', \
        'CWE_755_COUNT', 'CWE_798_COUNT', 'TOTAL_EVENT_COUNT']
                     
    for field in fields2explore:
        field_res_list = res_df[res_df['CATEGORY'] == field ]   
        density_val_list = field_res_list['EVENT_DENSITY'].tolist() 
        average_density_metric = Average(density_val_list)        
        print('CATEGORY:{}, AVG_DENSITY_VAL:{}'.format( field, average_density_metric  ))
        print('-'*50)     
        median_density_metric = Median(density_val_list) 
        max_density_metric = max(density_val_list) 
        min_density_metric = min(density_val_list) 
        print('CATEGORY:{}, MIN_DENSITY_VAL:{}'.format( field, min_density_metric  ))
        print('CATEGORY:{}, MAX_DENSITY_VAL:{}'.format( field, max_density_metric  ))       
        print('CATEGORY:{}, MEDIAN_DENSITY_VAL:{}'.format( field, median_density_metric  ))
        print('-'*50) 
        
            
if __name__=='__main__': 
    print('*'*100 )
    t1 = time.time()
    print('Started at:', giveTimeStamp() )
    print('*'*100 )
    
    print('*'*300) 
    print("Supervised GITHUB Proportion")
    RESULTS_FILE = 'output/PROPORTION_SUPERVISED_GITHUB.csv'
    reportProp( RESULTS_FILE )
    print('*'*50) 
    
    print('*'*50) 
    print("Supervised GITHUB Density")
    RESULTS_FILE = 'output/DENSITY_SUPERVISED_GITHUB.csv' 
    reportDensity( RESULTS_FILE )
    print('*'*100) 
 
#     print('*'*100) 
#     print("Supervised GITLAB Proportion")
#     RESULTS_FILE = 'output/PROPORTION_SUPERVISED_GITLAB.csv'
#     reportProp( RESULTS_FILE )
#     print('*'*50) 
#     
#     print('*'*50) 
#     print("Supervised GITLAB Density")
#     RESULTS_FILE = 'output/DENSITY_SUPERVISED_GITLAB.csv' 
#     reportDensity( RESULTS_FILE )
#     print('*'*100) 
    
#     print('*'*100) 
#     print("Supervised MODELZOO Proportion")
#     RESULTS_FILE = 'output/PROPORTION_SUPERVISED_MODELZOO.csv'
#     reportProp( RESULTS_FILE )
#     print('*'*50) 
#     
#     print('*'*50) 
#     print("Supervised MODELZOO Density")
#     RESULTS_FILE = 'output/DENSITY_SUPERVISED_MODELZOO.csv' 
#     reportDensity( RESULTS_FILE )
#     print('*'*300) 

#     print('*'*100) 
#     print("Non ML Proportion")
#     RESULTS_FILE = 'output/PROPORTION_NON_ML.csv'
#     reportProp( RESULTS_FILE )
#     print('*'*50) 
#     
#     print('*'*50) 
#     print("Non ML Density")
#     RESULTS_FILE = 'output/DENSITY_NON_ML.csv' 
#     reportDensity( RESULTS_FILE )
#     print('*'*100) 

    print('*'*100 )
    print('Ended at:', giveTimeStamp() )
    print('*'*100 )