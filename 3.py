# 3.py - Generate Topic Response

def generate_topic_response(sentiment, topic):
    responses = {
        "greetings": {
            "positive": "Hi!",
            "negative": "Hello...",
            "neutral": "Hello!"
        },
        # Add more topics and responses here
    }
    return responses.get(topic, {}).get(sentiment, "I'm not sure what you mean.")

user_sentiment = "neutral"  # Replace with actual sentiment
user_topic = "greetings"  # Replace with actual topic
response = generate_topic_response(user_sentiment, user_topic)
print(response)
