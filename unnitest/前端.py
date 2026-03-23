import unittest
from _ast import Assert

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Denglu(unittest.TestCase):
    def setUp(self):#登录
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get('http://127.0.0.1:8090/book/')
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/ul/li[6]/a").click()
        time.sleep(3)
        self.driver.find_element(By.NAME, "user.username").send_keys("1")
        self.driver.find_element(By.NAME, "user.password").send_keys("1")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div/form/div[4]/input").click()


    def test_detail(self):
        print("查看图书详情")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[5]/div[1]/div/a/img").click() #查看图书详情
        check = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]").text
        time.sleep(3)
        self.assertTrue(check)

    def test_cart(self):
        print("加入购物车")
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[5]/div[1]/div/a/img").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[3]/a/img").click()  #加入购物车
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[1]/a").click()   #查看购物车
        check = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]").text
        time.sleep(3)
        self.assertTrue(check)

    def test_bi(self):
        print("查看书店简介")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/ul/li[2]/a").click() #查看书店简介
        check = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]").text
        time.sleep(3)
        self.assertTrue(check)

    def test_search(self):
        print("图书搜索")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/ul/li[8]/form/input").send_keys("程序员修炼手册")  # 图书搜索
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/ul/li[8]/form/a").click()
        check = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]").text
        time.sleep(3)
        self.assertTrue(check)

    def test_sale(self):
        print("查看优惠促销")
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/ul/li[5]/a").click()  # 查看优惠促销
        check = self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[1]").text
        time.sleep(3)
        self.assertTrue(check)




    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Denglu("test_detail"))
    suite.addTest(Denglu("test_cart"))
    suite.addTest(Denglu("test_bi"))
    suite.addTest(Denglu("test_search"))
    suite.addTest(Denglu("test_sale"))
    runner = unittest.TextTestRunner()
    runner.run(suite)