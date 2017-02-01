def change(stri,str1):
	for i in range(len(stri)):
		if ord('a') <= ord(stri[i]) <= ord('x'):
			str1[i] = chr(ord(stri[i])+2) 
			print(str1[i],end='')
		elif ord('y') <= ord(stri[i]) <= ord('z'):
			str1[i] = chr(ord(stri[i])-ord('y')+ord('a'))
			print(str1[i],end='')
		else:
			print (stri[i],end='')
	print()
def main ():
	str1 = {}
	change('''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.''',str1)
	change('map',str1)
	#aa = str1.maketrans();
	#print (aa)
	
if __name__ == '__main__':
	main()