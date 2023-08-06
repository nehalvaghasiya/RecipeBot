import uuid
import streamlit as st
from streamlit_chat import message
from utils import get_completion
from config import Parameters
import json
import re

class RecipeBot:
    """
    Class representing the Recipe chatbot.
    """

    def __init__(self) -> None:
        self.prompts = [
            "Can you tell me if you have any dietary restrictions or preferences?",
            "What kind of cuisine are you interested in today?",
            "Do you have any specific ingredients you'd like to use or avoid?",
            "Are you looking for a quick meal or something more elaborate?",
            "Do you have any specific nutritional needs or goals, such as low-carb, high-protein, etc.?",
            "Would you like a side dish, beverage, or dessert recommendation to accompany the main course?"
        ]

        if 'answers' not in st.session_state:
            st.session_state['answers'] = []
        
        if 'recipe_step' not in st.session_state:
            st.session_state['recipe_step'] = 0

        self.session_state = st.session_state
        self.session_state['questions'] = [(question, self._generate_uuid()) for question in self.prompts]

    def ask_question(self) -> None:
        text, key = self.session_state['questions'][self.session_state['recipe_step']]
        message(text, key=key)
        # message(self.prompts[self.session_state['recipe_step']])

    def get_answer(self) -> None:
        answer = st.text_input("Your answer:", key="input" + str(self.session_state['recipe_step']))

        if answer:
            self.session_state['answers'].append((answer, self._generate_uuid()))
            self.session_state['recipe_step'] += 1
            st.experimental_rerun()

    def display_past_questions_and_answers(self) -> None:
        for i in range(self.session_state['recipe_step']):
            question_text, question_key = self.session_state['questions'][i]
            message(question_text, key=question_key)

            if i < len(self.session_state['answers']):
                answer_text, answer_key = self.session_state['answers'][i]
                message(answer_text, is_user=True, key=answer_key)

    def user_preference(self) -> str:
        user_prefs = "".join([f"Question: {question}\nAnswer: {answer}\n" for (question, _), (answer, _) in zip(self.session_state['questions'], self.session_state['answers'])])
        return user_prefs

    def generate_recipe(self) -> str:
        response = get_completion(Parameters.RECIPE_GENERATOR_PROMPT.format(user_prefs=self.user_preference()))  
        return response

    def evaluate_potential_bias(self) -> str:
        evaluation_prompt = Parameters.EVALUATION_PROMPT.format(user_prefs=self.user_preference(), generated_recipe= self.generate_recipe())
        response = get_completion(evaluation_prompt)
        print(response)
        return response
    

    def performance_metrics(self) -> str:
        performance_prompt = Parameters.PERFORMANCE_PROMPT.format(user_prefs=self.user_preference(), generated_recipe= self.generate_recipe())
        result = get_completion(performance_prompt)
        return result

    def execute_recipe_generation(self) -> None:
        self.display_past_questions_and_answers()

        if self.session_state['recipe_step'] < len(self.prompts):
            self.ask_question()
            self.get_answer()

        elif self.session_state['recipe_step'] == len(self.prompts):
            recipe = self.generate_recipe()
            st.markdown(f"<b>Here's a recipe for you based on your preferences:</b>\n {recipe}", unsafe_allow_html=True)
            # st.write(f"**Here's a recipe for you based on your preferences:**\n {recipe}")
            print("-------------------------------------------------------------------------------------")
            evaluation = self.evaluate_potential_bias()
            st.markdown(f"<b>Evaluation of potential biases:</b>\n {evaluation}", unsafe_allow_html=True)
            # st.write(f"**Evaluation of potential biases:**\n {evaluation}")
            print("-------------------------------------------------------------------------------------")
            performance_metrics = self.performance_metrics()
            st.markdown(f"<b>Performance Metrics:</b>\n {performance_metrics}", unsafe_allow_html=True)
            # st.write(f"**Performance Metrics:**\n {performance_metrics}")
            self.session_state['recipe_step'] += 1

    @staticmethod
    def _generate_uuid() -> str:
        return str(uuid.uuid4())


def create_bot() -> None:
    bot = RecipeBot()
    bot.execute_recipe_generation()


st.title("RecipeBot - AI Recipe Generation Chatbot")
create_bot()
