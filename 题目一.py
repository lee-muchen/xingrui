from selenium import webdriver
import csv
# 打开Chrome浏览器
driver = webdriver.Chrome("F:/chromedriver.exe")
# 浏览网址
driver.get('https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml')

# 根据xpath提示表格开始行进行遍历
for row in range(9, 92):
    row_list = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[{}]'.format(str(row))).text.split()
    with open('题目1.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        # 提取前六列
        writer.writerow(row_list[:6])
