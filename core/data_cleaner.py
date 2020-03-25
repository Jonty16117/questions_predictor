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
	curr_str = ''.join(curr_list)
	if (re.search("(s|S)(e|E)(c|C)(t|T)(i|I)(o|O)(n|N).*[aA]\\s*.*(2).*(20)", curr_str)) is not None:
		section_a_ques.append(\
			''.join(re.findall("[a-z|A-Z][a-z|A-Z].*[\\.|\\?]", ''.join(re.findall("[a|A|1|i|I|]{1}[\\)|\\.|].*\\.", curr_str)))))
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

for i in tb.sentences:
	#print(i)
	set_ques_flags(i)
	
	'''
	if we see "section a", then continue to add all next question
	to list until we see "section b"	
	'''
	# if currently_in_section_a:
	#     pass

	'''
	if we see "section b", then continue to add all next question
	to list until we see "section c"	
	'''
	# else if currently_in_section_b:
	#     pass

	'''
	if we see "section c", then continue to add all next question
	to list until we see "section a" or end of the string                                                   	
	'''
	# else if currently_in_section_c:
	#     pass
print(section_a_ques)
print(section_b_ques)
print(section_c_ques)