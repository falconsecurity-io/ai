import openai
import os
from dotenv import load_dotenv
import docx

load_dotenv()

def read_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def generate_resume(template, job_aposting):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"""
    You are an expert resume writer. Using the following resume template:
    {template}

    And the following job posting:
    {job_posting}

    Generate a personalized resume that is tailored to the job posting. Make sure to include relevant experience and skills from the job posting.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=800,
        temperature=0.7
    )

    return response.choices[0].text.strip()

def main():
    # File paths for the resume template and job posting
    resume_template_path = 'resume_template.docx'
    job_posting_path = 'job_posting.txt'

    # Read the template and job posting
    resume_template = read_docx(resume_template_path)
    job_posting = read_file(job_posting_path)

    # Generate resume using the OpenAI API
    generated_resume = generate_resume(resume_template, job_posting)

    # Save the generated resume to a new file
    with open('generated_resume.txt', 'w', encoding='utf-8') as file:
        file.write(generated_resume)

    print("Resume generated successfully and saved to 'generated_resume.txt'")

if __name__ == "__main__":
    main()
