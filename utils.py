import openai
import re
from typing import List
from openai.error import InvalidRequestError
from config import Parameters

def get_completion(complete_prompt: str) -> str:
    """
    Send a message to the OpenAI API to get a response.
    """
    try:
        messages = [{"role": "user", "content": complete_prompt}]
        response = openai.ChatCompletion.create(model=Parameters.MODEL, messages=messages,
                                                temperature = 0)
        return response.choices[0].message["content"]
    
    except InvalidRequestError as e:
        print(f"Encountered an error: {e}")
        return "Error: Input too long for model."
    

# User preferences:
# Question: Can you tell me if you have any dietary restrictions or preferences?
# Answer: Vegan 
# Question: What kind of cuisine are you interested in today?
# Answer: Indian cuisine
# Question: Do you have any specific ingredients you'd like to use or avoid?
# Answer: I would prefer tomatoes and garlic as special ingredients and I would like to avoid dairy products.
# Question: Are you looking for a quick meal or something more elaborate?
# Answer: QUick meal
# Question: Do you have any specific nutritional needs or goals, such as low-carb, high-protein, etc.?
# Answer: Low carbs and High protein
# Question: Would you like a side dish, beverage, or dessert recommendation to accompany the main course?
# Answer: Peanut butter cookies
