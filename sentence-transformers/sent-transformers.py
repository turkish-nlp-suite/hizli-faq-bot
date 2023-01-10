from sentence_transformers import SentenceTransformer, util
import numpy as np

from  html_parser import extract_ques_and_answers

kredi_html = "../data/kredi.html"

embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')


questions, answers = extract_ques_and_answers(kredi_html)

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




top_k=3
corpus_embeddings = embedder.encode(questions, convert_to_tensor=True)

for query in allqs:
  query_embedding = embedder.encode(query, convert_to_tensor=True)
  hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=top_k)
  hit = hits[0]
  #print(hit)
  hit_id = hit[0]['corpus_id']
  sim_ques = questions[hit_id]
  print(query, sim_ques)






