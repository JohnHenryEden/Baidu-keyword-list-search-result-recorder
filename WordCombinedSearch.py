from selenium import webdriver
import time
import re

driver = webdriver.Firefox()
driver.set_window_size(1024, 800)
driver.get("https://www.baidu.com")
KwList = open("简化关键词.txt").readlines()

crawlResult = open('KeyWordCombinedResultSimp1.925.csv', 'w')

pattern = re.compile("\d+.\d+.\d+")

KWCList = open('简化关键词组合1.txt', 'r')

def set():
    for kw in KwList:
        for i in range(0, KwList.__len__()):
            KWCList.write(kw.strip('\r\n') + ' ' + KwList[i])
            print(kw.strip('\r\n') + ' ' + KwList[i])

def get():
    for kw in KWCList:
        try:
            driver.find_element_by_class_name("s_ipt").send_keys(kw)
            driver.find_element_by_id("su").click()
            time.sleep(2)
            try:
                resultNum = pattern.findall(driver.find_element_by_class_name("nums").text).pop()
                print(kw.strip("\r\n") + ',' + resultNum.replace(',', '') + "\n")
                crawlResult.write(kw.strip("\r\n") + ',' + resultNum.replace(',', '') + "\n")
            except Exception as ex:
                print(kw.strip("\r\n") + ',' + "1000" + "\n")
                crawlResult.write(kw.strip("\r\n") + ',' + "1000" + "\n")
            driver.find_element_by_class_name("s_ipt").clear()
        except Exception as e:
            print(str(e) + ' ' + kw)

get()
driver.close()
