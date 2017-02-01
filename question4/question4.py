import urllib.request
import re

def find (string,num):
	url = string+str(num)
	html = urllib.request.urlopen(url)
	content = html.read().decode()
	biaoda = re.compile("is\s(\d+)")
	judge = biaoda.search(content)
	if judge:
		nums = biaoda.findall(content)[0]
		print(nums)
		find (string,nums)
	else :
		print(content)

def main ():
	find (r'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=',63579)#16044 82682

if __name__ == '__main__':
	main()