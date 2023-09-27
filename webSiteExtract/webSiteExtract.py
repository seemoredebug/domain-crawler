import os
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import TimeoutException

class WebSiteExtract:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def open_website(self):
        # 设置 Chrome 浏览器选项
        options = Options()
        # options.add_argument("--headless")  # 使用无头模式，不显示浏览器窗口

        # 启动 ChromeDriver
        self.driver = webdriver.Chrome(options=options)

        # 打开网站
        self.driver.get(self.url)

    def extract_content(self,dir):
        # 创建存储文件的文件夹
        data_dir = dir
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # 等待渲染完成
        self.wait_for_render()
        time.sleep(2)
        # 获取页面的完整 HTML 内容
        html_content = self.driver.page_source

        # 使用 BeautifulSoup 解析 HTML 内容
        soup = BeautifulSoup(html_content, 'html.parser')

        # 递归删除所有图片节点
        image_urls = []
        for img in soup.find_all('img'):
            img.extract()
            image_urls.append(img['src'])

        # 保存图片链接至文件
        image_file_name = os.path.join(data_dir, time.strftime("%Y-%m-%d_%H-%M-%S_image_urls.txt"))  # 使用当前日期和时间作为文件名
        with open(image_file_name, "w", encoding="utf-8") as file:
            for url in image_urls:
                file.write(url + "\n")

        # 提取所有文本内容
        all_text = soup.get_text()
        # 使用正则表达式替换连续的空白字符
        all_text = re.sub(r'\n{2,}', '\n', all_text)
        all_text = re.sub(r'\s{2,}', ' ', all_text)
        # 保存文本到文件
        text_file_name = os.path.join(data_dir, time.strftime("%Y-%m-%d_%H-%M-%S.txt"))  # 使用当前日期和时间作为文件名
        with open(text_file_name, "w", encoding="utf-8") as file:
            file.write(all_text)

        # 保存 HTML 到文件
        html_file_name = os.path.join(data_dir, time.strftime("%Y-%m-%d_%H-%M-%S.html"))  # 使用当前日期和时间作为文件名
        with open(html_file_name, "w", encoding="utf-8") as file:
            file.write(html_content)

        # 保存网站截图
        screenshot_name = os.path.join(data_dir, time.strftime("%Y-%m-%d_%H-%M-%S.png"))  # 使用当前日期和时间作为文件名
        self.driver.save_screenshot(screenshot_name)
        return all_text

    def close(self):
        # 关闭浏览器
        self.driver.quit()

    def wait_for_render(self):
        start_time = time.time()
        while True:
            try:
                self.driver.execute_script("return document.readyState") == "complete"
                break
            except TimeoutException:
                pass

            if time.time() - start_time > 10:
                break
            time.sleep(1)


if __name__ == '__main__':
    # website = WebSiteExtract("https://new8.wehomeshop.com/product/myzh7etaxs?c=SA&lang=en-US")
    website = WebSiteExtract("https://sinootea.com/products/little-green-citrus-dried-tangerine-peel-ferment-pu-erh")
    website.open_website()
    website.extract_content()
    website.close()

