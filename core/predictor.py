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

1) Make a grammar from the given language to make one
final question from each group

2) Parse a sentence from this grammar using parse tree
for each group

3) Save this sentence

Step 4):

1) Separate each question in different section

2) Format the final results

3) Produce the final result file in the required format
'''




import os
from textblob import TextBlob
from textblob import Word
from nltk.corpus import stopwords

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
CLEANED_DATA_DIR = PROJECT_DIR + "/cleaned_data"

set_a = [[None]] # contains group of similar types of ques of section a
set_b = [[None]]
set_c = [[None]]
ques_parse_tags = ['WRB', 'WP', 'WDT', 'VB', 'MD', 'JJ']
stop_words = list(stopwords.words('english'))
jaccard_similarity_threshold = None

def jaccard_similarity(sent1, sent2):
    sw1 = TextBlob(sent1).tags
    sw2 = TextBlob(sent2).tags
    sent1 = []
    sent2 = []

    for i in sw1:
        if i[1] not in ques_parse_tags:
            sent1.append(i[0])

    for i in sw2:
        if i[1] not in ques_parse_tags:
            sent2.append(i[0])

    sent1 = [word.lower() for word in sent1 if not word in stop_words]
    sent2 = [word.lower() for word in sent2 if not word in stop_words]

    for i in range(len(sent1)):
        temp = Word(sent1[i]).singularize().lemmatize()
        if sent1[i] != temp:
            sent1[i] = temp

    for i in range(len(sent2)):
        temp = Word(sent2[i]).singularize().lemmatize()
        if sent2[i] != temp:
            sent2[i] = temp

    intersection = set(sent1).intersection(set(sent2))
    union = set(sent1).union(set(sent2))
    # print(sent1)
    # print(sent2)
    return len(intersection)/len(union)


def make_groups():
    global set_a
    global set_b
    global set_c

    with open(CLEANED_DATA_DIR + "/section_a_ques.txt", "r") as f:
        line = f.readline()
        while line:
            found_group = False
            for s in set_a:
                if jaccard_similarity(line, s[0]) >= jaccard_similarity_threshold:
                    s.append(line)
                    found_group = True
            if not found_group:
                set_a.append([line])
            line = f.readline()




#sent1 = [word for word in "what do you mean by time sharing systems?".split() if not word in stop_words]
#print(sent1)
i = jaccard_similarity("Explain Time sharing systems.", "what do you mean by time sharing systems?")
print(i)