import os
import json
from fpdf import FPDF

PROJECT_DIR = os.path.abspath(os.path.join(".", os.pardir))
CLEANED_DATA_DIR = PROJECT_DIR + "/cleaned_data"
RESULTS_DIR = PROJECT_DIR + "/results"

ques_set_1 = {}
ques_set_2 = {}
ques_set_3 = {}
ques_set_4 = {}

def get_data_from_json():
    global ques_set_1
    global ques_set_2
    global ques_set_3
    global ques_set_4

    with open(CLEANED_DATA_DIR + "/top_freq_uniq_ques_per_sec.json", \
        'r') as f:
        temp = json.load(f)
        ques_set_1 = temp["Questions"]

    with open(CLEANED_DATA_DIR + "/top_freq_uniq_ques_all_sec.json", \
        'r') as f:
        ques_set_2 = json.load(f)

    with open(CLEANED_DATA_DIR + "/all_uniq_ques_all_sec.json", \
        'r') as f:
        ques_set_3 = json.load(f)

    with open(CLEANED_DATA_DIR + "/all_ques_all_sec.json", \
        'r') as f:
        temp = json.load(f)
        ques_set_4 = temp["Questions"]

def make_pdf():
    pdf = FPDF()

    #adding ques_set_1 to pdf
    pdf.add_page()
    
    #header for the first set of questions
    header_text_1 = "Most important questions from each section"
    header_text_2 = "(sorted in descending order on the basis of importance)"
    pdf.set_font('Arial', '', 18)
    pdf.set_fill_color(117, 163, 163)
    pdf.cell(190, 10, header_text_1, border = 0, align = 'C', ln = 2, fill = True)
    pdf.set_font('Arial', 'IU', 10)
    pdf.set_fill_color(179, 204, 204)
    pdf.cell(190, 5, header_text_2, border = 0, align = 'C', ln = 2, fill = True)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)



    #adding section a questions
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(255, 26, 26)
    pdf.cell(190, 7, "Section A", border = 0, align = 'C', ln = 2, fill = True)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.set_font('Arial', '', 14)
    for i in range(len(ques_set_1["Section A"])):
        pdf.cell(190, 8, "Q" + str(i + 1) + ") " + ques_set_1['Section A'][i], border = 0, align = 'L', ln = 2)
            
    #add spacing
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)

    #adding section b questions
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(57, 230, 0)
    pdf.cell(190, 7, "Section B", border = 0, align = 'C', ln = 2, fill = True)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.set_font('Arial', '', 14)
    for i in range(len(ques_set_1["Section B"])):
        pdf.cell(190, 8, "Q" + str(i + 1) + ") " + ques_set_1['Section B'][i], border = 0, align = 'L', ln = 2)

    #add spacing
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)

    #adding section c questions
    pdf.set_font('Arial', 'B', 16)
    pdf.set_fill_color(51, 153, 255)
    pdf.cell(190, 7, "Section C", border = 0, align = 'C', ln = 2, fill = True)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.set_font('Arial', '', 14)
    for i in range(len(ques_set_1["Section C"])):
        pdf.cell(190, 8, "Q" + str(i + 1) + ") " + ques_set_1['Section C'][i], border = 0, align = 'L', ln = 2)

    #adding ques_set_2 to pdf
    pdf.add_page()

    #header for the second set of questions
    header_text_1 = "Most important questions from all sections"
    header_text_2 = "(sorted in descending order on the basis of importance)"
    pdf.set_font('Arial', '', 18)
    pdf.set_fill_color(117, 163, 163)
    pdf.cell(190, 10, header_text_1, border = 0, align = 'C', ln = 2, fill = True)
    pdf.set_font('Arial', 'IU', 10)
    pdf.set_fill_color(179, 204, 204)
    pdf.cell(190, 5, header_text_2, border = 0, align = 'C', ln = 2, fill = True)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)


    #adding questions
    pdf.set_font('Arial', '', 14)
    for i in range(len(ques_set_2["Questions"])):
        pdf.cell(190, 8, "Q" + str(i + 1) + ") " + ques_set_2['Questions'][i], border = 0, align = 'L', ln = 2)


    #adding ques_set_3 to pdf
    pdf.add_page()

    #header for the third set of questions
    header_text_1 = "All unique questions from all sections"
    header_text_2 = "(sorted in descending order on the basis of importance)"
    pdf.set_font('Arial', '', 18)
    pdf.set_fill_color(117, 163, 163)
    pdf.cell(190, 10, header_text_1, border = 0, align = 'C', ln = 2, fill = True)
    pdf.set_font('Arial', 'IU', 10)
    pdf.set_fill_color(179, 204, 204)
    pdf.cell(190, 5, header_text_2, border = 0, align = 'C', ln = 2, fill = True)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)

    #adding questions
    pdf.set_font('Arial', '', 14)
    for i in range(len(ques_set_3["Questions"])):
        pdf.cell(190, 8, "Q" + str(i + 1) + ") " + ques_set_3['Questions'][i], border = 0, align = 'L', ln = 2)
        

    #adding ques_set_4 to pdf
    pdf.add_page()

    #header for the fourth set of questions
    header_text_1 = "All questions from all sections"
    header_text_2 = "(first question of each type of question is colour coded and sorted in descending order on the basis of importance)"
    pdf.set_font('Arial', '', 18)
    pdf.set_fill_color(117, 163, 163)
    pdf.cell(190, 10, header_text_1, border = 0, align = 'C', ln = 2, fill = True)
    pdf.set_font('Arial', 'IU', 10)
    pdf.set_fill_color(179, 204, 204)
    pdf.cell(190, 5, header_text_2, border = 0, align = 'C', ln = 2, fill = True)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)
    pdf.cell(190, 5, '', border = 0, align = 'C', ln = 2)

    #adding questions
    pdf.set_font('Arial', '', 14)
    ques_no = 1
    first_ques_of_group = True
    red = 0
    green = 255
    blue = 0
    inc_tans = 255//len(ques_set_4)
    for i in range(len(ques_set_4)):
        curr_group = "group " + str(i)
        pdf.set_fill_color(r = red, g = green, b = blue)
        pdf.cell(190, 8, "Q" + str(ques_no) + ") " + ques_set_4[curr_group][0], border = 0, align = 'L', ln = 2, fill = True)
        ques_no += 1
        red += inc_tans
        blue += inc_tans
        pdf.set_fill_color(r = red, g = green, b = blue)
        for j in range(1, len(ques_set_4[curr_group])):
            pdf.cell(190, 8, "Q" + str(ques_no) + ") " + ques_set_4[curr_group][j], border = 0, align = 'L', ln = 2, fill = False)
            ques_no += 1


    #saving the resultant file
    pdf.output(RESULTS_DIR + '/results.pdf', 'F')


get_data_from_json()
make_pdf()
