'''PY PROGRAM TO GENERATE A SUMMARY FOR A GIVEN PIECE OF TEXT'''

'''FURTHER TASKS:
1. REPLACE MORE CASES LIKE i.e., AND e.g. IN ORDER TO AVOID CONFUSIONS WHILE TOKENIZING.
2. FIND A WAY TO GET THE TEXT FROM PARSING THE SOURCE CODE OF A WEBSITE.
3. MODULARIZE THE CODE.
4. EXPAND STOPWORD LIST.
5. CONVERT THE SUMMARY FROM LIST TO STRING.'''



import nltk
from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest
from nltk.probability import FreqDist
from collections import defaultdict

t = input("Enter text: ")
t = t.replace("i.e.","that is, ")
t = t.replace("e.g.","for example, ")		#FIND MORE SUCH CASES LIKE THESE TWO


def summarize(text, n):
	sents = sent_tokenize(text)

	assert n <= len(sents)
	word_sent = word_tokenize(text.lower())
	_stopwords = set(stopwords.words('english') + list(punctuation))	#Create a custom list of all stopwords to be removed from the text. The list consists of all stopwords from nltk.corpus as well as punctuation marks from string module.
	word_sent = [word for word in word_sent if word not in _stopwords]	#Create a list of all words in the text with the stopwords removed.
	freq = FreqDist(word_sent)	#The freq distribution of the words in the text is constructed as a dictionary with the key as the word and the value as its frequency.

	ranking = defaultdict(int)		#Create a new dictionary to store the word frequencies.
	for i, sent in enumerate(sents):
		for w in word_tokenize(sent.lower()):
			if w in freq:
				ranking[i] += freq[w]
	sents_index = nlargest(n, ranking, key=ranking.get)	#Get the top n frequencies of words in the text
	return [sents[j] for j in sorted(sents_index)]



print("\nSummary: ", summarize(t,10))

