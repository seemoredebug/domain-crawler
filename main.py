import os
import random
import time
from datetime import datetime
import json

from GPT.gptExtraction import ask_question
from importIo import CrawlBaseApiClient
from pysitemap import crawler
from pysitemap.parsers.lxml_parser import Parser
from webSiteExtract.webSiteExtract import WebSiteExtract

if __name__ == '__main__':

    # current_datetime = datetime.now()
    # formatted_datetime = current_datetime.strftime("%Y%m%d_%H%M%S")
    # xmlPath = f"sitemaps/sitemap_{formatted_datetime}.xml"
    #
    # root_url = 'https://ohohpet.com/'
    # crawler(
    #     root_url, out_file=xmlPath, exclude_urls=[".pdf", ".jpg", ".zip"],
    #     http_request_options={"ssl": False}, parser=Parser
    # )
    #
    # token = '_2lOWoqVxl4_ZfaYEd1XBA'
    #
    # client = CrawlBaseApiClient(token)
    # urls = client.extract_urls_from_xml(xmlPath)
    # print("解析站点数量为: " + str(len(urls)))
    #
    # # 随机选择一个URL
    # url = random.choice(urls)
    #
    # print("随机选取的URL为: " + url)
    #

    dir = "./data/" + time.strftime("%Y-%m-%d_%H-%M-%S")
    website = WebSiteExtract("https://ohohpet.com/products/anti-breaking-i-shaped-cat-nylon-chest-strap-adjustable-pet-rope")
    website.open_website()
    content = website.extract_content(dir)
    website.close()
    print("解析完成")
    response = ask_question(content)
    response_file = os.path.join(dir, time.strftime("%Y-%m-%d_%H-%M-%S_json.txt"))  # 使用当前日期和时间作为文件名
    with open(response_file, "w", encoding="utf-8") as file:
        file.write(response)
    print("提取完成")
    # import_io_data = client.requestCrawlBase(url)
    #
    # # 文件路径和名称
    # file_path = "jsonData/data_{formatted_datetime}.json"
    #
    # print("数据解析完成: "+json.dumps(import_io_data))
    # # 确保文件夹存在，如果不存在则创建文件夹
    # os.makedirs(os.path.dirname(file_path), exist_ok=True)
    # # 将JSON数据写入文件
    # with open(file_path, 'w') as file:
    #     json.dump(import_io_data, file)