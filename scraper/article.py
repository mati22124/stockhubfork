from chatgpt import *
from sentimentAnalyze import *
from urlFinder import *
from websiteFuncs import *


title,content = bbcScrapper("https://www.bbc.com/news/technology-67794645")
summary = summarize_text(content)
print(f"Summarized Text: {summary}")
print("positivity:")
print((sentiment_analyzer(summary)['compound'] + 1)/2)