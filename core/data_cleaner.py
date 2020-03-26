import os
import re
from textblob import TextBlob

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
RAW_DATA_DIR = PROJECT_DIR + "/raw_data"
CLEANED_DATA_DIR = PROJECT_DIR + "/cleaned_data"

raw_data = None
with open(f"{RAW_DATA_DIR}/raw_data.txt") as f:
    raw_data = f.read()

tb = TextBlob(raw_data)

section_a_ques = []
section_b_ques = []
section_c_ques = []

currently_in_section_a = False
currently_in_section_b = False
currently_in_section_c = False


def set_ques_flags(curr_list):
    global currently_in_section_a
    global currently_in_section_b
    global currently_in_section_c
    curr_str = ''.join(curr_list)
    if (re.search("(s|S)(e|E)(c|C)(t|T)(i|I)(o|O)(n|N).*[aA]\\s*.*(2).*(20)", curr_str)) is not None:
        section_a_ques.append(''.join(re.findall("[a-z|A-Z][a-z|A-Z].*[\\.|\\?]", ''.join(re.findall("[a|A|1|i|I|]{1}[\\)|\\.|].*\\.", curr_str)))))
        currently_in_section_a = True
        currently_in_section_b = False
        currently_in_section_c = False

    elif (re.search("(s|S)(e|E)(c|C)(t|T)(i|I)(o|O)(n|N).*[bB]\\s*.*(4|5).*(20)", curr_str)) is not None:
        section_b_ques.append(''.join(re.findall("[a-z|A-Z][a-z|A-Z].*[\\.|\\?]", curr_str)))
        currently_in_section_a = False
        currently_in_section_b = True
        currently_in_section_c = False

    elif (re.search("(s|S)(e|E)(c|C)(t|T)(i|I)(o|O)(n|N).*[cC]\\s*.*(10).*(20)", curr_str)) is not None:
        section_c_ques.append(''.join(re.findall("[a-z|A-Z][a-z|A-Z].*[\\.|\\?]", curr_str)))
        currently_in_section_a = False
        currently_in_section_b = False
        currently_in_section_c = True

def get_ques():
    global section_a_ques
    global section_b_ques
    global section_c_ques

    for i in tb.sentences:
        #print(i)
        #print(type(str(i)))
        set_ques_flags(i)

        if currently_in_section_a:
            section_a_ques.append(''.join(re.findall("[a-z|A-Z][a-z|A-Z].*[\\.|\\?]", str(i))))

        elif currently_in_section_b:
            section_b_ques.append(''.join(re.findall("[a-z|A-Z][a-z|A-Z].*[\\.|\\?]", str(i))))

        elif currently_in_section_c:
            section_c_ques.append(''.join(re.findall("[a-z|A-Z][a-z|A-Z].*[\\.|\\?]", str(i))))

def remove_empty_ques():
    global section_a_ques
    global section_b_ques
    global section_c_ques

    section_a_ques = list(filter(None, section_a_ques)) 
    section_b_ques = list(filter(None, section_b_ques))
    section_c_ques = list(filter(None, section_c_ques)) 

def save_cleaned_data():
    global section_a_ques
    global section_b_ques
    global section_c_ques

    #save this cleaned data
    with open(CLEANED_DATA_DIR + "/section_a_ques" + ".txt", "w") as f:
        for i in section_a_ques:
            f.write(i + "\r\n")
    with open(CLEANED_DATA_DIR + "/section_b_ques" + ".txt", "w") as f:
        for i in section_b_ques:
            f.write(i + "\r\n")
    with open(CLEANED_DATA_DIR + "/section_c_ques" + ".txt", "w") as f:
        for i in section_c_ques:
            f.write(i + "\r\n")

get_ques()
remove_empty_ques()
save_cleaned_data()




#print(section_c_ques)
# print("+++++++++++++++++++section_a_ques+++++++++++++++++++")
# for i in section_a_ques:
#     print(i)
# print("+++++++++++++++++++section_b_ques+++++++++++++++++++")
# for i in section_b_ques:
#     print(i)
# print("+++++++++++++++++++section_c_ques+++++++++++++++++++")
# for i in section_c_ques:
#     print(i)

