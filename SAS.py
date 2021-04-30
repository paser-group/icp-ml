import os
import re
import subprocess
import numpy as np

def runBandit(python_file_list):
    for PYTHON_SCRIPT in python_file_list:
        PYTHON_SCRIPT = re.escape(PYTHON_SCRIPT)
        cmd_ = "bandit " + PYTHON_SCRIPT + " > bandit_output"
        print(cmd_)
        try:
            subprocess.check_output(['bash','-c', cmd_])    
        except subprocess.CalledProcessError:
            print('Cant run bandit on', PYTHON_SCRIPT )
        
        alert_line = 0       
        for i, line in enumerate(open('bandit_output')):
            if('No issues identified' in line):
                print("No Issue")
                alert_line = -1
        if(alert_line != -1):
            print("Found Issue")
            with open("bandit_output") as f:
                #with open("modelzoo_output", "a") as outfile:
                with open("modelzoo_output", "a") as outfile:
                    outfile.write(PYTHON_SCRIPT)
                    for line in f:
                        outfile.write(line) 
                    outfile.write("*"*1000)
    

                        
if __name__=='__main__':
    path2dir = 'supervised_repos/MODELZOO'
    #path2dir = 'supervised_repos/GITLAB_REPOS'
    #path2dir = 'Comparison/NON_ML_REPOS'
    python_file_list = []
    list_subfolders_with_paths = [f.path for f in os.scandir(path2dir) if f.is_dir()]
    for subfolder in list_subfolders_with_paths: 
        print(subfolder)
        print("#"*1000)
        for root_, dirnames, filenames in os.walk(path2dir):
            for file_ in filenames:
                full_path_file = os.path.join(root_,file_) 
                if(os.path.exists(full_path_file)):
                    if (file_.endswith('py')) :
                        python_file_list.append(full_path_file) 
    
    python_file_list = np.unique(  python_file_list )
    runBandit(python_file_list)


