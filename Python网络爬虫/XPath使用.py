from selenium import webdriver

def myXpath(xpath):
	driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/chromedriver/chromedriver.exe")
	url = "https://www.douyu.com/g_jdqs"
	driver.get(url)
	temp = driver.find_element_by_xpath(xpath).text
	print(temp)

def iteratorXpath(li_xpath):
	driver = webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/chromedriver/chromedriver.exe")
	li_list = driver.find_elements_by_xpath(li_xpath)
	print(li_list)
	for li in li_list:
		mytxt = li.find_element_by_xpath('./a/div/div/h3').text
		print(mytxt)

if __name__=="__main__":
	# dic = {"title":"//*[@id='live-list-contentbox']/li[2]/a/div[1]/div/h3","game":"//*[@id='live-list-contentbox']/li[2]/a/div[1]/div/span","master":"//*[@id='live-list-contentbox']/li[2]/a/div[1]/p/span[1]"}
	# for i in dic：
	# 	myXpath(i.value)
	li_xpath = "//*[@id='live-list-contentbox']/li"
	iteratorXpath(li_xpath)