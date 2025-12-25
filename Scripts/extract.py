import os
import pdfplumber
import re
import json
import random

PDF_FOLDER = "C:\\Users\\Amrita\\Desktop\\Python Project - Copy\\PYP's"

all_questions=[]

for filename in os.listdir(PDF_FOLDER):
    pdf_path = os.path.join(PDF_FOLDER, filename)  
    year = int(filename.split("_")[0])       
    full_text = ""           
    with pdfplumber.open(pdf_path) as pdf:  
        for page in pdf.pages:              
            text = page.extract_text()    
            full_text += "\n" + text

    current_subject = None
    current_question = None

    lines = full_text.splitlines()

    for line in lines:
        line_clean = line.strip()
        line_upper = line_clean.upper()

            
        if "PHYSICS" in line_upper:
            current_subject = "physics"
            continue
        elif "CHEMISTRY" in line_upper:
            current_subject = "chemistry"
            continue
        elif "MATHEMATICS" in line_upper or "MATHS" in line_upper:
            current_subject = "maths"
            continue

           
        if current_subject and re.search(r"Q\.\s*\d+", line_clean):

        
            if current_question:
              all_questions.append({
                  "year": year,
                  "subject": current_subject,
                  "question": current_question.strip()
              })

        
            current_question = line_clean

        else:
            if current_question:
              current_question += " " + line_clean
    if current_question:
       all_questions.append({
        "year": year,
        "subject": current_subject,
        "question": current_question.strip()
       })
            
OUTPUT_FILE = "C:\\Users\\Amrita\\Desktop\\Python Project - Copy\\Data\\all_questions.json"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=4, ensure_ascii=False)

with open("C:\\Users\\Amrita\\Desktop\\Python Project - Copy\\Data\\all_questions.json", "r", encoding="utf-8") as f:
    all_questions = json.load(f)

def get_random_question(year, subject):
    filtered = []
    for q in all_questions:
        if q["year"] == year and q["subject"] == subject:
            filtered.append(q)
    
    if len(filtered) == 0:
        return None

    return random.choice(filtered)

year = 2022
subject = "maths"

q = get_random_question(year, subject)

if q:
    print("Year:", q["year"])
    print("Subject:", q["subject"])
    print("Question:", q["question"])

                
       

       

     

      

            

        

