# docsum ![](https://github.com/angzla/docsum/workflows/tests/badge.svg)
Use an LLM to summarize a document on the command line. Uses groq and recursive summarization for bigger documents. Can summarize documents of all file types using fulltext. Due to fulltext's dependencies, this runs on Python 3.11.9

The following example summarizes the declaration of independence. You can upload other files in the same format to summarize. 
```
$ python3 docsum.py docs/declaration.txt
A long time ago, some people in America decided they wanted to be free. They were tired of being ruled by a king from a faraway land. The king was being mean and taking away their rights. The people wrote a special paper to say they were free and independent. They said they didn't want to be ruled by the king anymore. They promised to work together and take care of each other to make sure they stayed safe and happy. This paper is called the Declaration of Independence. It's like a big declaration that says, "We are free and we're going to make our own decisions!"
```
