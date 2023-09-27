import xml.etree.ElementTree as ET
import requests
import json

class CrawlBaseApiClient:
    def __init__(self, token):
        self.token = token

    def requestCrawlBase(self, url):
        import_io_url = f'https://api.crawlbase.com/scraper?token={self.token}&url={url}'

        response = requests.get(import_io_url)
        json_data = json.loads(response.text)

        return json_data

    def extract_urls_from_xml(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        urls = [url.text for url in root.findall('ns:url/ns:loc', namespace)]

        return urls

if __name__ == '__main__':
    token = '_2lOWoqVxl4_ZfaYEd1XBA'
    file_path = '../sitemap-generator/debug/sitemap2.xml'

    client = CrawlBaseApiClient(token)
    # urls = client.extract_urls_from_xml(file_path)

    # url = urls[16]
    # print(url)

    url = "https://new8.wehomeshop.com/product/myzh7etaxs?c=SA&lang=en-US"
    import_io_data = client.requestCrawlBase(url)
    print(json.dumps(import_io_data))
