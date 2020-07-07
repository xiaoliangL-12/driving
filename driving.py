country = input('请问你是哪国人: ')
age = input('请输入你年龄: ')
age = int(age)
if country == '中国人':
	if age >= 18:
		print('你可以开车')
	else:
		print('你不能开车')
