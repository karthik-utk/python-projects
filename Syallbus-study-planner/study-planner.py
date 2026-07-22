import fitz  
from datetime import datetime
from google import genai

def read_pdf(path):

    try:
        doc = fitz.open(path)
        pdf_content = ''
    except Exception as e:
        print(f'Error ocurred: {e}')
        exit()

    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()

        pdf_content += text
        
    doc.close()
    
    if len(pdf_content.strip()) < 50:
        print('This PDF appears to have no extractable text (it may be a scanned/image-based PDF). Try a text-based PDF instead.')
        exit()
    
    return pdf_content

def days_until(date_string):
    exam_date = datetime.strptime(date_string, "%Y-%m-%d")
    date_today = datetime.now()

    days_left = exam_date - date_today

    return days_left.days

def build_prompt(pdf_text, days_left):

    return f'Act as an expert academic coach and create a hyper-customized daily study plan based on the content and timeline provided below. Format the output with clear daily milestones, active recall checkpoints, and built-in review sessions to ensure mastery before the deadline. Days Remaining: {days_left} Content to Cover:{pdf_text}'

def get_study_plan(prompt):
    try:
        client = genai.Client()

        response = client.models.generate_content(
            model = "gemini-3.5-flash",
            contents = prompt
        )

        return response.text
    except Exception as e:
        print(f'Error occured : {e}')
        exit()

def main():
    path = input('Enter the pdf file path: ')
    date_string = input('Enter the exam date("YYYY-MM-DD"): ')

    pdf_text = read_pdf(path)
    days_left = days_until(date_string)
    prompt = build_prompt(pdf_text,days_left)

    print(f'Your study plan:\n{get_study_plan(prompt)}')
    

if __name__ == "__main__":
    main()