import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

text='Natural Language Processing Is a branch of Artificial Intelligence'

tokens=word_tokenize(text)
print('Original text:')
print(text)
stop_words = set(stopwords.words('english'))

filtered_tokens = []

for word in tokens:
    if word.lower() not in stop_words:
        filtered_tokens.append(word)

print("\nTokens after Stop Word Removal:")
print(filtered_tokens)




#Original text:
#Natural Language Processing Is a branch of Artificial Intelligence

#Tokens after Stop Word Removal:
#['Natural', 'Language', 'Processing', 'branch', 'Artificial', 'Intelligence']
