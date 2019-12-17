import requests
import json

'''

def translate(string):
	query_str = string

	# 检查输入语言类型
	post_url = "https://fanyi.baidu.com/langdetect"
	post_data = {"query":query_str}
	# res = requests.post(post_url,data=post_data)
	# print(res.content.decode())

	# 对应翻译
	headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}
	post_url_from_to = "https://fanyi.baidu.com/basetrans"
	post_data_en_cn = {"query":query_str,
						"from":"en",
						"to":"zh"}
	
	res = requests.post(post_url_from_to,data=post_data_en_cn,headers=headers)
	result = json.loads(res.content.decode())
	print("result:" + result["trans"][0]["dst"])

def translateCycle():
	flag = True
	while flag:
		string = input("Input the content that you want to translate or input 'exit' to exit:")
		if(string=='exit'):
			flag = False
		else:
			translate(string)


if __name__=="__main__":
	translateCycle()
'''

class translate():

	def __init__(self,string):
		self.string = string
		self.Language = 'zh'
		self.toLanguage = 'en'
		self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"}
		self.langUrl = "https://fanyi.baidu.com/langdetect"
		self.transUrl = "https://fanyi.baidu.com/basetrans"

	def language(self):
		post_data = {"query":self.string}
		result = requests.post(self.langUrl, data=post_data,headers=self.headers)
		# print(json.loads(result.content.decode()))
		return json.loads(result.content.decode())["lan"]

	def translating(self):
		self.Language = self.language()
		if(self.Language=='zh'):
			self.toLanguage='en'
		else:
			self.toLanguage='zh'
		post_data = {"query":self.string,
						"from":self.Language,
						"to":self.toLanguage}
		res = requests.post(self.transUrl,data=post_data,headers=self.headers)
		result = json.loads(res.content.decode())
		print("result:" + result["trans"][0]["dst"])	

def tanslateCycle():
	flag = True
	while flag:
		string = input("Input the content that you want to translate or input 'exit' to exit:")
		if(string=='exit'):
			flag = False
		else:
			translate(string).translating()	

if __name__ == "__main__":
	tanslateCycle()
