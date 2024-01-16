from openai import OpenAI
from websiteFuncs import *



title, article = cnnScrapper(url = "https://www.cnn.com/2024/01/15/politics/2024-curtain-raiser-iowa/index.html")
bbcTitle, bbcArticle = bbcScrapper(url = "https://www.bbc.com/news/business-67977967")

# Nick im at c2 but im just gonna be on 
# print(title)
# print(article)


def summarize_text(article):
  gpt_key = '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'
  
  client = OpenAI(api_key=gpt_key)
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": "Summize this article: " + article}
    ]
  )
  
  return completion.choices[0].message.content

# print(summize_text(article))

