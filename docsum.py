import os
from groq import Groq
import fulltext
import re
import time

def split_document_into_chunks(text):
    chunk_size = 15
    # Step 1: Split the text into sentences
    sentences = re.split(r'\n{2,}|(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    
    # Step 2: Split sentences into chunks of chunk_size sentences
    chunks = [' '.join(sentences[i:i + chunk_size]) 
              for i in range(0, len(sentences), chunk_size)]
    
    return chunks


def summarize_text(text, client):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    'role': 'system',
                    'content': 'Summarize the input text below. Limit the summary to 1 paragraph and use a 1st grade reading level.',
                },
                {
                    'role': 'user',
                    'content': text,
                }
            ],
            model="llama3-8b-8192",
        )
    except groq.InternalServerError:
         time.sleep(5)
    except (groq.BadRequestError, groq.RateLimitError):
         time.sleep(5)
         
    return chat_completion.choices[0].message.content


# parse command line args 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

print(f"args.filename={args.filename}")

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
	)

with open(args.filename, encoding='ISO-8859-1') as f: 
	text  = fulltext.get(f, name = args.filename)

def recursive_summarize(text, client, max_depth=5, delay=0, depth=0):
    if depth >= max_depth:
        return text

    chunks = split_document_into_chunks(text)
    print(len(chunks))
    summarized_chunks = []
    count = 0 

    for chunk in chunks:
        summary = summarize_text(chunk, client)
        summarized_chunks.append(summary)
        count += 1
        print(count)
        # time.sleep(delay)  # Delay to avoid sending too many requests at once

    combined_summary = ' '.join(summarized_chunks)
    
    # Recursively summarize the combined summary
    return recursive_summarize(combined_summary, client, max_depth, delay, depth + 1)

final_summary = recursive_summarize(text, client)

print("result", final_summary)
