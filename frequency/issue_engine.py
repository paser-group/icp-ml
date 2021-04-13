import numpy as np 

def getAllIssueCount(bandit_output, target_file_name):
    with open(bandit_output) as f:
        datafile = f.readlines()
        
        
        CWE_61_COUNT = CWE_77_COUNT = CWE_78_COUNT = CWE_79_COUNT = CWE_89_COUNT = CWE_91_COUNT = \
        CWE_220_COUNT = CWE_242_COUNT = CWE_259_COUNT = CWE_269_COUNT = CWE_285_COUNT = CWE_295_COUNT = \
        CWE_319_COUNT = CWE_326_COUNT = CWE_338_COUNT = CWE_377_COUNT = CWE_477_COUNT = CWE_489_COUNT = \
        CWE_601_COUNT = CWE_617_COUNT = CWE_676_COUNT = CWE_733_COUNT = CWE_755_COUNT = CWE_798_COUNT = 0
    
    issue = ""
    file_name = ""
    target1 = "Issue:"
    target2 = "Location:"
    for line in datafile:
        words = line.split()
        for i,w in enumerate(words):
            if w == target1:
                issue = words[i+1]
            elif w == target2:
                file_name = line.split(':')[1]
                file_name = file_name.replace(" ", "")
                if file_name == target_file_name:
                    if ('B101' in issue):
                        CWE_617_COUNT =+ 1 
                        CWE_733_COUNT =+ 1
                    elif ('B102' in issue):
                        CWE_78_COUNT =+ 1
                    elif ('B103' in issue):
                        CWE_269_COUNT =+ 1
                    elif ('B104' in issue):
                        CWE_285_COUNT =+ 1
                    elif ('B105' in issue):
                        CWE_798_COUNT =+ 1
                        CWE_259_COUNT =+ 1
                    elif ('B106' in issue):
                        CWE_798_COUNT =+ 1
                        CWE_259_COUNT =+ 1
                    elif ('B107' in issue):
                        CWE_798_COUNT =+ 1
                        CWE_259_COUNT =+ 1
                    elif ('B108' in issue):
                        CWE_377_COUNT =+ 1
                    elif ('B110' in issue):
                        CWE_755_COUNT =+ 1
                    elif ('B112' in issue):
                        CWE_755_COUNT =+ 1
                    elif ('B201' in issue):
                        CWE_489_COUNT =+ 1
                    elif ('B301' in issue):
                        CWE_676_COUNT =+ 1
                    elif ('B302' in issue):
                        CWE_676_COUNT =+ 1
                    elif ('B303' in issue):
                        CWE_326_COUNT =+ 1
                    elif ('B306' in issue):
                        CWE_242_COUNT =+ 1
                    elif ('B307' in issue):
                        CWE_676_COUNT =+ 1
                    elif ('B308' in issue):
                        CWE_676_COUNT =+ 1
                    elif ('B309' in issue):
                        CWE_319_COUNT =+ 1
                    elif ('B310' in issue):
                        CWE_601_COUNT =+ 1
                    elif ('B311' in issue):
                        CWE_338_COUNT =+ 1
                    elif ('B313' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B314' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B318' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B319' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B320' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B321' in issue):
                        CWE_220_COUNT =+ 1
                    elif ('B323' in issue):
                        CWE_295_COUNT =+ 1
                    elif ('B325' in issue):
                        CWE_61_COUNT =+ 1
                    elif ('B402' in issue):
                        CWE_220_COUNT =+ 1
                    elif ('B403' in issue):
                        CWE_676_COUNT =+ 1
                    elif ('B404' in issue):
                        CWE_676_COUNT =+ 1
                    elif ('B405' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B406' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B408' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B409' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B410' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B411' in issue):
                        CWE_91_COUNT =+ 1
                    elif ('B413' in issue):
                        CWE_477_COUNT =+ 1
                    elif ('B501' in issue):
                        CWE_319_COUNT =+ 1
                    elif ('B504' in issue):
                        CWE_295_COUNT =+ 1
                    elif ('B505' in issue):
                        CWE_326_COUNT =+ 1
                    elif ('B506' in issue):
                        CWE_676_COUNT =+ 1
                    elif ('B602' in issue):
                        CWE_77_COUNT =+ 1
                    elif ('B603' in issue):
                        CWE_77_COUNT =+ 1
                    elif ('B604' in issue):
                        CWE_77_COUNT =+ 1
                    elif ('B605' in issue):
                        CWE_77_COUNT =+ 1
                    elif ('B607' in issue):
                        CWE_77_COUNT =+ 1
                    elif ('B610' in issue):
                        CWE_89_COUNT =+ 1
                    elif ('B611' in issue):
                        CWE_89_COUNT =+ 1
                    elif ('B701' in issue):
                        CWE_79_COUNT =+ 1
                    elif ('B702' in issue):
                        CWE_79_COUNT =+ 1
                    elif ('B703' in issue):
                        CWE_89_COUNT =+ 1
                    
                    
    return CWE_61_COUNT, CWE_77_COUNT, CWE_78_COUNT, CWE_79_COUNT, CWE_89_COUNT, CWE_91_COUNT, \
        CWE_220_COUNT, CWE_242_COUNT, CWE_259_COUNT, CWE_269_COUNT, CWE_285_COUNT, CWE_295_COUNT, \
        CWE_319_COUNT, CWE_326_COUNT, CWE_338_COUNT, CWE_377_COUNT, CWE_477_COUNT, CWE_489_COUNT, \
        CWE_601_COUNT, CWE_617_COUNT, CWE_676_COUNT, CWE_733_COUNT, CWE_755_COUNT, CWE_798_COUNT
