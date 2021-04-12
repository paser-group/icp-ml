import numpy as np
import os
import time
import datetime
import issue_engine
import pandas as pd


def giveTimeStamp():
    tsObj = time.time()
    strToret = datetime.datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
    return strToret


def getCSVData(file_list, bandit_output):
    temp_list = []
    for PYTHON_SCRIPT in file_list:
    
        CWE_617_COUNT, CWE_733_COUNT, CWE_78_COUNT, CWE_269_COUNT, \
	    CWE_285_COUNT, CWE_798_COUNT, CWE_259_COUNT, CWE_377_COUNT, CWE_755_COUNT, CWE_489_COUNT, \
	    CWE_676_COUNT, CWE_326_COUNT, CWE_242_COUNT, CWE_601_COUNT, CWE_338_COUNT, CWE_91_COUNT, \
	    CWE_295_COUNT, CWE_77_COUNT, CWE_79_COUNT = issue_engine.getAllIssueCount(bandit_output, PYTHON_SCRIPT)
	
        total_event_count = CWE_617_COUNT + CWE_733_COUNT + CWE_78_COUNT + CWE_269_COUNT + CWE_285_COUNT \
        + CWE_798_COUNT + CWE_259_COUNT + CWE_377_COUNT + CWE_755_COUNT + CWE_489_COUNT + CWE_676_COUNT \
        + CWE_326_COUNT + CWE_242_COUNT + CWE_601_COUNT + CWE_338_COUNT + CWE_91_COUNT + CWE_295_COUNT \
        + CWE_77_COUNT + CWE_79_COUNT

        if 'MODELZOO' in PYTHON_SCRIPT:
            dir_repo = PYTHON_SCRIPT.split('/')[0] + PYTHON_SCRIPT.split('/')[1] + PYTHON_SCRIPT.split('/')[2] + PYTHON_SCRIPT.split('/')[3]
        else:
            dir_repo = PYTHON_SCRIPT.split('/')[0] + PYTHON_SCRIPT.split('/')[1] + PYTHON_SCRIPT.split('/')[2]
		
        the_tup = ( dir_repo, PYTHON_SCRIPT, CWE_617_COUNT, CWE_733_COUNT, CWE_78_COUNT, CWE_269_COUNT, \
		CWE_285_COUNT, CWE_798_COUNT, CWE_259_COUNT, CWE_377_COUNT, CWE_755_COUNT, CWE_489_COUNT, \
		CWE_676_COUNT, CWE_326_COUNT, CWE_242_COUNT, CWE_601_COUNT, CWE_338_COUNT, CWE_91_COUNT, \
		CWE_295_COUNT, CWE_77_COUNT, CWE_79_COUNT, total_event_count )

        temp_list.append( the_tup )
    return temp_list  
    
    
def getNoIssueCSVData(file_list):
    temp_list = []
    for PYTHON_SCRIPT in file_list:
    
        CWE_617_COUNT = CWE_733_COUNT = CWE_78_COUNT = CWE_269_COUNT = \
	    CWE_285_COUNT = CWE_798_COUNT = CWE_259_COUNT = CWE_377_COUNT = CWE_755_COUNT = CWE_489_COUNT = \
	    CWE_676_COUNT = CWE_326_COUNT = CWE_242_COUNT = CWE_601_COUNT = CWE_338_COUNT = CWE_91_COUNT = \
	    CWE_295_COUNT = CWE_77_COUNT = CWE_79_COUNT = 0
	
        total_event_count = 0

        if 'MODELZOO' in PYTHON_SCRIPT:
            dir_repo = PYTHON_SCRIPT.split('/')[0] + PYTHON_SCRIPT.split('/')[1] + PYTHON_SCRIPT.split('/')[2] + PYTHON_SCRIPT.split('/')[3]
        else:
            dir_repo = PYTHON_SCRIPT.split('/')[0] + PYTHON_SCRIPT.split('/')[1] + PYTHON_SCRIPT.split('/')[2]
		
        the_tup = ( dir_repo, PYTHON_SCRIPT, CWE_617_COUNT, CWE_733_COUNT, CWE_78_COUNT, CWE_269_COUNT, \
		CWE_285_COUNT, CWE_798_COUNT, CWE_259_COUNT, CWE_377_COUNT, CWE_755_COUNT, CWE_489_COUNT, \
		CWE_676_COUNT, CWE_326_COUNT, CWE_242_COUNT, CWE_601_COUNT, CWE_338_COUNT, CWE_91_COUNT, \
		CWE_295_COUNT, CWE_77_COUNT, CWE_79_COUNT, total_event_count )

        temp_list.append( the_tup )
    return temp_list 
  

