import spacy
from whoosh.index import create_in
from whoosh.fields import *

from  html_parser import extract_ques_and_answers

nlp = spacy.load("tr_core_news_trf")
kredi_html = "../data/kredi.html"
indexdir = "index"


def lemmatize_sentence(sent):
  doc = nlp(sent)
  nouns = [token  for token in doc if token.pos_ in ["NOUN", "PROPN"]]
  noun_lemmas = [(token.lemma_.lower() if token.lemma_ else token.text.lower()) for token in nouns]
  all_lemmas = " ".join(noun_lemmas).strip()
  return all_lemmas


def create_index(html_page):
  questions, answers = extract_ques_and_answers(kredi_html)
  schema = Schema(question=TEXT(stored=True), answer=TEXT(stored=True))
  ix = create_in(indexdir, schema)
  writer = ix.writer()

  for ques,ans in zip(questions, answers):
    lemmatized_ques = lemmatize_sentence(ques)
    print(lemmatized_ques, "//", ques)
    writer.add_document(question=lemmatized_ques, answer=ans)
  writer.commit()


create_index(kredi_html)




