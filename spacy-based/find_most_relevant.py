import spacy
import numpy as np
from  html_parser import extract_ques_and_answers

nlp = spacy.load("tr_core_news_md")
kredi_html = "../data/kredi.html"
indexdir = "index"



questions, answers = extract_ques_and_answers(kredi_html)
all_ques = [nlp(question) for question in questions]

allqs = [
"Mortgage faiz oranı ne kadar?",
"Mortgage faizleri ne kadar?",
"Kimler mortgage kredisi alabilir?",
"Ev kredisi faizleri ne kadar?",
"İhtiyaç kredisini ne kadar vadeyle alabilirim?",
"İhtiyaç kredisini en fazla kaç aylık çekebilirim?",
"Taşıt kredisi için gerekli belgeler neler?",
"Taşıt kredisine nasıl başvurabilirim?",
"Taşıt kredisi nasıl çekebilirim?",
"Taşıt kredisi için gerekli evrak?",
]


for query in allqs:
  query = nlp(query)
  scores=[]
  for question in all_ques:
    semsimscore = query.similarity(question)
    scores.append(semsimscore)
  best_index = np.argmax(scores)
  best_match = questions[best_index]
  print(query, "//",  best_match)






