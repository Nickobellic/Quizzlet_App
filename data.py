import requests
import ast



questions = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean").content
data_o = questions.decode("UTF-8")
data_n = ast.literal_eval(data_o)

question_data = data_n['results']

