import PyPDF2
import re
from datetime import datetime

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text

def analyze_questions(text):
    # Extract questions based on question numbers
    questions_with_numbers = re.findall(r'\d+\..*?(?=\d+\.|$)', text, re.DOTALL)

    # Flatten the list of questions
    questions = [question.strip() for question_with_number in questions_with_numbers for question in question_with_number.split('\n') if question.strip()]

    # Create a timestamp for the output file name
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f"output_{timestamp}.txt"

    # Save the questions to a new file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write("Extracted Questions:\n")
        for question in questions:
            file.write(f"{question}\n")

    # Print success message
    print(f"Analysis completed successfully! Questions saved to {output_file}")

# Example usage
pdf_path = "path/to/your/file.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
analyze_questions(pdf_text)
