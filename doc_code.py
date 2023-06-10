import weaviate
import config
import pprint
import sys
import json
import os
import time
import random
import traceback

from lib.util import random_string, get_username

from lib.database import weaviate_schema, weaviate_query, weaviate_update, weaviate_object, featurebase_query
from lib.ai import ai

from coolname import generate_slug

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

# user
username = get_username()

# create Weaviate schema
weaviate_schema = weaviate_schema("Code")

# get files to process
filename = "python.pdf"

def go_weaviate(question, filename="", move_tos=[], num_results=20):
	start_time = time.time()
	# lookup matches from weaviate's QandAs
	weaviate_results = weaviate_query([question], "PDFs", ["filename", "page_id", "fragment"], move_tos=move_tos, filename=filename, num_results=num_results)

	end_time = time.time()
	elapsed_time = end_time - start_time
	print("system> Queried Weaviate for questions in:", elapsed_time, "seconds")
	print("system> %s results found." % len(weaviate_results))
	# print(weaviate_results[0])
	# print(weaviate_results[0].get('fragment'))
	return weaviate_results

# build history and session
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory

history = FileHistory(".DoctorGPT")
session = PromptSession(history=history)

while True:
	# get a query from the user

	# TODO
	# 1. write code fragments into weaviate and featurebase for prompt assembly (to help write more complicated code)
	# 2. call the AI model for extracting keyterms and insert into featurebase, along with the code
	# 3. describe what the code does so we can better search for it later using keyterms

	try:
		question = session.prompt("%s[%s]> " % (username, "python3"))

	except KeyboardInterrupt:
		print("system>", random.choice(["Bye!", "Later!", "Nice working with you."]))
		sys.exit()

	# build the document for the AI calls
	move_tos = ['python3']
	document = {"question": question, "text": "print('hello world')", "keyterms": move_tos}

	# call the AI
	print("system> Calling GPTChat for code...please wait.")

	# we'll try up to 4 times to get GPTChat to write the code, passing failures in for correction
	for x in range(4):
		try:
			document = ai("ask_gptcode", document)
			answer = document['answer']
			if answer.find('```python') != -1:
				start_index = answer.find('```python') + len('```python')
				end_index = answer.find('```', start_index)
				code = answer[start_index:end_index]
			else:
				code = answer

			print("system> Showing code...")
			print(highlight(code, PythonLexer(), TerminalFormatter()))
			print("system> Running code...")
			exec(code)

			# get keyterms (and a related question)
			document_terms = {"code": code, "prompt": question}
			document_terms = ai("gpt_codeterms", document_terms)
			
			explanation = document_terms.get('explanation')
			if not explanation.endswith('.'):
				explanation += "."
			print("system>", explanation)
			
			break

		except Exception as e:
			traceback_str = traceback.format_exc()
			error_msg = str(e)
			print("system>", error_msg)
			print("system> Providing traceback to ChatGPT for correction...")
			document['text'] = code + "\n" + traceback_str + "\n" + error_msg + "\nRemember, we are using '''start_index = answer.find('```python') + len('```python')''' to detect code to run. Please follow that format.\n"
	else:
		print("system> Failed to compile a valid solution. Please provide one in a document and retry.")



