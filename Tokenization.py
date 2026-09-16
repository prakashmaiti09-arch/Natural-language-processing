import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text="Natural Language Processing Is a branch of Artificial Intelligence"

tokens=word_tokenize(text)

print('Original Text:')
print(text)

print("\nTokens:")
print(tokens)


#Original Text:
#Natural Language Processing Is a branch of Artificial Intelligence


#Tokens:
#['Natural', 'Language', 'Processing', 'Is', 'a', 'branch', 'of', 'Artificial', 'Intelligence']
