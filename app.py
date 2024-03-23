from flask import Flask, render_template, jsonify, request
from sentencegen import convertArticleText, extract_features, generate_sentence_with_emotion, robertaClassifier
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        linkurl = request.form['link']
        passage = convertArticleText(linkurl)
        new_article = generate_sentence_with_emotion(passage, robertaClassifier(passage))
        return(new_article)
    else:
        return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    url = request.form.get('link')
    message = "Received link: " + url
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)
