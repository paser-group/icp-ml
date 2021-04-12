import numpy as np 

if __name__=='__main__':

    with open('gitlab_partial_output') as f:
        datafile = f.readlines()
        
    issue_list = []
    target = "Issue:"
    for line in datafile:
        words = line.split()
        for i,w in enumerate(words):
            if w == target:
                issue_list.append(words[i+1])
            
    issue_list = np.unique(issue_list)
    print (issue_list) 