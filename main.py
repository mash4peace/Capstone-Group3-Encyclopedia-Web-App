import wikipedia
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    searchText = None
    wikiText = None
    if request.method == 'POST' and 'searchText' in request.form:
        searchText = request.form['searchText']
        wikiText = wikipedia.summary(searchText)
    return render_template('index.html', wikiText=wikiText)

if __name__ == '__main__':
    app.run(debug=True)

