import os
import json
import time
from tqdm import tqdm

QUES_TO_SELECT_PER_SEC_IN_SEC_A = 5
QUES_TO_SELECT_PER_SEC_IN_SEC_B = 5
QUES_TO_SELECT_PER_SEC_IN_SEC_C = 5

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
CLEANED_DATA_DIR = PROJECT_DIR + "/cleaned_data"
RESULTS_DIR = PROJECT_DIR + "/results"

grouped_sec_a_ques = {}
grouped_sec_b_ques = {}
grouped_sec_c_ques = {}

groups_len_a = {}
groups_len_b = {}
groups_len_c = {}

groups_len_all = []

n_sec_a = None
n_sec_b = None
n_sec_c = None

def get_data_from_file():
    global grouped_sec_a_ques
    global grouped_sec_b_ques
    global grouped_sec_c_ques

    with open(CLEANED_DATA_DIR + "/grouped_ques.json", 'r') as f:
        temp_dict = json.load(f)
        temp_dict = temp_dict["Questions"]
        grouped_sec_a_ques = temp_dict["Section A"]
        grouped_sec_b_ques = temp_dict["Section B"]
        grouped_sec_c_ques = temp_dict["Section C"]

def find_group_len():
    for i in range(len(grouped_sec_a_ques)):
        curr_grp = "group " + str(i)
        groups_len_a.update({curr_grp: len(grouped_sec_a_ques[curr_grp])})

    for i in range(len(grouped_sec_b_ques)):
        curr_grp = "group " + str(i)
        groups_len_b.update({curr_grp: len(grouped_sec_b_ques[curr_grp])})

    for i in range(len(grouped_sec_c_ques)):
        curr_grp = "group " + str(i)
        groups_len_c.update({curr_grp: len(grouped_sec_c_ques[curr_grp])})

def sort_groups_acc_to_ques_len():
    global groups_len_a
    global groups_len_b
    global groups_len_c

    groups_len_a = dict(sorted(groups_len_a.items(), \
        key = lambda kv: (kv[1], kv[0]), reverse = True))
    groups_len_a = list(groups_len_a.keys())

    groups_len_b = dict(sorted(groups_len_b.items(), \
        key = lambda kv: (kv[1], kv[0]), reverse = True))
    groups_len_b = list(groups_len_b.keys())

    groups_len_c = dict(sorted(groups_len_c.items(), \
        key = lambda kv: (kv[1], kv[0]), reverse = True))
    groups_len_c = list(groups_len_c.keys())

def making_sorted_single_group_of_all_ques():
    global groups_len_all

    for i in range(len(groups_len_a)):
        groups_len_all.append((groups_len_a[i], \
            len(grouped_sec_a_ques[groups_len_a[i]]), "a"))

    for i in range(len(groups_len_b)):
        groups_len_all.append((groups_len_b[i], \
            len(grouped_sec_b_ques[groups_len_b[i]]), "b"))

    for i in range(len(groups_len_c)):
        groups_len_all.append((groups_len_c[i], \
            len(grouped_sec_c_ques[groups_len_c[i]]), "c"))

    groups_len_all = sorted(groups_len_all, reverse = True)

