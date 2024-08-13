from snownlp import SnowNLP

def analyze_sentiment(text):
    s = SnowNLP(text)
    return s.sentiments
