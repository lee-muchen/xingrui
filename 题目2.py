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

text_dict = {}
text_list = long_text.strip().split('\n')
text_dict['name'] = text_list[0]
text_dict['lei'] = text_list[1]
del text_list[:2]
text_dict['sub_fund'] = []

isin_list = []
sub_fund_dict = {}
for text in text_list:
    print(text)
    if text.find('.') > 0:  # 是
        if sub_fund_dict:
            text_dict['sub_fund'].append(sub_fund_dict)
        sub_fund_dict['title'] = text.split('.')[1].strip(' ')
        sub_fund_dict['isin'] = []
    else:
        sub_fund_dict['isin'].append(text)
print(text_dict)
