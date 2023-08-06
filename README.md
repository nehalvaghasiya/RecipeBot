# RecipeBot - AI Recipe Generation Chatbot
## Table of Content

- Overview
- Technical Aspect
- Installation
- Troubleshooting
- Directory Tree
- Bug / Feature Request
- Technologies Used

## Overview
RecipeBot is an AI-driven chatbot that generates personalized recipes based on user preferences and dietary requirements. Powered by OpenAI's GPT and built with the Streamlit framework, the bot engages users in a series of questions to understand their preferences and dietary needs, and then crafts a unique recipe tailored just for them. This is achieved using a sequence of prompts that leverage the language model's capabilities in creating questions and evaluating responses.



## Technical Aspect
The RecipeBot project consists of several core functionalities:

1. Collection of user preferences, including dietary restrictions, cuisine types, specific ingredients, and cooking complexity.
2. Generation of a custom recipe based on user inputs.
3. Evaluation of potential biases in the recipe recommendations.
4. Presentation of performance metrics for the generated recipe.

These tasks are accomplished using OpenAI's GPT language model, and Streamlit is used to create a web interface for the chatbot.

## Installation

The installation steps are different for different OS.

### Linux:

```bash
python3.8 --version
apt install python3.8-venv
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```

### Windows:

```bash
python3.8 -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```

### Mac:

```bash
python3.8 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```

Remember to replace `<your secret key>` with your actual OpenAI API Key.


## Troubleshooting

If you encounter errors while installing the dependencies from `requirements.txt`, try installing the packages individually using the following commands:

```bash
pip install openai
pip install streamlit
pip install streamlit-chat
```

Then, export your OpenAI API Key and run the chatbot:
```bash
export OPENAI_API_KEY=<your secret key>
streamlit run chatbot.py
```
Remember to replace `<your secret key>` with your actual OpenAI API Key.


## Directory Tree
```
├── images
│   ├── openai.png
│   ├── streamlit.jpg
├── .gitignore
├── chatbot.py
├── config.py
├── utils.py
├── requirements.txt
└── README.md
```

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/RecipeBot/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/RecipeBot/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

<img src="images/openai.png" width="125"/><img src="images/streamlit.jpg" width="210"/> 
