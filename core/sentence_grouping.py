import os
import json
import time
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
from tqdm import tqdm

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
CLEANED_DATA_DIR = PROJECT_DIR + "/cleaned_data"

set_a = [['']] # contains group of similar types of ques of section a
set_b = [['']]
set_c = [['']]
stop_words = list(stopwords.words('english'))

my_stop_words = [ \
'abbreviate', \
'advantage', \
'assume', \
'attempt', \
'b/w', \
'between', \
'brief', \
'briefly', \
'circumstance', \
'clean', \
'consider', \
'considering', \
'could', \
'define', \
'detail', \
'diagram', \
'different', \
'differentiate', \
'distinguish', \
'draw', \
'elaborate', \
'example', \
'explain', \
'find', \
'following', \
'how', \
'list', \
'method', \
'mean', \
'neat', \
'reference', \
'show', \
'that', \
'under', \
'various', \
'would', \
'what', \
'when', \
'write' \
]

blacklist_words = stop_words + my_stop_words
jaccard_similarity_threshold = 0.95                                   

def jaccard_similarity(sent1, sent2):
    sw1 = []
    sw2 = []
    for i in TextBlob(sent1).words:
        i = i.lower()
        temp = Word(i).singularize().lemmatize()
        if i != temp:
            i = temp
        if i not in blacklist_words:
            sw1.append(i)

    for i in TextBlob(sent2).words:
        i = i.lower()
        temp = Word(i).singularize().lemmatize()
        if i != temp:
            i = temp
        if i not in blacklist_words:
            sw2.append(i)

    intersection = set(sent1).intersection(set(sent2))
    union = set(sent1).union(set(sent2))
    similarity = len(intersection)/len(union)
    return similarity

def make_groups():
    global set_a
    global set_b
    global set_c

    with open(CLEANED_DATA_DIR + "/section_a_ques.txt", "r") as f:
        line = f.readline()
        while line:
            found_group = False
            for s in set_a:
                if jaccard_similarity(line, s[0]) >= \
                jaccard_similarity_threshold:
                    s.append(line)
                    found_group = True
            if not found_group:
                set_a.append([line])
            line = f.readline()
    set_a.pop(0)

    with open(CLEANED_DATA_DIR + "/section_b_ques.txt", "r") as f:
        line = f.readline()
        while line:
            found_group = False
            for s in set_b:
                if jaccard_similarity(line, s[0]) >= \
                jaccard_similarity_threshold:
                    s.append(line)
                    found_group = True
            if not found_group:
                set_b.append([line])
            line = f.readline()
    set_b.pop(0)

    with open(CLEANED_DATA_DIR + "/section_c_ques.txt", "r") as f:
        line = f.readline()
        while line:
            found_group = False
            for s in set_c:
                if jaccard_similarity(line, s[0]) >= \
                jaccard_similarity_threshold:
                    s.append(line)
                    found_group = True
            if not found_group:
                set_c.append([line])
            line = f.readline()
    set_c.pop(0)

def export_groups_to_json():
    f = open(CLEANED_DATA_DIR + "/grouped_ques.json", 'w', encoding='utf-8')
    temp_dict = {}

    print("\tIn Section A: ")
    pbar = tqdm(total=100)
    pbar_len = 100 / len(set_a)
    inner_temp_dict = dict()
    for i in range(len(set_a)):

        # for loading bar
        time.sleep(0.1)
        pbar.update(pbar_len)

        curr_key = "group " + str(i)
        for j in set_a[i]:
            curr_list = inner_temp_dict.get(curr_key)
            if curr_list is None:
                curr_list = []
            curr_list.append(j.strip())
            inner_temp_dict.update({curr_key: curr_list})
    temp_dict.update({"Section A": inner_temp_dict})
    
    pbar.close()

    print("\tIn Section B: ")
    pbar = tqdm(total=100)
    pbar_len = 100 / len(set_b)
    inner_temp_dict = dict()
    for i in range(len(set_b)):

        # for loading bar
        time.sleep(0.1)
        pbar.update(pbar_len)

        curr_key = "group " + str(i)
        for j in set_b[i]:
            curr_list = inner_temp_dict.get(curr_key)
            if curr_list is None:
                curr_list = []
            curr_list.append(j.strip())
            inner_temp_dict.update({curr_key: curr_list})
    temp_dict.update({"Section B": inner_temp_dict})
    
    pbar.close()

    print("\tIn Section C: ")
    pbar = tqdm(total=100)
    pbar_len = 100 / len(set_c)
    inner_temp_dict = dict()
    for i in range(len(set_c)):

        # for loading bar
        time.sleep(0.1)
        pbar.update(pbar_len)

        curr_key = "group " + str(i)
        for j in set_c[i]:
            curr_list = inner_temp_dict.get(curr_key)
            if curr_list is None:
                curr_list = []
            curr_list.append(j.strip())
            inner_temp_dict.update({curr_key: curr_list})
    temp_dict.update({"Section C": inner_temp_dict})

    final_dict = {"Questions": temp_dict}

    pbar.close()

    json.dump(final_dict, f, ensure_ascii=False, indent=4)
    f.close()  

def delete_redundant_files():
    os.remove(CLEANED_DATA_DIR + "/section_a_ques.txt")
    os.remove(CLEANED_DATA_DIR + "/section_b_ques.txt")
    os.remove(CLEANED_DATA_DIR + "/section_c_ques.txt")

make_groups()
export_groups_to_json()
delete_redundant_files()
print('\n')