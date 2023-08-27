# 1.py - Sentiment Analysis

from textblob import TextBlob

def get_sentiment(input_text):
    analysis = TextBlob(input_text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

user_input = input("Enter a sentence: ")
sentiment = get_sentiment(user_input)
print(f"Sentiment: {sentiment}")
