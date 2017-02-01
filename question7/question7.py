from PIL import Image

def findd (string):
	im = Image.open(string,'r')
	print (im)
def main ():
	findd("oxygen.png")

if __name__ == '__main__':
	main()