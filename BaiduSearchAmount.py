from selenium import webdriver
import time
import re

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
KwList = open("关键词.txt").readlines()

crawlResult = open('KeyWordResultNum.csv', 'w')

pattern = re.compile("\d+.\d+.\d+")

for kw in KwList:
    kw.strip('\n')
    driver.find_element_by_class_name("s_ipt").send_keys(kw)
    driver.find_element_by_id("su").click()
    time.sleep(2.5)
    try:
        resultNum = pattern.findall(driver.find_element_by_class_name("nums").text).pop()
        print(kw.strip('\n') + ',' + resultNum.replace(',', '') + "\n")
        crawlResult.write(kw.strip('\n') + ',' + resultNum.replace(',', '') + "\n")
    except Exception as ex:
        print(kw.strip('\n') + ',' + "<1000" + "\n")
        crawlResult.write(kw.strip('\n') + ',' + "<1000"  + "\n")
    driver.find_element_by_class_name("s_ipt").clear()

driver.close()
