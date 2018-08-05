"""
Mockup model
"""
import joblib
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

class Model(object):
	def __init__(self):
		self.model = joblib.load('demo_model')
		self.tfidf_vectorizer = joblib.load('demo_tfidf_vectorizer')
		#jieba.load_userdict(path + '../dict.txt')
		#self.tokenizer = (lambda string: " ".join([token for token in jieba.cut(string, cut_all=False)]))
		
	def predict(self, fact:str):
		print("fact: "+fact)
		fact_token = " ".join([token for token in jieba.cut(fact, cut_all=False)])
		print("fact_token: "+fact_token)
		fact_tfidf = self.tfidf_vectorizer.transform([fact_token])
		accu = self.model.predict(fact_tfidf)[0]

		return {'accusation': accu, 'term': '100 years'}