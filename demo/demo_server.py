from flask import Flask, request, make_response
from flask import render_template, jsonify
from model import model

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# mock the prediction model
@app.route('/predict', methods=['POST'])

def predict():
	fact = request.form['fact']
	print('TO PREDICT: ', fact)
	prediction = model.predict(fact)
	return jsonify({
		'accusation': prediction['accusation'], 
		'term': prediction['term']
	})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=6006, debug=True, load_dotenv=True)