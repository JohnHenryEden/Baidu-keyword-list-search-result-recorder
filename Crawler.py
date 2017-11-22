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
driver.find_element_by_id("uc-common-account").send_keys("***Censored***")
driver.find_element_by_id("ucsl-password-edit").send_keys("***Censored***")
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
KeywordListFile = open("关键词.txt", 'r')
try:
    os.remove("AvrgSearchNum.txt")
except():
    print("清除旧文件失败！")
    sys.exit(1)
NumFile = open("AvrgSearchNum.txt", 'w')
KeywordList = []
for line in KeywordListFile.readlines():
    if line != '\n':
        KeywordList.append(line)
for i in range(0, KeywordList.__len__()):

        print(KeywordList[i])
        driver.find_element_by_xpath("//*[@id='ctrl-default-esui8785934']/div/div[1]/div[5]/div[1]/input").send_keys(KeywordList[i])
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='ctrl-default-esui8785934']/div/div[1]/div[5]/div[1]/div[2]").click()
        time.sleep(2)
        try:
            AvrgSearchNum = driver.find_element_by_xpath("//*[@id='ctrl-default-esui8785934']/div/div[1]/div[1]/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[4]/div").text
        except Exception as ex:
            print("此项无数据")
            NumFile.write("此项无数据")
        NumFile.write(AvrgSearchNum + "\n")
        driver.find_element_by_xpath("//*[@id='ctrl-default-esui8785934']/div/div[1]/div[5]/div[1]/input").clear()
        print(AvrgSearchNum)

NumFile.close()
KeywordListFile.close()

DataOrgnizer = open('BaiduDailyAvrgSearch.csv', 'w')
data1 = open('关键词.txt', 'r')
data2 = open("AvrgSearchNum.txt", 'r')
KwData = []
NumData = []
for entries in data1.readlines():
    KwData.append(entries.strip('\n'))
for entries in data2.readlines():
    NumData.append(entries)

for i in range(0, KwData.__len__()):

    DataOrgnizer.write(KwData[i] + "," + NumData[i])
    print(KwData[i] + "," + NumData[i])
data1.close()
data2.close()
DataOrgnizer.close()
driver.close()
