from flask import Flask
from flask import render_template, request
from scraper import *


app = Flask(__name__)
@app.route('/', methods=['GET'])
def root():
    if request.method == 'GET':
        return render_template('home.html')
@app.route('/results')
def results():
        scraper = ProxyScraper()
        scraper.run()
        return render_template('results.html', proxies = scraper.results)



if __name__ == '__main__':
    app.run(debug=True, threaded = True)