def issueCount(path2dir, csv_fil, bandit_output):
    with open(bandit_output) as f:
        datafile = f.readlines()
        
    issue_file_list = []
    target = "Location:"
    for line in datafile:
        words = line.split()
        for i,w in enumerate(words):
            if w == target:
                file_name = line.split(':')[1]
                file_name = file_name.replace(" ", "")
                issue_file_list.append(file_name)    
    issue_file_list = np.unique(issue_file_list)  

    issue_data  = getCSVData(issue_file_list, bandit_output)
    full_df = pd.DataFrame( issue_data ) 
    
    all_file_list = []
    list_subfolders_with_paths = [f.path for f in os.scandir(path2dir) if f.is_dir()]
    for subfolder in list_subfolders_with_paths: 
        for root_, dirnames, filenames in os.walk(path2dir):
            for file_ in filenames:
                full_path_file = os.path.join(root_,file_) 
                if(os.path.exists(full_path_file)):
                    if (file_.endswith('py')) :
                        all_file_list.append(full_path_file) 
    all_file_list = np.unique(all_file_list)
    
    no_issue_file_list =  np.setdiff1d(all_file_list, issue_file_list)    
    no_issue_data  = getNoIssueCSVData(no_issue_file_list)
    no_issue_df = pd.DataFrame(no_issue_data) 
    
    full_df = full_df.append(no_issue_df)
    
	
    CSV_HEADER = ['REPO_FULL_PATH','FILE_FULL_PATH','CWE_617_COUNT', 'CWE_733_COUNT', 'CWE_78_COUNT',\
	'CWE_269_COUNT', 'CWE_285_COUNT', 'CWE_798_COUNT', 'CWE_259_COUNT', 'CWE_377_COUNT', 'CWE_755_COUNT',\
	'CWE_489_COUNT', 'CWE_676_COUNT', 'CWE_326_COUNT', 'CWE_242_COUNT', 'CWE_601_COUNT', 'CWE_338_COUNT',\
	'CWE_91_COUNT', 'CWE_295_COUNT', 'CWE_77_COUNT', 'CWE_79_COUNT',\
	  'TOTAL_EVENT_COUNT']
    full_df.to_csv(csv_fil, header= CSV_HEADER, index=False, encoding= 'utf-8')     

if __name__=='__main__':
	command_line_flag = False ## after acceptance   

	t1 = time.time()
	print('Started at:', giveTimeStamp() )
	print('*'*100 )

	if command_line_flag:
		dir_path = input(constants.ASK_INPUT_FROM_USER)   
		dir_path = dir_path.strip() 
		if(os.path.exists( dir_path ) ):
			repo_dir    = dir_path 
			output_file = dir_path.split('/')[-2]
			output_csv = output_file + '.csv'
			full_dict  = issueCount(repo_dir, output_csv)
	else: 
		# repo_dir   = 'supervised/GITHUB_REPOS/'
# 		output_csv = 'output/SUPERVISED_OUTPUT_GITHUB.csv'
# 		full_dict  = issueCount(repo_dir, output_csv)
# 		
# 		repo_dir   = 'supervised/GITLAB_REPOS/'
# 		output_csv = 'output/SUPERVISED_OUTPUT_GITLAB.csv'
# 		full_dict  = issueCount(repo_dir, output_csv)
# 		
		repo_dir   = 'supervised_repos/MODELZOO/'
		output_csv = 'output/SUPERVISED_OUTPUT_MODELZOO.csv'
		bandit_output = 'modelzoo_output'
		issueCount(repo_dir, output_csv, bandit_output)


	print('*'*100 )
	print('Ended at:', giveTimeStamp() )
	print('*'*100 )
	
	t2 = time.time()
	time_diff = round( (t2 - t1 ) / 60, 5) 
	print('Duration: {} minutes'.format(time_diff) )
	print('*'*100 )
