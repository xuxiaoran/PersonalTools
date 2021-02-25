import os

def dfs(root):
	for item in os.listdir(root):
		path = root + '/' + item
		#print("checking " + path)
		if item == "._.DS_Store" or item == ".DS_Store":
			print(path)
			os.remove(path)
		else:
			if(os.path.isdir(path)):
				#print("going to " + path)
				dfs(path)


if __name__ == '__main__':
	root = input("Enter where to start: ")
	dfs(root)
