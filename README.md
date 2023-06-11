# PythonGPT | Dynamic Programming with LLMs | 💻🐚📝
PythonGPT implements a generative language model powered shell using Python. When run, the script is capable of writing Python to accomplish various tasks. 

PythonGPT will eventually integrate with [DoctorGPT](https://github.com/FeatureBaseDB/DoctorGPT) for access to relevant documents when needed. 

## Disclaimer
Before you do anything else, please review the [disclaimer](https://github.com/FeatureBaseDB/PythonGPT/blob/main/DISCLAIMER.md). Use of this project without accepting the terms of the disclaimer is strictly prohibited.

## Example
Here's an example of what PythonGPT can do:

```
spiffy-malamute[python3]> draw a cow in ascii
system> Calling GPTChat for code...please wait.
system> Showing code...
print(r'''
       ____
   (  /     \_)
    \(o)____(o)/
       ~~   ~~
''')

system> Running code...

       ____
   (  /     \_)
    \(o)____(o)/
       ~~   ~~

system> This code prints a cow using escape sequences and the backslash (\) to represent the cow in ASCII art.
```

The repository uses tools such as [Weaviate](https://weaviate.io/) for dense vector search and embedding handling, and [FeatureBase](https://featurebase.com/) for back of the book indexing and graph traversal of terms, questions and document fragments.

The project is installed, configured and run locally from the command line. You will need a [Google Cloud](https://cloud.google.com/) account with [Vision enabled](https://cloud.google.com/vision/docs/before-you-begin), an [OpenAI account](https://openai.com), a [FeatureBase cloud](https://cloud.featurebase.com) account and a [Weaviate cloud](https://console.weaviate.cloud/) account to run the code.

## Theory of Operation
This project asks ChatGPT to write Python, then executes that Python with the [exec()](https://docs.python.org/3/library/functions.html#exec) function. Additionally:

1. User entry is managed by a simple Python powered shell. History of entries is saved in a file for recall.
2. Entries are also stored in Weaviate and FeatureBase. Entries and the generated code is analyzed for keyterms.
3. Subsequent queries create searches against the graph stored in FeatureBase and the embeddings (vectors) in Weaviate.
4. Results are used to create dynamic prompts. This allows the LLM to reference previously generated functions.

Future work:

1. Add functionality to allow the user to save the Python written by the LLM to disk.
2. Add functionality to integrate with DoctorGPT to allow the LLM to reference advanced Python use, or other knowledge.
3. Add functionality to dynamically alter the shell experience using generative plugins.

## Install Instructions
Eensure you follow these instructions carefully. It is suggested you use [ChatGPT](https://chat.openai.com/) to assist you with any errors. Simply paste in the entire content of this README into ChatGPT before asking your question about the install process.

### Checkout the Code
To check out the code from Github, run the following command from a terminal window (we recommend using [GitBash](https://git-scm.com/downloads) on Windows to do this step):

`git clone https://github.com/FeatureBaseDB/PythonGPT.git`

Change into the directory to prepare for installing the packages required to run the project:

`cd ~/<path_to_code>/PythonGPT`

On Windows, you'll want to do this last part in Powershell.

### Create a Config File
Copy the `config.py.example` file to `config.py`. Use this file to store the various strings and tokens for the services utilized by this project.

### Cloud Setup
To use Weaviate and FeatureBase with DoctorGPT, you will need to signup for their free cloud offerings. Follow the instructions below to get started.

#### Weaviate Cloud
Go to [Weaviate Cloud](https://console.weaviate.cloud/dashboard) and sign up for an account.

After signup, navigate to the dashboard. Click on the "Create Cluster" button to create a new cluster. Name the cluster and ensure authentication is enabled.

After the cluster is created, click on "Details" and click on the cluster URL to copy the cluster address. Paste this address into the value for the `weaviate_cluster` variable in the config file.

Next, click on the key next to "Enabled Authentication" to copy the Weaviate token. Paste this into the config file for the `weaviate_token` variable.

Your Weaviate Cloud config will be complete. This sandbox cluster will expire in 14 days.

#### FeatureBase Cloud
Go to [FeatureBase Cloud](https://cloud.featurebase.com/) and sign up for an account.

Once you have signed up, you will be taken to the dashboard. Click on "Databases" to the left. Click on "NEW DATABASE". Select the 8GB database option and create the database, naming it `python_gpt`

On the Databases page, click on your new database. Copy the `Query endpoint` by clicking on the URL. Paste the URL into the `config.py` file mentioned above and DELETE the `/query/sql` path on the end, leaving a URL without a `/` on the end. It should look something like this:

```
# featurebase
featurebase_endpoint = "https://query.featurebase.com/v2/databases/d071c1e12-9dfc-41af-9103-d071c1e12"
```

Next, click on `configuration` in the left panel, then `Manage API Keys`. Click `Create a Key`, name the key, and click `Create`. Copy the `secret` key token shown. 

Place this token in the `config.py` file under the `featurebase_token` variable.

### OpenAI Auth
Go to [OpenAI](https://openai.com/) and signup or login. Navigate to the [getting started page](https://platform.openai.com/) and click on your user profile at the top right. 

Select "view API keys" and then create a new API key. Copy this key and put it in the `config.py` file under the `openai_token` variable.

### Install Requirements
There are a few packages used for this project that are required for execution. You may inspect the packages by looking at the `requirements.txt` file in the root directory of the project.

To install the required packages, ensure you have Python 3.10.11 or greater installed. It may be possible to use a lower version of Python, but this package has only been tested on Python 3.10.x, so your mileage may vary. It is left up to the user to determine the best way to update Python, but you may want to ask [ChatGTP](https://chat.openai.com) about it.

Run the following to install the required packages, use the `pip` package for Python:

`pip install -r requirements.txt`

### Interact with the PythonGPT
To begin using the language model shell, enter the following:

```
python doc_code.py
```

History is accessible by hitting the up and down arrows at the prompt:

```
kord@bob PythonGPT $ python3 doc_code.py          
abiding-ape[python3]> draw a cow in ascii
```

Advanced interaction with the Internet and filesystem is posible:

```
abiding-ape[python3]> ping google 20 times and write the logs to a file
system> Calling GPTChat for code...please wait.
system> Showing code...
import os
import subprocess

with open("ping_logs.txt", "w") as f:
    for i in range(20):
        response = subprocess.getoutput("ping -c 1 google.com")
        f.write(f"Ping {i+1}:\n")
        f.write(response)
        f.write("\n\n")
    print("Ping logs saved to ping_logs.txt")

system> Running code...
Ping logs saved to ping_logs.txt
system> This code initiates a loop in which the computer sends 20 pings to Google. The computer stores the response from each ping in the file 'ping_logs.txt' using the Python modules 'os' and 'subprocess' to execute the ping commands.
```

Please open tickets for any issues you encounter and consider contributing to this repository with pull requests. It is only through open collaboration that the "existential threat" of Strong AI is mitigated.
