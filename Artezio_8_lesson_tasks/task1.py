"""Task 1 """
import requests

def get_html_page(url):
    url_request = requests.get(url)
    html_page = url_request.text
    return len(html_page)



print(get_html_page('https://google.com'))
