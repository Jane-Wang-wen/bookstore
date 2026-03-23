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
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/ul/li[8]/a").click()  # 后台登录
        handles_list = self.driver.window_handles
        print(handles_list)
        self.driver.switch_to.window(handles_list[-1])
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[1]/td[2]/input").send_keys(
        #     1)
        # self.driver.find_element(By.XPATH,
        #                          "/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(
        #     1)
        self.driver.find_element(By.XPATH,
                                 "/html/body/map/area[1]").click()
        # time.sleep(3)
        # check = self.driver.find_element(By.XPATH,
        #                                  "/html/body/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr/td/span[3]/a").text
        time.sleep(3)
        frame1 = self.driver.find_element(By.ID, "mainFrame")
        time.sleep(3)
        self.driver.switch_to.frame(frame1)


    def test_tjts(self):
        time.sleep(3)
        frame4 = self.driver.find_element(By.ID, "frame_left")
        time.sleep(3)
        self.driver.switch_to.frame(frame4)
        print("添加图书")
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div[5]/a").click() #添加图书
        self.driver.find_element(By.XPATH,
                                 "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div[6]/ul/li[5]/a").click()
        self.driver.switch_to.parent_frame()
        frame5 = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[3]/iframe")
        time.sleep(3)
        self.driver.switch_to.frame(frame5)
        self.driver.find_element(By.XPATH,
                                 "/html/body/form/input[2]").send_keys("自动化测试用书")  # 添加图书
        self.driver.find_element(By.XPATH,
                                 "/html/body/form/input[8]").click()  # 添加图书
        time.sleep(3)
        # self.driver.switch_to.parent_frame()
        # frame6 = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[3]/iframe")
        # time.sleep(3)
        # self.driver.switch_to.frame(frame6)
        check = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/div").text
        time.sleep(3)
        self.assertEqual("自动化测试用书", check)

    def test_tjlm(self):
        frame2 = self.driver.find_element(By.ID, "frame_left")
        time.sleep(3)
        self.driver.switch_to.frame(frame2)
        print("添加类目")
        self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div[7]/a").click()
        self.driver.find_element(By.XPATH,"/html/body/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div[8]/ul/li[2]/a").click()
        self.driver.switch_to.parent_frame()
        frame3 = self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td[3]/iframe")
        time.sleep(3)
        self.driver.switch_to.frame(frame3)
        self.driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[1]/td/input").send_keys("测试类目")
        self.driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td/input").click()
        check=self.driver.find_element(By.XPATH, "/html/body/table/tbody/tr[1]/td/table/tbody/tr/td[2]/span").text
        self.assertEqual("类目列表", check)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Denglu("test_tjts"))
    suite.addTest(Denglu("test_tjlm"))
    runner = unittest.TextTestRunner()
    runner.run(suite)