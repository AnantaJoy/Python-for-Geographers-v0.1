from bs4 import BeautifulSoup
import requests

response = requests.get("http://stackoverflow.com/questions/")
soup = BeautifulSoup(response.text, "html.parse")

questions = soup.select(".question-summary")
print(questions[0].get("id", 0))
for question in questions:
    print(questions[0].select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())






