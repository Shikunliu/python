from urllib import request
apple_url = 'http://chart.finance.yahoo.com/table.csv?s=AAPL&a=2&b=4&c=2017&d=3&e=4&f=2017&g=d&ignore=.csv'

def download_stock_data(csv_url):
	response = request.urlopen(csv_url) #打开url网址的操作，参数可以是一个url 
	csv = response.read() #all data stored in csv
	csv_str = str(csv)
	lines = csv_str.split("\\n") # 按照换行符号分段
	dest_url = r'apple.csv' #防止字符转义
	fx = open(dest_url, "w")
	for line in lines:
		fx.write(line + "\n")
	fx.close()

download_stock_data(apple_url)