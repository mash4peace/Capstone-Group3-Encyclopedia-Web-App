import wikipedia
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    searchText = None
    wikiImage=None
    wikiText = None
    if request.method == 'POST' and 'searchText' in request.form:
        searchText = request.form['searchText']
        wikiPage = wikipedia.page(searchText)
        
        wikiText=wikiPage.content
        wikiImage=None
        wikiImage = wikiPage.images[0]
    return render_template('index.html', wikiText=wikiText, wikiImage=wikiImage)

if __name__ == '__main__':
    app.run(debug=True)

