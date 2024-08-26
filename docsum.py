import os
from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)

filename = 'docs/declaration'
with open(filename) as f: 
	text  = f.read()

chat_completion = client.chat.completions.create(
    messages=[
        {'role': 'system',
'content': 'Summarize the input text below. Limit the summary to 1 paragraph and use a 1st grade reading level.',},
{
            "role": "user",
            "content": text,
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)
