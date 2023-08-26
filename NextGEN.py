import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import spacy

# Load NLP models and download necessary resources
nlp = spacy.load("en_core_web_sm")
nltk.download("vader_lexicon")

# Define categories and phrases here
categories_phrases = {
     0: [
        "Saying negative thoughts about yourself won't make you feel better. It will ruin your friendship, relationship and love.",
        "I am sorry to hear that. But I can help.",
        "I am sorry, is there anything I can help with?",
        "I am sorry that you are feeling down. How can I make you feel up?",
        "Feel better and follow dreams. Those who make fun of you have no talent."
    ],
    1: [
        "I see that your friendship with the person you're talking about is strained. I'm here to offer support.",
        "I'm sorry to hear about your relationship. Can I assist you in any way?",
        "Harmful behavior can be damaging to both parties. Let's find a way to address this.",
        "Conflict and aggression can create negative outcomes. Let's work together to find resolution."
    ],
    2: [
        "Urgent situation? I'm here to help. Please let me know what you need.",
        "If you need immediate assistance, don't hesitate to reach out. I'm here for you.",
        "In a critical situation, it's important to get help quickly. What can I do for you?"
    ],
    3: [
        "Need a laugh? Here's a joke for you: Why don't scientists trust atoms? Because they make up everything!",
        "Laughter is the best medicine. How about a funny story to brighten your day?",
        "Sometimes, humor is all we need to lighten the mood. What makes you laugh?"
    ],
    4: [
        "Communication is key in any relationship. Have you considered sending them a message to clear things up?",
        "An email might be a great way to express your thoughts. Want help composing one?",
        "Inbox full? Let's organize your messages to make communication easier."
    ],
    5: [
        "Writing an essay can be daunting. Take it one step at a time and you'll do great!",
        "If you need help with your composition, I'm here to assist. What's the topic?",
        "Elaborate explanations can be difficult. Let's break it down into manageable parts."
    ],
    6: [
        "Want to play a game? Let's have some virtual fun!",
        "Entertainment is a great way to relax. How about trying out a new game?",
        "Recreation is important for a balanced life. Let's explore some game options!"
    ],
    7: [
        "Sometimes, nonsense words can bring a smile to your face. Try saying 'gibberish' out loud!",
        "Random words can lead to unexpected conversations. Give it a shot!",
        "Non sequiturs can be surprisingly entertaining. Share one with me!"
    ],
    8: [
        "Math problems might seem challenging, but with practice, you'll master them!",
        "Equations and numbers can be puzzling, but they follow logical rules. Want to work on some together?",
        "Geometry can be fascinating once you understand its concepts. Let's dive into some geometry problems!"
    ],
    9: [
        "Hello! How can I assist you today?",
        "Hi there! Is there something on your mind?",
        "Greetings! I'm here to help with anything you need.",
        "Hey there! How can I make your day better?",
        "How are you feeling? Let's chat!"
    ],
    10: [
        "Staying informed is important. Here's the latest news:",
        "Curious about current events? Let me share some updates with you:",
        "Stay up to date with the latest information:",
        "Want to know about recent developments? Here's the scoop:"
    ],
    # Add more categories and phrases here
}

def classify_category(input_text):
  doc = nlp(input_text)
  input_tokens = [token.text for token in doc]
    
max_similarity = 0
best_category = None
    
def new_func(best_category):
    return best_category

for category, phrases in categories_phrases.items():
        for phrase in phrases:
            phrase_doc = nlp(phrase)
            similarity = doc.similarity(phrase_doc)
            if similarity > max_similarity:
                max_similarity = similarity
                best_category = category
                return new_func(best_category)

def classify_sentiment(input_text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(input_text)["compound"]

    if sentiment_score > 0.2:
        return "positive"
    elif sentiment_score < -0.2:
        return "negative"
    else:
        return "neutral"


def generate_response(input_sentiment, category):
    phrases = categories_phrases.get(category, [])
    
    if phrases:
        return random.choice(phrases)
    else:
        return "No matching response available."


def handle_user_input(input_text, input_sentiment, category):
    # Check for user commands and provide corresponding responses
    if "my name is" in input_text:
        user_name = input_text.split("is")[1].strip()
        with open("memory.txt", "a") as memory_file:
            memory_file.write(f"Name: {user_name}\n")
        return f"Hi {user_name}, nice to meet you!"

    if any(command in input_text.lower() for command in ["tell me a joke", "say a joke", "share a joke"]):
        category = 3  # Joke category
        response = generate_response(input_sentiment, category)
        return response

    if "i have an emergency" in input_text:
        category = 2  # Emergency category
        response = generate_response(input_sentiment, category)
        return response

    # If the sentiment is negative and the category is other-harm, provide a supportive response
    if input_sentiment == "negative" and category == 1:  # other-harm category
        person_name = "John"  # Replace with the actual name mentioned in the user's input
        response = f"I know that {person_name} is your enemy, but I am here to help."
        return response

    # Default behavior: Generate a response based on sentiment and category
    response = generate_response(input_sentiment, category)
    return response

    # Check for joke commands
    joke_commands = ["tell me a joke", "say a joke", "share a joke"]
    for command in joke_commands:
        if command in input_text.lower():
            category = 3  # Joke category
            response = generate_response(input_sentiment, category)
            return response

    # ...

# Start the chat loop
while True:
    input_text = input("You: ")
    input_sentiment = classify_sentiment(input_text)
    category = classify_category(input_text)
    response = handle_user_input(input_text, input_sentiment, category)

    print("AI:", response)
    print("--------------------")
