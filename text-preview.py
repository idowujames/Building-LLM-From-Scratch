import re

with open('the-verdict.txt', 'r', encoding='utf-8') as f:
    text = f.read()

## print("Total Number of Characters:",len(text))

t = "Hello, world. This, is a test."

splitted = re.split(r'([,.]|\s)', t)
splitted = [item for item in splitted if item.strip()]
print(splitted)