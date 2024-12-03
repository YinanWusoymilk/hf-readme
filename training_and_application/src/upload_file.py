import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
response = openai.files.create(
  file=open("readme_sections_with_chat_format.jsonl", "rb"),
  purpose="fine-tune"
)

print(response.id)


response = openai.fine_tuning.jobs.create(
  training_file= response.id, 
  model="gpt-4o-2024-08-06"
)
