def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page,"html5lib")
    links = [element.get('href') for element in doc.find_all('a')]
    return links
if __name__ == '__main__':
    for num, link in enumerate(get_links('http://boingboing.net')):
        print(num, link)
