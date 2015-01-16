#-*- coding: utf-8 -*-

#코드님의 상태가...?

import string

def printLogo():
	print ("="*50 + """
	Refrigerator _ light
""" + "="*50)

def printMenu():
	print (u"""\t1. 보관 품목 조회
	2. 물건 넣기
	3. 물건 빼기
	0. 종료""")

#class Vector(object):						#벡터 무쓸모
#	"""docstring for Vector"""
#	def __init__(self, x=0, y=0):
#		super(Vector, self).__init__()
#		self.x = x
#		self.y = y



def readFile(itemDic):	#string itemName, int itemCount

	try:
		f = open("list.txt", "r")
	except (OSError, IOError), e:
		print u"error: 냉장고가 없습니다. 냉장고를 비치하겠습니다"
		f = open("list.txt", "w")
	else:
		line = f.readline()
		while line:
			if line=="":
				break
			parsed_list = line.split('\t')
			itemDic[parsed_list[0]] = parsed_list[1]
			line = f.readline()

		f.close()

def writeFile(itemDic):	#string, int
	dicKey = itemDic.keys()		#itemName
	dicValue = itemDic.values()	#itemCount
	try:
		f = open("list.txt", "w")
	except (OSError, IOError), e:
		print u"Error: unknown file IOError"
		return
	else:
		length = len(itemDic)
		for i in xrange(0,length):
			f.write(dicKey[i])
			f.write("\t")
			f.write(str(dicValue[i]))
			#f.write("\n")		#왜 끝에 캐리지리턴이 자동으로 들어가는지 모르겠네
			
		f.close()
		

def vSearch(itemDic, compareStr):	#있는지 조사
	return compareStr in itemDic



def input_item():
	inputBuffer = raw_input("입력할 아이템은?")
	itemDic = {}
	
	readFile(itemDic)


	isLocated = vSearch(itemDic, inputBuffer)
	if isLocated == True:							# 있으면
		tempValue = int(itemDic[inputBuffer])
		del itemDic[inputBuffer]
		itemDic[inputBuffer] = tempValue + 1	#삭제하고 새로 개수 늘려서 추가
	else:							# 없으면
		itemDic[inputBuffer] = 1


	writeFile(itemDic)


def output_item():
	inputBuffer = raw_input("꺼낼 아이템은?")
	itemDic = {}

	readFile(itemDic)

	isLocated = vSearch(itemDic, inputBuffer)
	if isLocated == True:							# 있으면
		tempValue = int(itemDic[inputBuffer])
		del itemDic[inputBuffer]				#1개면 그냥 날림
		if tempValue > 1:
			itemDic[inputBuffer] = tempValue - 1	#삭제하고 개수빼서 추가
	else:
		print u"어...읎어요" + "\n"

	writeFile(itemDic)

def lookup():
	try:
		f = open("list.txt", "r")
	except (OSError, IOError), e:
		print u"error: 냉장고가 없습니다. 냉장고를 비치하겠습니다"
		f = open("list.txt", "w")
	else:
		print u"\t현재 보관하고 있는 품목은 다음과 같습니다:"
		line = f.readline()
		while line:											#빈줄있으면 버그
			parsed_list = line.split('\t')
			print parsed_list[0] + "\t" + parsed_list[1]
			line = f.readline()

		f.close()


def main():


	while 1:
			printLogo()
			printMenu()
			menusel = raw_input("입력하세요 : ")
			if menusel == "1":
				lookup()
			elif menusel == "2":
				input_item()
			elif menusel == "3":
				output_item()
			elif menusel == "0":
				return 0
			else:
				print u">>>>>Error: 올바른 값을 입력해주세요"


main()



