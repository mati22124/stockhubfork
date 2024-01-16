import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_analyzer(text):
  # Tokenize the text into sentences
  sentences = nltk.sent_tokenize(text)
  
  # Initialize the Sentiment Intensity Analyzer
  sid = SentimentIntensityAnalyzer()
  
  # Analyze sentiment for each sentence
  for sentence in sentences:
      # print(sentence)
      sentiment_scores = sid.polarity_scores(sentence)
      # print(sentiment_scores)
  
  # Aggregate sentiment scores for the entire article
  overall_sentiment = sid.polarity_scores(text)
  # print("\nOverall Sentiment:", overall_sentiment)
  return overall_sentiment


if __name__ == "__main__":
  print(sentiment_analyzer("Help people with terrible diseases")) 