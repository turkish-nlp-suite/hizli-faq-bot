import spacy
import whoosh.index as index
from whoosh.qparser import QueryParser
from whoosh import scoring

nlp = spacy.load("tr_core_news_trf")
indexdir = "index"

def lemmatize_sentence(sent):
  doc = nlp(sent)
  nouns = [token  for token in doc if token.pos_ in ["NOUN", "PROPN"]]
  noun_lemmas = [(token.lemma_.lower() if token.lemma_ else token.text.lower()) for token in nouns]
  all_lemmas = " ".join(noun_lemmas).strip()
  return all_lemmas



ix = index.open_dir(indexdir)

'''
with ix.searcher() as searcher:
    print(list(searcher.lexicon("question")))
'''

query0 = "Mortgage faiz oranı ne kadar?"
query1 = "Mortgage faizleri ne kadar?"
query3 = "Kimler mortgage kredisi alabilir?"
query4 = "Ev kredisi faizleri ne kadar?"
query5 = "İhtiyaç kredisini ne kadar vadeyle alabilirim?"
query6 = "İhtiyaç kredisini en fazla kaç aylık çekebilirim?"
query7 = "Taşıt kredisi için gerekli belgeler neler?"
query8 = "Taşıt kredisine nasıl başvurabilirim?"
query9 = "Taşıt kredisi nasıl çekebilirim?"
query10 = "Taşıt kredisi için gerekli evrak?"
lemmatized_query = lemmatize_sentence(query6)
print("lemmatized: ", lemmatized_query)

qp = QueryParser("question", schema=ix.schema)
q = qp.parse(lemmatized_query)

with ix.searcher() as searcher:
    results = searcher.search(q)
    print(results[0])



