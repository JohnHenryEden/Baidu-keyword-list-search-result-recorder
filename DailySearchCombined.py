from selenium import webdriver
import time
import os
import sys

# driver = webdriver.PhantomJS(executable_path=r'opt\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Chrome()
driver.get("http://www2.baidu.com")
print("开始登录")
time.sleep(2)
driver.find_element_by_class_name("tab-header").click()
driver.find_element_by_id("uc-common-account").send_keys("JohnHEden")
driver.find_element_by_id("ucsl-password-edit").send_keys("E3nclave")
print("请输入验证码！")
while 1:
    if driver.find_element_by_id("uc-common-token").text is not None:
        time.sleep(10)
        driver.find_element_by_id("submit-form").click()
        if driver.current_url == "http://cas.baidu.com/?tpl=www2&fromu=http%3A%2F%2Fwww2.baidu.com%2F":
            continue
        else:
            break
time.sleep(3)
driver.find_element_by_class_name("product-data-entrance").click()
time.sleep(3)
handles = driver.window_handles
for handle in handles:
    if handle != driver.current_window_handle:
        driver.switch_to.window(handle)
time.sleep(10)
try:
    driver.find_element_by_class_name("ui_dialog_close").click()
except():
    print("广告未弹出，可以继续")

driver.find_element_by_class_name("operator-krStation").click()

time.sleep(3)

# TODO:Search all the keywords in the list and write the result to a .txt(.csv)file
KeywordList = open("关键词.txt", 'r').readlines()
ResFile = open("CombinedDailySearch.csv", 'w')
for kw in KeywordList:
    for i in range(0, KeywordList.__len__()):
        kwCombined = kw.strip("\r\n") + ' ' + KeywordList[i].strip("\r\n")
        driver.find_element_by_xpath("//*[@id='ctrl-default-esui8785934']/div/div[1]/div[5]/div[1]/input").send_keys(kwCombined)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='ctrl-default-esui8785934']/div/div[1]/div[5]/div[1]/div[2]").click()
        time.sleep(2)
        try:
            AvrgSearchNum = driver.find_element_by_xpath(
                "//*[@id='ctrl-default-esui8785934']/div/div[1]/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[4]/div").text
            ResFile.write(kwCombined + ',' + AvrgSearchNum + '\n')
            print(kwCombined + ',' + AvrgSearchNum)
        except Exception as ex:
            ResFile.write(kwCombined + ',' + "此项无数据" + '\n')
            print(kwCombined + ',' + "此项无数据")
        driver.find_element_by_xpath("//*[@id='ctrl-default-esui8785934']/div/div[1]/div[5]/div[1]/input").clear()




driver.close()
