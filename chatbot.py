import uuid
import streamlit as st
from streamlit_chat import message
from utils import get_completion
from config import Parameters


class RecipeBot:
    """
    Class representing the Recipe chatbot.
    """

    def __init__(self) -> None:
        self.initialize_session_state()
        self.session_state = st.session_state
        self.session_state['questions'] = [(question, self._generate_uuid()) for question in Parameters.PROMPTS]

    def initialize_session_state(self) -> None:
        """Initialize session state variables."""
        if 'answers' not in st.session_state:
            st.session_state['answers'] = []
        if 'recipe_step' not in st.session_state:
            st.session_state['recipe_step'] = 0

    def ask_question(self) -> None:
        """Display the next question to the user."""
        text, key = self.session_state['questions'][self.session_state['recipe_step']]
        message(text, key=key)

    def get_answer(self) -> None:
        """Get the answer from the user and update the session state."""
        answer = st.text_input("Your answer:", key="input" + str(self.session_state['recipe_step']))

        if answer:
            self.session_state['answers'].append((answer, self._generate_uuid()))
            self.session_state['recipe_step'] += 1
            st.experimental_rerun()

    def display_past_questions_and_answers(self) -> None:
        """Display previous questions and answers."""
        for i in range(self.session_state['recipe_step']):
            question_text, question_key = self.session_state['questions'][i]
            message(question_text, key=question_key)

            if i < len(self.session_state['answers']):
                answer_text, answer_key = self.session_state['answers'][i]
                message(answer_text, is_user=True, key=answer_key)

    def user_preference(self) -> str:
        """Compile user preferences from the answered questions."""
        user_prefs = "".join([f"Question: {question}\nAnswer: {answer}\n" for (question, _), (answer, _) in zip(self.session_state['questions'], self.session_state['answers'])])
        return user_prefs

    def generate_recipe(self) -> str:
        """Generate a recipe based on user preferences."""
        response = get_completion(Parameters.RECIPE_GENERATOR_PROMPT.format(user_prefs=self.user_preference()))  
        return response

    def evaluate_potential_bias(self) -> str:
        """Evaluate potential biases in the generated recipe."""
        evaluation_prompt = Parameters.EVALUATION_PROMPT.format(user_prefs=self.user_preference(), generated_recipe=self.generate_recipe())
        response = get_completion(evaluation_prompt)
        return response

    def performance_metrics(self) -> str:
        """Calculate performance metrics for the generated recipe."""
        performance_prompt = Parameters.PERFORMANCE_PROMPT.format(user_prefs=self.user_preference(), generated_recipe=self.generate_recipe())
        result = get_completion(performance_prompt)
        return result

    def execute_recipe_generation(self) -> None:
        """Main function to execute the recipe generation process."""
        self.display_past_questions_and_answers()

        if self.session_state['recipe_step'] < len(Parameters.PROMPTS):
            self.ask_question()
            self.get_answer()
        elif self.session_state['recipe_step'] == len(Parameters.PROMPTS):
            self.display_recipe_and_evaluation()
            self.session_state['recipe_step'] += 1

    def display_recipe_and_evaluation(self) -> None:
        """Generate and display the recipe along with bias evaluation and performance metrics."""
        # Generate the recipe
        recipe = self.generate_recipe()
        st.markdown(f"### Here's a recipe for you based on your preferences:\n{recipe}")

        # Evaluate potential biases
        evaluation = self.evaluate_potential_bias()
        st.markdown(f"### Evaluation of potential biases:\n{evaluation}")

        # Get the performance metrics
        performance_metrics = self.performance_metrics()
        st.markdown(f"### Performance Metrics:\n{performance_metrics}")

    @staticmethod
    def _generate_uuid() -> str:
        """Generate a unique identifier."""
        return str(uuid.uuid4())


def create_bot() -> None:
    """Create and execute the RecipeBot."""
    bot = RecipeBot()
    message("Hello! I'm your recipe assistant bot powered by OpenAI. I will ask you a few questions to understand your dietary preferences and needs. Let's get started.", key="greeting")
    bot.execute_recipe_generation()


st.title("RecipeBot - AI Recipe Generation Chatbot")
create_bot()