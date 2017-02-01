import pickle 
import urllib.request 
#f = open ('somedata','wb')
html = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
print(html)
data = pickle.load(html)

for line in data:
	#print(line)
	print("".join([k * v for k, v in line]))