def set_no_of_ques_to_select():
    global n_sec_a
    global n_sec_b
    global n_sec_c
    n_sec_a = min(len(grouped_sec_a_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_A)
    n_sec_b = min(len(grouped_sec_b_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_B)
    n_sec_c = min(len(grouped_sec_c_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_C)

#gives all the top frequently asked questions (unique) 
#from each section separately
def generate_top_freq_ques_per_sec(n_sec_a, n_sec_b, n_sec_c):
    temp_dict = dict()

    ques_list = list()
    for i in range(n_sec_a):
        #print(grouped_sec_a_ques)
        ques_list.append(\
            grouped_sec_a_ques[groups_len_a[i]][0])
    #print(ques_list)
    temp_dict["Section A"] = ques_list
    
    ques_list = list()
    for i in range(n_sec_b):
        ques_list.append(\
            grouped_sec_b_ques[groups_len_b[i]][0])
    temp_dict["Section B"] = ques_list
    
    ques_list = list()
    for i in range(n_sec_c):
        ques_list.append(\
            grouped_sec_c_ques[groups_len_c[i]][0])
    temp_dict["Section C"] = ques_list
    
    final_dict = {"Questions": temp_dict}
    with open(CLEANED_DATA_DIR + "/top_freq_uniq_ques_per_sec.json", \
        'w') as f:
        json.dump(final_dict, f, \
            ensure_ascii=False, indent=4)

    return True

#gives all the top frequently asked questions from all the sections
#combined
def generate_top_freq_ques_all_sec(n):
    n = min(n, len(groups_len_all))

    temp_list = list()
    for i in range(n):
        curr_grp = groups_len_all[i][0]
        curr_sec = groups_len_all[i][2]
        if curr_sec == 'a':
            temp_list.append(grouped_sec_a_ques[curr_grp][0])
        if curr_sec == 'b':
            temp_list.append(grouped_sec_b_ques[curr_grp][0])
        if curr_sec == 'c':
            temp_list.append(grouped_sec_c_ques[curr_grp][0])

    final_dict = {"Questions": temp_list}
    with open(CLEANED_DATA_DIR + "/top_freq_uniq_ques_all_sec.json", \
        'w') as f:
        json.dump(final_dict, f, \
            ensure_ascii=False, indent=4)

#gives all the different types of questions sorted from most frequently
#asked to the lowest frequently asked (removing that are of similar types)
def generate_all_ques_no_dup():
    n = len(groups_len_all)

    temp_list = list()
    for i in range(n):
        curr_grp = groups_len_all[i][0]
        curr_sec = groups_len_all[i][2]
        if curr_sec == 'a':
            temp_list.append(grouped_sec_a_ques[curr_grp][0])
        if curr_sec == 'b':
            temp_list.append(grouped_sec_b_ques[curr_grp][0])
        if curr_sec == 'c':
            temp_list.append(grouped_sec_c_ques[curr_grp][0])

    final_dict = {"Questions": temp_list}
    with open(CLEANED_DATA_DIR + "/all_uniq_ques_all_sec.json", \
        'w') as f:
        json.dump(final_dict, f, \
            ensure_ascii=False, indent=4)

#gives all the different types of questions sorted from most frequently
#asked to the lowest frequently asked (including of similar types)
def generate_all_ques_with_dup():
    n = len(groups_len_all)

    temp_dict = dict()
    for i in range(n):
        curr_grp = groups_len_all[i][0]
        curr_sec = groups_len_all[i][2]
        if curr_sec == 'a':
            temp_dict["group " + str(i)] = grouped_sec_a_ques[curr_grp]
        if curr_sec == 'b':
            temp_dict["group " + str(i)] = grouped_sec_b_ques[curr_grp]
        if curr_sec == 'c':
            temp_dict["group " + str(i)] = grouped_sec_c_ques[curr_grp]

    final_dict = {"Questions": temp_dict}
    with open(CLEANED_DATA_DIR + "/all_ques_all_sec.json", \
        'w') as f:
        json.dump(final_dict, f, \
            ensure_ascii=False, indent=4)

def collective_execution():
    #for loading bar
    pbar = tqdm(total=100)

    get_data_from_file()
    time.sleep(0.1)
    pbar.update(11.1)

    find_group_len()
    time.sleep(0.1)
    pbar.update(11.1)

    sort_groups_acc_to_ques_len()
    time.sleep(0.1)
    pbar.update(11.1)

    making_sorted_single_group_of_all_ques()
    time.sleep(0.1)
    pbar.update(11.1)

    set_no_of_ques_to_select()
    time.sleep(0.1)
    pbar.update(11.1)

    generate_top_freq_ques_per_sec(n_sec_a, n_sec_b, n_sec_c)
    time.sleep(0.1)
    pbar.update(11.1)

    generate_top_freq_ques_all_sec(10)
    time.sleep(0.1)
    pbar.update(11.1)

    generate_all_ques_no_dup()
    time.sleep(0.1)
    pbar.update(11.1)

    generate_all_ques_with_dup()
    time.sleep(0.1)
    pbar.update(11.1)

    pbar.close()

    print()

collective_execution()
