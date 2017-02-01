import zipfile
import re

def findd (string):
	z = zipfile.ZipFile('channel.zip','r')
	name = string + '.txt'
	content = z.read(name).decode()
	expr1 = re.compile('is\s(\d{2,})')
	judge1 = expr1.search(content)
	if judge1:
		nums = expr1.findall(content)[0]
		print (z.getinfo(name).comment.decode(),end='')
		findd (str(nums))
	else :
		print ("\n"+content)

def main ():
	findd ('90052')

if __name__ == '__main__':
	main()