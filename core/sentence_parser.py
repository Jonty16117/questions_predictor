import os
import json
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords

QUES_TO_SELECT_PER_SEC_IN_SEC_A = 5
QUES_TO_SELECT_PER_SEC_IN_SEC_B = 5
QUES_TO_SELECT_PER_SEC_IN_SEC_C = 5

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
CLEANED_DATA_DIR = PROJECT_DIR + "/cleaned_data"

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

grouped_sec_a_ques = {}
grouped_sec_b_ques = {}
grouped_sec_c_ques = {}

final_sec_a_ques = []
final_sec_b_ques = []
final_sec_c_ques = []

with open(CLEANED_DATA_DIR + "/grouped_ques.json", 'r') as f:
    temp_dict = json.load(f)
    temp_dict = temp_dict["Questions"]
    grouped_sec_a_ques = temp_dict["Section A"]
    grouped_sec_b_ques = temp_dict["Section B"]
    grouped_sec_c_ques = temp_dict["Section C"]

n_sec_a = min(len(grouped_sec_a_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_A)
n_sec_b = min(len(grouped_sec_b_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_B)
n_sec_c = min(len(grouped_sec_c_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_C)

def parse_ques_per_group(list_of_ques):
    no_of_que = len(list_of_ques)

    #if this group contains only one question
    #then return this question as it is
    if no_of_que == 1:
        return list_of_ques[0]

    word_list_list = list()
    main_words_for_final_ques = set()
    for i in range(no_of_que):
        #convert ques into list of words
        temp = TextBlob(list_of_ques[i]).words

        #lowercase each word
        temp = [w.lower() for w in temp]

        #singularize and lemmatize each word
        temp = [Word(w).singularize().lemmatize() for w in temp.copy()]

        #filter out all the stop words
        temp2= []
        for w in temp:
            if w not in blacklist_words:
                temp2.append(w)
        temp = temp2
        temp2 = None

        #put this list of words into target words
        word_list_list.append(temp)

    main_words_for_final_ques = \
    set(word_list_list.pop()).intersection(set(word_list_list.pop()))

    for word_list in word_list_list:
        main_words_for_final_ques = \
        main_words_for_final_ques.intersection(set(word_list))

    #deleting word_list_list
    word_list_list = None

    #now we have a list of words, from which we now 
    #need to make one quesiton. To do this we'll make
    #some production rules for our sentence grammar, 
    #then we will generate a parse tree from those rules
    #on our list of words to make a sentence, which 
    #will be our final output sentence

    #return one_final_ques

#print(grouped_sec_a_ques.get("group 0"))
parse_ques_per_group(grouped_sec_a_ques.get("group 0"))

def do_n_times_parsing(n_sec_a, n_sec_b, n_sec_c):
    #for section a
    for i in range(n_sec_a):
        parsed_ques = \
        parse_ques_per_group(grouped_sec_a_ques.get("group " + str(i)))
        final_sec_a_ques.append(parsed_ques)
    
    #for section b
    for i in range(n_sec_b):
        parsed_ques = \
        parse_ques_per_group(grouped_sec_b_ques.get("group " + str(i)))
        final_sec_b_ques.append(parsed_ques)

    #for section c
    for i in range(n_sec_c):
        parsed_ques = \
        parse_ques_per_group(grouped_sec_c_ques.get("group " + str(i)))
        final_sec_c_ques.append(parsed_ques)

print("done")
