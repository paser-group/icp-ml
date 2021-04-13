
import numpy as np 
import os 
import pandas as pd 
import time 
import datetime 

def giveTimeStamp():
  tsObj = time.time()
  strToret = datetime.datetime.fromtimestamp(tsObj).strftime( '%Y-%m-%d %H:%M:%S' ) 
  return strToret


def getAllSLOC(df_param, csv_encoding='latin-1' ):
    total_sloc = 0
    all_files = np.unique( df_param['FILE_FULL_PATH'].tolist() ) 
    for file_ in all_files:
        total_sloc = total_sloc + sum(1 for line in open(file_, encoding=csv_encoding))
    return total_sloc

def reportProportion( res_file, output_file ):
    res_df = pd.read_csv( res_file )
    repo_names   = np.unique( res_df['REPO_FULL_PATH'].tolist() )
    
    fields2explore = ['CWE_61_COUNT', 'CWE_77_COUNT', 'CWE_78_COUNT', \
        'CWE_79_COUNT', 'CWE_89_COUNT', 'CWE_91_COUNT', 'CWE_220_COUNT', 'CWE_242_COUNT', 'CWE_259_COUNT', \
        'CWE_269_COUNT', 'CWE_285_COUNT', 'CWE_295_COUNT', 'CWE_319_COUNT', 'CWE_326_COUNT', 'CWE_338_COUNT', \
        'CWE_377_COUNT', 'CWE_477_COUNT', 'CWE_489_COUNT', 'CWE_601_COUNT', 'CWE_617_COUNT', 'CWE_676_COUNT', \
        'CWE_733_COUNT', 'CWE_755_COUNT', 'CWE_798_COUNT', 'TOTAL_EVENT_COUNT']
	
	
    
    df_list = [] 
    
    for repo in repo_names:
        print('-'*50) 
        print(repo)
        repo_entity = res_df[res_df['REPO_FULL_PATH'] == repo ]           
        all_py_files   = np.unique( repo_entity['FILE_FULL_PATH'].tolist() )
        for field in fields2explore:
            field_atleast_one_df = repo_entity[repo_entity[field] > 0 ]
            atleast_one_files    = np.unique( field_atleast_one_df['FILE_FULL_PATH'].tolist() )
            prop_metric          = round(float(len( atleast_one_files ) )/float(len(all_py_files)) , 5) * 100
            print('TOTAL_FILES:{}, CATEGORY:{}, ATLEASTONE:{}, PROP_VAL:{}'.format( len(all_py_files), field, len(atleast_one_files) , prop_metric  ))
            print('-'*50) 
            
            the_tup = ( repo, len(all_py_files), field, len(atleast_one_files), prop_metric )
            df_list.append( the_tup )
            
    CSV_HEADER = ['REPO_NAME', 'TOTAL_FILES', 'CATEGORY', 'ATLEASTONE', 'PROP_VAL']
    full_df = pd.DataFrame( df_list ) 
    full_df.to_csv(output_file, header= CSV_HEADER, index=False, encoding= 'utf-8') 


def reportEventDensity(res_file, output_file): 
    res_df = pd.read_csv(res_file) 
    repo_names   = np.unique( res_df['REPO_FULL_PATH'].tolist() )
    fields2explore =  ['CWE_61_COUNT', 'CWE_77_COUNT', 'CWE_78_COUNT', \
        'CWE_79_COUNT', 'CWE_89_COUNT', 'CWE_91_COUNT', 'CWE_220_COUNT', 'CWE_242_COUNT', 'CWE_259_COUNT', \
        'CWE_269_COUNT', 'CWE_285_COUNT', 'CWE_295_COUNT', 'CWE_319_COUNT', 'CWE_326_COUNT', 'CWE_338_COUNT', \
        'CWE_377_COUNT', 'CWE_477_COUNT', 'CWE_489_COUNT', 'CWE_601_COUNT', 'CWE_617_COUNT', 'CWE_676_COUNT', \
        'CWE_733_COUNT', 'CWE_755_COUNT', 'CWE_798_COUNT', 'TOTAL_EVENT_COUNT']
  
    df_list = [] 
    
    for repo in repo_names:
        print('-'*50) 
        print(repo)
        repo_entity = res_df[res_df['REPO_FULL_PATH'] == repo ]                         
        all_py_files   = np.unique( repo_entity['FILE_FULL_PATH'].tolist() )  
        all_py_size    = getAllSLOC(repo_entity) 
  
  
        for field in fields2explore:
            field_res_list  = repo_entity[field].tolist() 
            field_res_count = sum( field_res_list ) 
            event_density   = round( float(field_res_count * 1000 ) / float(all_py_size)  , 5) 
            print('TOTAL_LOC:{}, CATEGORY:{}, TOTAL_EVENT_COUNT:{}, EVENT_DENSITY:{}'.format( all_py_size, field, field_res_count, event_density )  )
            print('-'*25)
            
            the_tup = ( repo, all_py_size, field, field_res_count, event_density )
            df_list.append( the_tup )
            
    CSV_HEADER = ['REPO_NAME', 'TOTAL_LOC', 'CATEGORY', 'TOTAL_EVENT_COUNT', 'EVENT_DENSITY']
    full_df = pd.DataFrame( df_list ) 
    full_df.to_csv(output_file, header= CSV_HEADER, index=False, encoding= 'utf-8') 

if __name__=='__main__': 
    print('*'*100 )
    t1 = time.time()
    print('Started at:', giveTimeStamp() )
    print('*'*100 )


#     RESULTS_FILE = 'SUPERVISED_OUTPUT_GITHUB.csv'
#     PROPORTION_FILE = 'PROPORTION_SUPERVISED_GITHUB.csv'   
#     DENSITY_FILE = 'DENSITY_SUPERVISED_GITHUB.csv' 
#     
#     reportProportion( RESULTS_FILE, PROPORTION_FILE )
#     print('*'*100) 
#     reportEventDensity( RESULTS_FILE, DENSITY_FILE )
#     print('*'*100) 
#     
#     RESULTS_FILE = 'SUPERVISED_OUTPUT_GITLAB.csv'
#     PROPORTION_FILE = 'PROPORTION_SUPERVISED_GITLAB.csv'   
#     DENSITY_FILE = 'DENSITY_SUPERVISED_GITLAB.csv' 
#     
#     reportProportion( RESULTS_FILE, PROPORTION_FILE )
#     print('*'*100) 
#     reportEventDensity( RESULTS_FILE, DENSITY_FILE )
#     print('*'*100) 
    
    RESULTS_FILE = 'output/SUPERVISED_OUTPUT_MODELZOO.csv'
    PROPORTION_FILE = 'output/PROPORTION_SUPERVISED_MODELZOO.csv'   
    DENSITY_FILE = 'output/DENSITY_SUPERVISED_MODELZOO.csv' 
    
    reportProportion( RESULTS_FILE, PROPORTION_FILE )
    print('*'*100) 
    reportEventDensity( RESULTS_FILE, DENSITY_FILE )
    print('*'*100)   
    
    print('*'*100 )
    print('Ended at:', giveTimeStamp() )
    print('*'*100 )
