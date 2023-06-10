# PythonGPT | Dynamic Programming with LLMs | 💻💡
PythonGPT implements a generative language model powered shell using Python. When run, the script is capable of creating, writing and indexing Python to provide a dynamic coding experience for building language model applications.

PythonGPT will eventually integrate with [DoctorGPT](https://github.com/FeatureBaseDB/DoctorGPT) to provide dynamic calls for relevant documents when needed in a prompt. 

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

system> This code prints a cow using escape sequences, the backslash (\) character and the new line character (
) to represent the cow in ASCII art.
```

The repository uses tools such as [Weaviate](https://weaviate.io/) for dense vector search and embedding handling, and [FeatureBase](https://featurebase.com/) for back of the book indexing and graph traversal of terms, questions and document fragments.

The project is installed, configured and run locally from the command line. You will need a [Google Cloud](https://cloud.google.com/) account with [Vision enabled](https://cloud.google.com/vision/docs/before-you-begin), an [OpenAI account](https://openai.com), a [FeatureBase cloud](https://cloud.featurebase.com) account and a [Weaviate cloud](https://console.weaviate.cloud/) account to run the code.

## Theory of Operation
The process of indexing a document is divided into three main steps:


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

Once you have signed up, you will be taken to the dashboard. Click on "Databases" to the left. Click on "NEW DATABASE". Select the 8GB database option and create the database, naming it `doc_gpt`

On the Databases page, click on your new database. Copy the `Query endpoint` by clicking on the URL. Paste the URL into the `config.py` file mentioned above and DELETE the `/query/sql` path on the end, leaving a URL without a `/` on the end.

##### FeatureBase Token
Keeping in mind your username/password you used for FeatureBase, open a terminal and navigate into the repository's directory.

Run the following to obtain a token for FeatureBase:

`python fb_token.py`

You'll receive output that includes the FeatureBase token. Place this token in the `config.py` file under the `featurebase_token` variable.

*NOTE*: You may need to use `python3` instead of `python` on some Python installs.

## Continue Setup
You'll need to grab an auth token for GPT-X from OpenAI, and install the required packages for Python to run the code.

### OpenAI Auth
Go to [OpenAI](https://openai.com/) and signup or login. Navigate to the [getting started page](https://platform.openai.com/) and click on your user profile at the top right. 

Select "view API keys" and then create a new API key. Copy this key and put it in the `config.py` file under the `openai_token` variable.

### Install Requirements
There are many packages used for this project that are required for execution. You may inspect the packages by looking at the `requirements.txt` file in the root directory of the project.

To install the required packages, ensure you have Python 3.10.11 or greater installed. It may be possible to use a lower version of Python, but this package has only been tested on Python 3.10.x, so your mileage may vary. It is left up to the user to determine the best way to update Python, but you may want to ask [ChatGTP](https://chat.openai.com) about it.

Run the following to install the required packages, use the `pip` package for Python:

`pip install -r requirements.txt`

### Interact with the PythonGPT
This is the step we've all been waiting for. In this step, you will interact directly with the document in a chat. Please note, for this particular release, the system does not recall previous questions. This will be addressed in an updated version soon.

```
python doc_code.py
```



```
Documents Directory
===================
0. animate.pdf
Enter the number of the file to chat with: 0
Entering conversation with animate.pdf. Use ctrl-C to end interaction.
user-9l1s[animate.pdf]> What is the relation between imaginary quantities and the square root of -1?
bot> The quantity i is defined as the square root of -1, and any quantity except zero has two square roots, each the negative of the other, so it is with -1; and we thus get two quantities, i and -i. They are absolutely interchangeable.
```

Please open tickets for any issues you encounter and consider contributing to this repository with pull requests. It is only through open collaboration that the "existential threat" of Strong AI is mitigated.
