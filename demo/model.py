"""
Mockup model
"""

class Model(object):
	def __init__(self):
		pass
	def predict(self, fact:str):
		return {'accusation': 'introducing bugs in code', 'term': '100 years'}


model = Model()