# chat.py - Main Script with Similarity System

import json
from importlib import import_module
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define predefined phrases or prompts
predefined_phrases = [
    "hello",
    "how are you?",
    "what's the weather like?",
    "tell me a joke",
    # Add more prompts here
]

def get_most_similar_phrase(user_input, predefined_phrases):
    all_text = predefined_phrases + [user_input]
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)
    
    cosine_sim = cosine_similarity(tfidf_matrix)
    most_similar_index = cosine_sim[-1].argsort()[-2]
    
    return predefined_phrases[most_similar_index]

def main():
    user_input = input("Enter a sentence: ")
    
    # Get the most similar predefined phrase
    most_similar_phrase = get_most_similar_phrase(user_input, predefined_phrases)
    
    # Import the other scripts as modules
    script1 = import_module("1")
    script2 = import_module("2")
    script3 = import_module("3")
    script4 = import_module("4")
    script5 = import_module("5")
    
    # Run the functions from the scripts
    sentiment = script1.get_sentiment(user_input)
    topic = script2.classify_topic(user_input)
    response = script3.generate_topic_response(sentiment, topic)
    combined_response = script4.combine_responses(response, response)
    
    # Update memory
    memory = script5.update_memory({}, user_input, combined_response)
    script5.save_memory_to_json(memory)
    
    print(f"Most similar phrase: {most_similar_phrase}")
    print(f"Topic: {topic}\nOutput: {combined_response}")
    print("Memory:", memory)

if __name__ == "__main__":
    main()
