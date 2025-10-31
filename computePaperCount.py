EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EOF = (-1)


class PaperCountComputing:
	@staticmethod
	def computePaperCount(lines:tuple|list|set) -> int:
		if isinstance(lines, (tuple, list, set)):
			cnt = 0
			for line in lines:
				if line:
					cnt += int(line.split(" * ")[1].split(" ")[0], 0) if " * " in line else 1
			return cnt
		else:
			return -1


def main() -> int:
	try:
		print("Paste the journals and conferences your have reviewed here compressed by \" * \". ")
		lines = []
		while True:
			line = input()
			if line:
				lines.append(line)
			else:
				break
		paperCount = PaperCountComputing.computePaperCount(lines)
		if paperCount > 1:
			print("You have reviewed {0} papers. ".format(paperCount))
			iRet = EXIT_SUCCESS
		elif paperCount >= 0:
			print("You have reviewed {0} paper. ".format(paperCount))
			iRet = EXIT_SUCCESS
		else:
			print("Failed to compute due to Code {0}. ".format(int(paperCount)))
			iRet = EXIT_FAILURE
	except BaseException as e:
		print("The following exception occurred. \n\t{0}".format(e))
		iRet = EOF
	try:
		print("Please press the enter key to exit ({0}). ".format(iRet))
		input()
	except:
		print()



if "__main__" == __name__:
	exit(main())