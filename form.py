import os
from docx import Document
from datetime import datetime

def create_application_letter(data):
    template_path = './templates.docx'

    with open(template_path, 'rb') as file:
        doc = Document(file)

        for paragraph in doc.paragraphs:
            for run in paragraph.runs:
                text = run.text
                for key, value in data.items():
                    placeholder = f"{{{{{key}}}}}"
                    text = text.replace(placeholder, str(value))
                run.text = text

        # Save the modified document
        output_filename = f'application_letter_{datetime.now().strftime("%Y%m%d_%H%M%S")}.docx'
        doc.save(output_filename)
        print(f"Application letter created: {output_filename}")

# Example usage:
applicant_data = {
    'YourName': 'John Doe',
    'Position': 'Software Engineer',
    'YourAddress': '123 Main St, Cityville, State',
    'Date': datetime.now().strftime("%B %d, %Y")
}

create_application_letter(applicant_data)
