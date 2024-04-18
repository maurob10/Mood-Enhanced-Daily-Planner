# Import necessary libraries
import spacy  # Import spaCy for NLP tasks
from tensorflow.keras.models import load_model  # Import load_model function from TensorFlow for loading pre-trained models

# Function to load the spaCy English language model, ensuring proper error handling
def load_spacy_model():
    """
    Load the spaCy English language model, handling the case where it might not be installed.
    """
    try:
        return spacy.load('en_core_web_sm')
    except Exception as e:
        print("An error occurred while loading the spaCy model:", e)
        print("Please ensure spaCy is installed and the English model (en_core_web_sm) is downloaded.")
        exit(1)  # Exit the program if the model can't be loaded.

# Load spaCy's English language model
nlp = load_spacy_model()

# Function to analyze mood from text
def analyze_mood(text):
    """
    Analyze the sentiment of the input text. Currently returns a placeholder sentiment.
    """
    # Preprocess text for sentiment analysis
    processed_text = nlp(text.lower())
    # Return "positive" if the word "happy" is in the text, otherwise "negative"
    return "positive" if any(word.text == 'happy' for word in processed_text) else "negative"

# Main function to run the daily planner
def daily_planner():
    """
    A simple mood-enhanced daily planner that suggests tasks based on user's mood from their input text.
    """
    print("Welcome to the Mood-Enhanced Daily Planner")
    print("Tell me how you're feeling or what's on your mind, and I'll suggest some activities for your day.")
    
    # User input about their day or feelings
    user_input = input("Enter your thoughts: ")
    
    # Analyze the mood of the user's input
    mood = analyze_mood(user_input)
    
    # Suggest activities based on the mood
    if mood == "positive":
        print("You seem to be in a good mood! Perhaps tackle a challenging task today or take some time for a creative activity.")
    else:
        print("It sounds like a calmer day might be best. Consider reading a book, meditating, or organizing your workspace.")

# Run the planner
if __name__ == "__main__":
    daily_planner()
