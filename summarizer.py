import os
from urllib import response 
from google import genai
from dotenv import load_dotenv

load_dotenv()
client=genai.Client()

def summarize_document(input_filename,output_filename):
    try:
        with open(input_filename,'r',encoding='utf-8') as file:
            document_text=file.read()


        prompt = f"Summarize the following text into exactly 3 key bullet points:\n{document_text}"

        response=client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        with open(output_filename,'w',encoding='utf-8') as file:
            file.write(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    summarize_document('sample.txt', 'summary.txt')