# app.py
from flask import Flask, render_template
from finnhub_util import get_news, get_stock_info, status, is_open

app = Flask(__name__)

@app.route('/')
def index():
    headlines = get_news()
    stock_info_list = get_stock_info()
    status_info = status()
    open = is_open()
    return render_template('index.html', headlines=headlines, stock_info_list = stock_info_list, status = status_info, open =open)

if __name__ == '__main__':
    app.run(debug=True)
