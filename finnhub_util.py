import finnhub
import requests

finnhub_client = finnhub.Client(api_key="cltm329r01qlu9okeajgcltm329r01qlu9okeak0")

def get_news():
    headlines = []
    conn = finnhub_client.general_news('general', min_id=0)
    if conn:
        for i in range(0, 5):
            headline = conn[i]['headline']
            url = conn[i]['url']
            image = conn[i]['image']
            summary = conn[i]['summary']
            headline_with_link = f'<a href="{url}" target="_blank">{headline}</a>'
            headlines.append({"headline": headline_with_link, "image": image, "summary": summary})
    return headlines
def get_stock_info():
    fortune_500_companies = [
        "WMT",
        "BRK.A",
        "AAPL",
        "AMZN"
    ]

    stock_info_list = []

    for symbol in fortune_500_companies:
        conn = finnhub_client.quote(symbol)
        logoconn = finnhub_client.company_profile2(symbol=symbol)
        close = conn['pc']
        current = conn['c']
        logo = logoconn['logo']
        color = "#90EE90" if close < current else "#ffcccb"
        logo_html = f"<img src='{logo}' alt='{symbol} Logo' style='width:50px;height:50px;'>"

        stock_info = f" {logo_html} {symbol}\n Close: {close} Current: {current} {conn['dp']} %"
        stock_info_list.append({"stock_info": stock_info, "color": color})

    return stock_info_list
def is_open():

    status_conn = finnhub_client.market_status(exchange='US')['isOpen']


    if status_conn == 'True':
        status = 'Open'
    else:
        status = 'Closed'
    return status



def status():
    url = "https://fear-and-greed-index.p.rapidapi.com/v1/fgi"

    headers = {
        "X-RapidAPI-Key": "21f43f6fe2msh2998ed916e77989p104673jsn0e135243fa7c",
        "X-RapidAPI-Host": "fear-and-greed-index.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            now = data['fgi']['now']['valueText']
            return f"Fear & Greed Index: {now}"
        else:
            return f"Error: {response.status_code} - {response.text}"

    except Exception as e:
        return f"An error occurred: {e}"


