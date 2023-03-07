long_text = """
Variopartner SICAV
529900LPCSV88817QH61
1. TARENO GLOBAL WATER SOLUTIONS FUND
LU2001709034
LU2057889995
LU2001709547
2. TARENO FIXED INCOME FUND
LU1299722972
3. TARENO GLOBAL EQUITY FUND
LU1299721909
LU1299722113
LU1299722030
4. MIV GLOBAL MEDTECH FUND
LU0329630999
LU0329630130
"""
# 定义列表
text_dict = {}
# 切割去空格
text_list = long_text.strip().split('\n')
# name lei 添加到字典中
text_dict['name'] = text_list[0]
text_dict['lei'] = text_list[1]
# 删除已添加的元素
del text_list[:2]
text_dict['sub_fund'] = []

isin_list = []
sub_fund_dict = {}
# 循环处理sub_fund内容
for text in text_list:
    # 判断是否有序号
    if text.find('.') > 0:  # 是
        # 提交上一轮sub——fund信息
        if sub_fund_dict:
            text_dict['sub_fund'].append(sub_fund_dict)
        # 初始化新sub_fund元素
        sub_fund_dict['title'] = text.split('.')[1].strip(' ')
        sub_fund_dict['isin'] = []
    else:
        sub_fund_dict['isin'].append(text)
print(text_dict)
