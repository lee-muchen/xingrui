from selenium import webdriver
import csv
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
}
driver = webdriver.Chrome("F:/chromedriver.exe")
driver.get('https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml')
# //*[@id="hiddenContent"]/table/tbody/tr[91]
# //*[@id="hiddenContent"]/table/tbody/tr[10]/td[6]
# //*[@id="hiddenContent"]/table/tbody/tr[9]/td[1]
# test = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[9]').text
# print(test)

for row in range(9, 92):
    row_list = driver.find_element_by_xpath('//*[@id="hiddenContent"]/table/tbody/tr[{}]'.format(str(row))).text.split()
    with open('题目1.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(row_list[:6])
