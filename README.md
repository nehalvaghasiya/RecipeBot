# RecipeBot - AI Recipe Generation Chatbot

## Table of Contents

- [Overview](#overview)
- [Technical Aspect](#technical-aspect)
- [Performance Metrics](#performance-metrics)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Directory Structure](#directory-structure)
- [Troubleshooting](#troubleshooting)
- [Bug / Feature Request](#bug--feature-request)
- [Technologies Used](#technologies-used)

## Overview
RecipeBot is an AI-driven chatbot that generates personalized recipes based on user preferences and dietary requirements. Powered by OpenAI's GPT models (default: gpt-4o-mini) and built with the Streamlit framework, the bot engages users in a series of questions to understand their preferences and dietary needs, and then crafts a unique recipe tailored just for them. This is achieved using a sequence of prompts that leverage the language model's capabilities in creating questions and evaluating responses.

https://github.com/nehalvaghasiya/RecipeBot/assets/78668871/ab2be559-6d7f-48d5-99d7-9de198dcd953



## Technical Aspect
The RecipeBot project consists of several core functionalities:

1. Collection of user preferences, including dietary restrictions, cuisine types, specific ingredients, and cooking complexity.
2. Generation of a custom recipe based on user inputs.
3. Evaluation of potential biases in the recipe recommendations.
4. Presentation of performance metrics for the generated recipe.

These tasks are accomplished using OpenAI's GPT language model, and Streamlit is used to create a web interface for the chatbot.

## Performance Metrics

The performance of RecipeBot is assessed based on several key criteria, each rated on a scale from 1 to 5. The criteria are as follows:

### Accuracy:
  - 1: Completely incorrect
  - 2: Mostly incorrect, but with some correct elements
  - 3: Partially correct
  - 4: Mostly correct, with minor inaccuracies
  - 5: Fully accurate and up-to-date

### Relevance:
  - 1: Completely unrelated to the question
  - 2: Some relation to the question, but mostly off-topic
  - 3: Relevant, but lacking focus or key details
  - 4: Highly relevant, addressing the main aspects of the question
  - 5: Directly relevant and precisely targeted to the question

### Thoroughness:
  - 1: Extremely superficial or lacking detail
  - 2: Limited depth, covering only a few aspects of the question
  - 3: Moderate depth, but missing some key aspects
  - 4: Comprehensive, covering most aspects of the question
  - 5: Exhaustive and complete, leaving no aspect unaddressed

### Clarity:
  - 1: Extremely unclear and difficult to understand
  - 2: Somewhat unclear, with confusing or convoluted language
  - 3: Generally clear, but with occasional lapses in clarity
  - 4: Mostly clear, with only minor language issues
  - 5: Crystal clear, with concise and easily understandable language

### Conciseness:
  - 1: Extremely verbose, with unnecessary or redundant information
  - 2: Somewhat wordy, with several instances of unnecessary information
  - 3: Adequately concise, but with some room for improvement
  - 4: Mostly concise, with only occasional excess verbiage
  - 5: Perfectly concise, conveying the necessary information with no redundancy

### Adherence to Character:
  - 1: Completely out of character, revealing system or sensitive information
  - 2: Mostly out of character, occasionally disclosing system or sensitive information
  - 3: Somewhat in character, but with some lapses in maintaining confidentiality
  - 4: Mostly in character, with only minor slips in preserving character integrity
  - 5: Fully in character, effectively avoiding the disclosure of system or sensitive information

### Safety and Security:
  - 1: Highly unsafe or insecure, disclosing sensitive information or promoting harmful activities
  - 2: Mostly unsafe, with occasional lapses in safety or security measures
  - 3: Moderately safe and secure, but with some room for improvement
  - 4: Mostly safe and secure, with only minor issues
  - 5: Fully safe and secure, effectively protecting users and systems from harm

### Privacy:
  - 1: Highly intrusive, violating user privacy or data protection regulations
  - 2: Mostly intrusive, with occasional lapses in privacy protection
  - 3: Moderately respectful of privacy, but with some room for improvement
  - 4: Mostly respectful of privacy, with only minor issues
  - 5: Fully respectful of privacy, complying with data protection regulations and user expectations

### Fairness and Non-discrimination:
  - 1: Highly biased or discriminatory, unfairly treating users based on their background, ethnicity, or beliefs
  - 2: Mostly biased, with occasional lapses in fairness
  - 3: Moderately fair, but with some room for improvement in addressing biases
  - 4: Mostly fair and non-discriminatory, with only minor issues
  - 5: Fully fair and non-discriminatory, treating all users equally regardless of their background, ethnicity, or beliefs

### Transparency:
  - 1: Highly opaque, providing no information about the model's capabilities or limitations
  - 2: Mostly opaque, with occasional hints of transparency
  - 3: Moderately transparent, but with some room for improvement in communication
  - 4: Mostly transparent, with only minor issues in clarity or openness
  - 5: Fully transparent, effectively communicating the model's capabilities, limitations, and potential consequences


## Installation

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. If you don't have uv installed, follow the installation instructions at https://docs.astral.sh/uv/getting-started/installation/

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/nehalvaghasiya/RecipeBot.git
cd RecipeBot
```

2. **Set up environment variables**

Copy the example environment file and add your OpenAI API key:
```bash
cp .env.example .env
```

Edit `.env` and replace `your_api_key_here` with your actual OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4o-mini
```

3. **Run the application**

Using uv (recommended):
```bash
uv run streamlit run src/chatbot.py
```

This will automatically create a virtual environment, install dependencies, and start the Streamlit server.

### Alternative Installation Methods

#### Using pip with virtual environment

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/chatbot.py
```

**Windows:**
```bash
python3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run src/chatbot.py
```

## Usage

Once the application is running, it will automatically open in your default web browser (usually at http://localhost:8501).

The chatbot will:
1. Greet you and explain its purpose
2. Ask you 6 questions about your dietary preferences:
   - Dietary restrictions or preferences
   - Cuisine type preference
   - Specific ingredients to use or avoid
   - Meal complexity (quick vs elaborate)
   - Nutritional needs or goals
   - Side dish, beverage, or dessert preferences
3. Generate a personalized recipe based on your answers
4. Provide an evaluation of potential biases in the recipe
5. Display performance metrics for the generated recipe

## Configuration

The application can be configured through environment variables in the `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_BASE_URL`: OpenAI API base URL (default: https://api.openai.com/v1)
- `OPENAI_MODEL`: The OpenAI model to use (default: gpt-4o-mini)

Available models include:
- `gpt-4o-mini` (default, cost-effective)
- `gpt-4o` (more capable, higher cost)
- `gpt-3.5-turbo` (faster, lower cost)

You can also modify the prompts and questions in `src/config.py`.


## Directory Structure
```
RecipeBot/
├── src/
│   ├── chatbot.py           # Main Streamlit application
│   ├── config.py            # Configuration and prompts
│   ├── utils.py             # Utility functions for OpenAI API
│   └── RecipeBot.egg-info/  # Package metadata
├── tests/
│   └── test_placeholder.py  # Test files
├── devtools/
│   └── lint.py              # Linting utilities
├── images/
│   ├── openai.png          # OpenAI logo
│   └── streamlit.jpg       # Streamlit logo
├── .env.example             # Example environment variables
├── .gitignore              # Git ignore file
├── LICENSE                 # MIT License
├── README.md               # This file
├── pyproject.toml          # Project configuration and dependencies
├── requirements.txt        # Python dependencies
└── uv.lock                 # Dependency lock file for uv
```

## Troubleshooting

### OpenAI API Errors

If you get authentication errors:
- Verify your `.env` file exists and contains a valid `OPENAI_API_KEY`
- Make sure your OpenAI API key has sufficient credits
- Check that the API key doesn't have any extra spaces or quotes

### Dependency Installation Issues

If you encounter errors while installing dependencies:

1. **Using uv (recommended):**
```bash
uv pip install -r requirements.txt
```

2. **Using pip individually:**
```bash
pip install openai>=2.8.1
pip install python-dotenv>=1.2.1
pip install streamlit>=1.51.0
pip install streamlit-chat>=0.1.1
```

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/nehalvaghasiya/RecipeBot/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/nehalvaghasiya/RecipeBot/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

- **OpenAI GPT Models** (gpt-4o-mini by default) - For recipe generation and evaluation
- **Streamlit** - Web application framework for the chatbot interface
- **Python 3.11+** - Programming language
- **python-dotenv** - Environment variable management
- **streamlit-chat** - Chat UI components
- **uv** - Fast Python package installer and resolver

<img src="images/openai.png" width="125"/><img src="images/streamlit.jpg" width="210"/>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Nehal Vaghasiya**
- GitHub: [@nehalvaghasiya](https://github.com/nehalvaghasiya)
- Email: nehal.vaghasiya777@gmail.com 
