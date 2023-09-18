import os
import random
from datetime import datetime
import json

from importIo import ImportIoApiClient
from pysitemap import crawler
from pysitemap.parsers.lxml_parser import Parser

if __name__ == '__main__':

    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
    xmlPath = f"sitemaps/sitemap_{formatted_datetime}.xml"

    root_url = 'https://sinootea.com/'
    crawler(
        root_url, out_file=xmlPath, exclude_urls=[".pdf", ".jpg", ".zip"],
        http_request_options={"ssl": False}, parser=Parser
    )

    token = '_2lOWoqVxl4_ZfaYEd1XBA'

    client = ImportIoApiClient(token)
    urls = client.extract_urls_from_xml(xmlPath)
    print("解析站点数量为: " + str(len(urls)))

    # 随机选择一个URL
    url = random.choice(urls)

    print("随机选取的URL为: " + url)
    import_io_data = client.requestImportIo(url)

    # 文件路径和名称
    file_path = "jsonData/data_{formatted_datetime}.json"

    print("数据解析完成: "+json.dumps(import_io_data))
    # 确保文件夹存在，如果不存在则创建文件夹
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # 将JSON数据写入文件
    with open(file_path, 'w') as file:
        json.dump(import_io_data, file)