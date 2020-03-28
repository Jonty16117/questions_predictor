'''
What I currently have in mind to solve this problem is
informaly described below.

Okay, so we have 3 sets of questions:
-> section_a_ques
-> section_b_ques
-> section_c_ques,
all in the form of sentences, separated by lines
in 3 different files.

Our target is to find the most (and by most we can
assume about 5 questions per section) frequently 
asked questions from each section.Ideally our 
training test will contain manyquestions of a 
single type, however if at some point all the next 
questions are present with the same frequency, 
select the next ones as in the sequence.

Assuming that there will be many questions asking
the same thing, but in different way (or syntax),
one of the possible way to do this can be describe
using the following procedure as:

1) Compare each question with all other questions
in each section and make groups for similar types 
of questions.

2) Select top 5 groups from each section, therefore
in total there will be 15 groups

3) Parse one question from each group, therefore 
there will be total 15 questions at the end

4) Store the final questions in the result file

We will now do each step individually. Step one and
step 3 will be the most difficult to design I think.
Each of the step will contain many subroutines and 
algorithms, therefore each step is individually 
showcased below:

Step 1):

1) Pick one sentence and compare with first (or any) 
sentence from each group

2) If this sentence matches with any group 
copy that sentence to that group

3) If this sentence does not matches with any group,
then create a new group and copy this sentence to 
this group

Step 2):

1) Just filter the top 5 groups according to their
length from each section

Step 3):

1) Select the top most question from each group

Step 4):

1) Separate each question in different section

2) Format the final results

3) Produce the final result file in the required format
'''

import os
import json
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords

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

    inner_temp_dict = dict()
    for i in range(len(set_a)):
        curr_key = "group " + str(i)
        for j in set_a[i]:
            curr_list = inner_temp_dict.get(curr_key)
            if curr_list is None:
                curr_list = []
            curr_list.append(j.strip())
            inner_temp_dict.update({curr_key: curr_list})
    temp_dict.update({"Section A": inner_temp_dict})
    
    inner_temp_dict = dict()
    for i in range(len(set_b)):
        curr_key = "group " + str(i)
        for j in set_b[i]:
            curr_list = inner_temp_dict.get(curr_key)
            if curr_list is None:
                curr_list = []
            curr_list.append(j.strip())
            inner_temp_dict.update({curr_key: curr_list})
    temp_dict.update({"Section B": inner_temp_dict})
    
    inner_temp_dict = dict()
    for i in range(len(set_c)):
        curr_key = "group " + str(i)
        for j in set_c[i]:
            curr_list = inner_temp_dict.get(curr_key)
            if curr_list is None:
                curr_list = []
            curr_list.append(j.strip())
            inner_temp_dict.update({curr_key: curr_list})
    temp_dict.update({"Section C": inner_temp_dict})

    final_dict = {"Questions": temp_dict}

    json.dump(final_dict, f, ensure_ascii=False, indent=4)
    f.close()  

make_groups()
export_groups_to_json()