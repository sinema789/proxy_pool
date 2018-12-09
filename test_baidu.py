from selenium import webdriver
import unittest
from Base.SearchPage import SearchPage
from time import sleep


class BaiduTest(unittest.TestCase):
    """百度首页搜索测试用例"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"

    def test_baidu_search_01(self):
        driver = self.driver
        print("开始[case_0001]百度搜索")
        driver.get(self.base_url)

        # 验证标题
        self.assertEqual(driver.title, "百度一下，你就知道")
        search_page = SearchPage(self.driver)
        search_page.set_value("python")
        search_page.click_button()
        sleep(3)

        # 验证搜索结果标题
        self.assertEqual(driver.title, "python_百度搜索")

    def test_baidu_search_02(self):
        driver = self.driver
        print("开始[case_0002]百度搜索")
        driver.get(self.base_url)
        search_page = SearchPage(self.driver)
        search_page.set_value("淘宝")
        search_page.click_button()

        sleep(3)

        # 验证搜索结果标题
        self.assertEqual(driver.title, "淘宝_百度搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
