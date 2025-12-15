import os
from sys import argv, exit
from time import sleep
try:
	os.chdir(os.path.abspath(os.path.dirname(__file__)))
except:
	pass
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EOF = (-1)


class Node:
	def __init__(self:object, parent:object|None = None) -> object:
		self.__content, self.__children, self.__parent = "", [], parent
	def addContent(self:object, content:str) -> bool:
		if isinstance(content, str):
			self.__content += content
			return True
		else:
			return False
	def addChild(self:object) -> object:
		child = Node(parent = self)
		self.__children.append(child)
		return child
	def getParent(self:object) -> object|None:
		return self.__parent
	def __str__(self:object) -> str:
		self.__children.sort(key = lambda x:x.__content)
		return "{0}{1}".format(self.__content, "".join(str(child) for child in self.__children))

class Arranger:
	def __init__(self:object, inputFilePath:str, outputFilePath:str) -> object:
		self.__inputFilePath, self.__outputFilePath, self.__root = inputFilePath, outputFilePath, None
	def __countLevel(self:object, line:str) -> int:
		if isinstance(line, str):
			cnt = 0
			for ch in line:
				if "#" == ch:
					cnt += 1
				else:
					break
			return cnt
		else:
			return -1
	def load(self:object, encoding:str = "utf-8") -> bool:
		try:
			with open(self.__inputFilePath, "r", encoding = encoding) as f:
				content = f.read()
		except BaseException as e:
			print("Failed to load \"{0}\" due to exceptions. Details are as follows. \n\t{1}".format(self.__inputFilePath, e))
			return False
		self.__root, nodeLevel = Node(), 0
		node = self.__root
		for line in content.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
			level = self.__countLevel(line)
			if level >= 1:
				if nodeLevel < level:
					while nodeLevel < level:
						node = node.addChild()
						nodeLevel += 1
				else:
					while nodeLevel > level:
						node = node.getParent()
						nodeLevel -= 1
					node = node.getParent().addChild()
			node.addContent(line + "\n")
		print("Successfully loaded \"{0}\". ".format(self.__inputFilePath))
		return True
	def dump(self:object, encoding:str = "utf-8") -> bool:
		try:
			with open(self.__outputFilePath, "w", encoding = encoding) as f:
				f.write(str(self.__root)[:-1])
			print("Successfully wrote to \"{0}\". ".format(self.__outputFilePath))
			return True
		except BaseException as e:
			print("Failed to write to \"{0}\" due to exceptions. Details are as follows. \n\t{1}".format(self.__outputFilePath, e))
			return False

def main() -> int:
	warningTime = 3
	argc = len(argv)
	if argc >= 3:
		arranger = Arranger(argv[1], argv[2])
		iRet = EXIT_SUCCESS if arranger.load() and arranger.dump() else EXIT_FAILURE
	elif 2 == argc:
		print("The script will process the file in place within {0} second(s). ".format(warningTime))
		try:
			sleep(warningTime)
			arranger = Arranger(argv[1], argv[1])
			iRet = EXIT_SUCCESS if arranger.load() and arranger.dump() else EXIT_FAILURE
		except:
			iRet = EOF
	else:
		print("Nothing to handle. Please use the command line to specify the input and output files. ")
		iRet = EOF
	print("Please press the enter key to exit ({0}). ".format(iRet))
	try:
		input()
	except:
		print()
	return iRet



if "__main__" == __name__:
	exit(main())