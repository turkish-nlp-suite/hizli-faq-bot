from bs4 import BeautifulSoup


def extract_text(html_page):
  html = open(html_page).read()
  soup = BeautifulSoup(html, 'lxml')

  lists = soup.find_all('body')
  for llist in lists:
    qList = llist.find_all('ul')
    ansList = llist.find_all(['ol', "p"])
  return qList, ansList


def clean_tags(text):
 tags = ["<ul>", "</ul>", "<li>", "</li>" , "<ol>", "</ol>", "<p>", "</p>"]
 for tag in tags:
     text = text.replace(tag, " ")
 text = " ".join(text.strip().split())
 return text


def find_content(tag):
  content = tag.contents
  result = []
  for piece in content:
    piece = clean_tags(str(piece))
    if piece: result.append(piece)
  result =  " ".join(result)
  return result


def extract_ques_and_answers(html_page):
  qList, ansList = extract_text(html_page)
  all_ques, all_answer = [], []
  for ques,ans in zip(qList, ansList):
    ques = find_content(ques)
    ans = find_content(ans)
    all_ques.append(ques)
    all_answer.append(ans)
  return all_ques, all_answer
