import os
import json
import nltk
from tkinter import *
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords
from nltk.corpus import state_union

QUES_TO_SELECT_PER_SEC_IN_SEC_A = 5
QUES_TO_SELECT_PER_SEC_IN_SEC_B = 5
QUES_TO_SELECT_PER_SEC_IN_SEC_C = 5

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
CLEANED_DATA_DIR = PROJECT_DIR + "/cleaned_data"

grouped_sec_a_ques = {}
grouped_sec_b_ques = {}
grouped_sec_c_ques = {}

groups_len_a = {}
groups_len_b = {}
groups_len_c = {}

top_sec_a_ques = []
top_sec_b_ques = []
top_sec_c_ques = []

with open(CLEANED_DATA_DIR + "/grouped_ques.json", 'r') as f:
    temp_dict = json.load(f)
    temp_dict = temp_dict["Questions"]
    grouped_sec_a_ques = temp_dict["Section A"]
    grouped_sec_b_ques = temp_dict["Section B"]
    grouped_sec_c_ques = temp_dict["Section C"]

n_sec_a = min(len(grouped_sec_a_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_A)
n_sec_b = min(len(grouped_sec_b_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_B)
n_sec_c = min(len(grouped_sec_c_ques), QUES_TO_SELECT_PER_SEC_IN_SEC_C)


#gives all the top frequently asked questions from each section
#separately
def generate_top_freq_ques_per_sec(n_sec_a, n_sec_b, n_sec_c):
    for i in range(n_sec_a):
        top_sec_a_ques.append(grouped_sec_a_ques["group " + str(i)][0])
    
    for i in range(n_sec_b):
        top_sec_b_ques.append(grouped_sec_b_ques["group " + str(i)][0])
    
    for i in range(n_sec_c):
        top_sec_c_ques.append(grouped_sec_c_ques["group " + str(i)][0])
    return True


#gives all the top frequently asked questions from all the sections
#combined
def generate_top_freq_ques_all_sec():
    pass

#gives all the different types of questions sorted from most frequently
#asked to the lowest frequently asked (removing duplicates)
def generate_all_ques_no_dup():
    pass

#gives all the different types of questions sorted from most frequently
#asked to the lowest frequently asked (including duplicates)
def generate_all_ques_with_dup():
    pass
