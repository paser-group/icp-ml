
import time
import datetime
import pandas as pd
import numpy as np


def giveTimeStamp():
    tsObj = time.time()
    strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
    return strToret



def colocation_data(input_csv, colocation_input):
    file_df = pd.read_csv(input_csv) 
    
    colocate_data = [] 
    
    file_names = np.unique( file_df['FILE_FULL_PATH'].tolist() )
    
    for file_name in file_names:
        file_entity = file_df[file_df['FILE_FULL_PATH'] == file_name ]                         
    
        fields2explore =  ['CWE_61_COUNT', 'CWE_77_COUNT', 'CWE_78_COUNT', \
        'CWE_79_COUNT', 'CWE_89_COUNT', 'CWE_91_COUNT', 'CWE_220_COUNT', 'CWE_242_COUNT', 'CWE_259_COUNT', \
        'CWE_269_COUNT', 'CWE_285_COUNT', 'CWE_295_COUNT', 'CWE_319_COUNT', 'CWE_326_COUNT', 'CWE_338_COUNT', \
        'CWE_377_COUNT', 'CWE_477_COUNT', 'CWE_489_COUNT', 'CWE_601_COUNT', 'CWE_676_COUNT', \
        'CWE_755_COUNT', 'CWE_798_COUNT']
    
        for field in fields2explore:
            field_type  = file_entity[field]
            if field_type.iloc[0] > 0:
                the_tup = ( file_name, field )
                colocate_data.append( the_tup )
    
    
    colocate_df = pd.DataFrame(colocate_data) 
    CSV_HEADER = ['FILEPATH','TYPE']
    colocate_df.to_csv(colocation_input, header= CSV_HEADER, index=False, encoding= 'utf-8')  


if __name__=='__main__':

	t1 = time.time()
	print('Started at:', giveTimeStamp() )
	print('*'*100 )
	
	print("----------------MODELZOO--------------------")
	input_csv = 'output/SUPERVISED_OUTPUT_MODELZOO.csv'
	colocation_input = 'output/COLOCATION_MODELZOO_INPUT.csv'
	colocation_data(input_csv, colocation_input)
	
	print("----------------GITLAB--------------------")
	input_csv = 'output/SUPERVISED_OUTPUT_GITLAB.csv'
	colocation_input = 'output/COLOCATION_GITLAB_INPUT.csv'
	colocation_data(input_csv, colocation_input)
	
	print("----------------GITHUB--------------------")
	input_csv = 'output/SUPERVISED_OUTPUT_GITHUB.csv'
	colocation_input = 'output/COLOCATION_GITHUB_INPUT.csv'
	colocation_data(input_csv, colocation_input)

	print('*'*100 )
	print('Ended at:', giveTimeStamp() )
	print('*'*100 )
	
	t2 = time.time()
	time_diff = round( (t2 - t1 ) / 60, 5) 
	print('Duration: {} minutes'.format(time_diff) )
	print('*'*100 )
