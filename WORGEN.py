import time
import os
from itertools import product

print("- \n      ---       ---           PPPPPP   RRRRRR    EEEEEEEE  SSSSSSS   EEEEEEEE  NNN     NN  TTTTTTTTTT  SSSSSSS\n    --- ---     ---           PP   PP  RR   RR   EE        SS   SSS  EE        NN NN   NN      TT      SS   SSS\n   ---   ---    ---           PPPPPP   RRRRRR    EEEEEEEE  SSS       EEEEEEEE  NN  NN  NN      TT      SSS\n  -----------   ---           PP       RRRR      EE           SSS    EE        NN   NN NN      TT         SSS\n ---       ---  ----------    PP       RR  RR    EE        SS   SS   EE        NN    NNNN      TT      SS   SS\n---         --- ----------    PP       RR   RRR  EEEEEEEE  SSSSSSS   EEEEEEEE  NN     NNN      TT      SSSSSSS\n \n")
lt = ["@", "4", "ß", "8","<", "(", "3", "€", "ƒ", "9", "6", "H", "!", "|", "j", "l", "L", "|V|", "/\\/", "0", "®", "5", "$", "+", "7", "Ш", "%", "¥", "2"] 
lf = ["a", "A", "b", "B", "c", "C", "e", "E", "f", "g", "G", "#", "i", "I", "¿", "1", "£", "M", "N", "O", "R", "s", "S", "t", "T", "W", "X", "Y", "Z"]
starting = (input(" -h                  --help ==========> Shows how to use. \n -v               --version ==========> Shows software version. \n -w       --wordlist_import ==========> Use to import your wordlist. \n -u                   --use ==========> Use to start program. \n -e                  --exit ==========> Use to exit WORGEN \n\n Enter your option: \n ").strip()).lower()
nswr = ["u", "-u", "h", "-h", "v", "-v", "w ", "-w ", "e", "-e"]
while starting not in nswr and "w " not in starting:
	print("\n______________________________________________________\n______________YOU MUST SELECT AN OPTION!______________\n-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
	starting = (input(" -h                  --help ==========> Shows how to use. \n -v               --version ==========> Shows software version. \n -w       --wordlist_import ==========> Use to import your wordlist. \n -u                   --use ==========> Use to start program. \n -e                  --exit ==========> Use to exit WORGEN \n\n Enter your option: \n ").strip()).lower()
if "w " in starting:
	starting1 = ((starting.replace("-", "")).replace("w", "")).strip()
	while os.path.isfile(starting1) == False:
		print("You must enter the correct file path!!!\n")
		starting = (input(" -h                  --help ==========> Shows how to use. \n -v               --version ==========> Shows software version. \n -w       --wordlist_import ==========> Use to import your wordlist. \n -u                   --use ==========> Use to start program. \n -e                  --exit ==========> Use to exit WORGEN \n\n Enter your option: \n ").strip()).lower()
		starting1 =  ((starting.replace("-", "")).replace("w", "")).strip()
	if os.path.isfile(starting1) == True:
		starting1 =  ((starting.replace("-", "")).replace("w", "")).strip()
		starting = "-w " + starting1
#Standart Use Section
if starting == "-u" or starting == "u" or "-w" in starting:
	filename = (input("File Name: ").strip()) + ".txt"
	while filename == ".txt":
		print("You must enter a name for wordlist name!!!\n")
		filename = (input("File Name: ").strip()) + ".txt"
	f = open(filename, "wt")
	if starting == "-u" or starting == "u":
		chc= (input("Do you want to add letters or words? l/w: ").strip()).lower()
		while chc != "l" and chc != "w":
			print("You must enter a valid value!!!\n")
			chc = (input("Do you want to add letters or words? l/w: ").strip()).lower()
	else:
		pass
	permi = input("Minimum Combination (Recommended: [1-50]): ").strip()
	try:
		int(permi)
	except:
		print("You must enter a valid value!!!")
		permi = input("Minimum Combination (Recommended: [1-50]): ").strip()
	perm = input("Maximum Combination (Recommended: [1-50]): ").strip()
	try:
		int(perm)
	except:
		print("You must enter a valid value!!!")
		perm = input("Maximum Combination (Recommended: [1-50]): ").strip()
	while int(permi) > int(perm):
		print("You can't enter the minimum combination greater than the maximum combination, please try again")
		permi = input("Minimum Combination (Recommended: [1-50]): ").strip()
		perm = input("Maximum Combination (Recommended :[1-50]): ").strip()
	korllist = []
	if "-w " in starting or "w " in starting:
		korllist = (((open(((starting.replace("w ", "")).replace("-", "")).strip(), "rt", encoding = "utf-8")).read().replace(" ","")).replace("\n\n","\n")).split("\n")
		while "" in korllist:
			korllist.remove("")
	elif starting == "-u" or starting == "u":
		if chc == "w":
			clclt = 1
			keywordnumb = input("How many words will you enter (Recommended: [1-50]): ").strip()
			try:
				int(keywordnumb)
			except:
				print("You must enter a valid value!!!")
				keywordnumb = input("How many words will you enter (Recommended: [1-50]): ").strip()
			while int(keywordnumb) >= clclt:
				AL = input(("Keyword {}: ").format(clclt)).strip()
				korllist.append(AL)
				clclt += 1
		if chc == "l":
			ALK = (input("Do you want LOWERCASE letters? ('y' or 'n'): ").strip()).lower()
			while ALK != "y" and ALK != "n":
				print("You must enter a valid value!!!\n")
				ALK = (input("Do you want LOWERCASE letters? ('y' or 'n'): ").strip()).lower()
			if ALK == "y":
				an1 = ["a", "b", "c", "d", "e", "f", "g", "h", "ı", "j", "k", "l", "m", "n", "o", "q", "p", "r", "s", "t", "u", "v", "y", "z", "x", "w"]
				korllist.extend(an1)
			else:
				pass
			ALK1 = (input("Do you want UPPERCASE letters? ('y' or 'n'): ").strip()).lower()
			while ALK1 != "y" and ALK1 != "n":
				print("You must enter a valid value!!!\n")
				ALK1 = (input("Do you want UPPERCASE letters? ('y' or 'n'): ").strip()).lower()
			if ALK1 == "y":
				an2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "V", "Y", "Z", "Q", "X", "W"]
				korllist.extend(an2)
			else:
				pass
	addnum = (input("Do you want numbers? ('y' or 'n'): ").strip()).lower()
	while addnum != "y" and addnum != "n":
		print("You must enter a valid value!!!\n")
		addnum = (input("Do you want numbers? ('y' or 'n'): ").strip()).lower()
	if addnum == "y":
		numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		korllist.extend(numlist)
	else:
		pass
	addspecial = (input("Do you want special characters (#,@,$,&,/,?,*,_,-,%,+,|,=)? ('y' or 'n'): ").strip()).lower()
	while addspecial != "y" and addspecial != "n":
		print("You must enter a valid value!!!\n")
		addspecial = (input("Do you want special characters (#,@,$,&,/,?,*,_,-,%,+,|,=)? ('y' or 'n'): ").strip()).lower()
	if addspecial == "y":
		speciallist = ["#", "@", "$", "&", "/", "\\", "?", "*", "_", "-", "%", "+", "|", "="]
		korllist.extend(speciallist)
	else:
		pass
	addbday = (input("Do you want to add birthday year? ('y' or 'n'): ").strip()).lower()
	while addbday != "y" and addbday != "n":
		print("You must enter a valid value!!!\n")
		addbday = (input("Do you want to add birthday year? ('y' or 'n'): ").strip()).lower()
	if addbday == "y":
		fromy = (input("From what year: ").strip())
		try:
			int(fromy)
		except:
			print("You must enter a valid birthday!!!")
			fromy = (input("From what year: ").strip())
		fromu = (input("Until what year: ").strip())
		try:
			int(fromu)
		except:
			print("You must enter a valid birthday!!!")
			fromu = (input("Until what year: ").strip())
		while int(fromy) > int(fromu):
			print("The first entered date must be greater than or equal to the second.")
			fromy = (input("From what year: ").strip())
			try:
				int(fromy)
			except:
				print("You must enter a valid birthday!!!")
				fromy = (input("From what year: ").strip())
			fromu = (input("Until what year: ").strip())
			try:
				int(fromu)
			except:
				print("You must enter a valid birthday!!!")
				fromu = (input("Until what year: ").strip())
		while int(fromy) <= int(fromu):
			try:
				fromy = str(fromy)
				korllist.append(fromy)
				fromy = int(fromy)
				fromy += 1
			except:
				pass
	else:
		pass
	addleet = (input("Do you want to add leetcode of keywords? ('y' or 'n'): ").strip()).lower()
	while addleet != "y" and addleet != "n":
		print("You must enter a valid value")
		addleet = (input("Do you want to add leetcode of keywords? ('y' or 'n'): ").strip()).lower()
	if addleet == "y":
		nr = 0
		for rlf in lf:
			rlt = lt[nr]
			for elt in korllist:
				nelt = elt.replace(rlf, rlt)
				if nelt != elt:
					korllist.append(nelt)
			nr += 1		
	else:		
		pass
	addreverse = (input("Do you want to add reverse of the keywords? ('y' or 'n'): "))
	while addreverse != "y" and addreverse != "n":
		print("You must enter a valid value!!!\n")
		addreverse = (input("Do you want to add reverse of the keywords? ('y' or 'n'): ").strip()).lower()
	if addreverse == "y":
		i = 0
		reverselist = []
		while i < len(korllist):
			reverselist.append("".join(reversed(korllist[i])))
			i += 1
		korllist.extend(reverselist)
	else:
		pass
	adddif = (input("Do you want to add something different? ('y' or 'n'): ").strip()).lower()
	while adddif != "y" and adddif != "n":
		print("You must enter a valid value!!!\n")
		adddif = (input("Do you want to add something different? ('y' or 'n'): ").strip()).lower()
	if adddif == "y":
		diflist = (input(" (Warning: Put space between the elements you want to add!)\n What would you like to add:").strip()).split(" ")
		korllist.extend(diflist)
	else:
		pass
	#Print Section
	printq = (input("Which way would you like to print? (hyper speed print = 'HSP', normal print = 'NP', 'dont print = DP'): ").strip()).lower()
	while printq != "hsp" and printq != "np" and printq != "dp":
		print("You must enter a valid value!!!\n")
		printq = (input("Which way would you like to print? (hyper speed print = 'hsp', normal print = 'np', 'dont print = dp'): ").strip()).lower()
	while int(perm) > int(permi) - 1:
		while "" in korllist:
			korllist = list(set(korllist.remove("")))
		permi = int(permi)
		permi += 1 
		for a1 in product((korllist), repeat = permi - 1):
			str(a1)
			a = "".join(a1)
			if printq == "np":
				print(a, file=f)
				print(a)
			elif printq == "hsp":
				print(a, file=f)
				print(a)
				time.sleep(00000.09)
				if os.name == "posix":
					os.system("clear")
				elif os.name == "nt":
					os.system("cls")
			elif printq == "dp":
				print(a, file=f)
	print("Print successful.")
#Help Section
elif starting == "-h" or starting == "h" or starting=="-H" or starting == "H":
	print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nFIRST OF ALL, WELCOME TO 'WORGEN'.\n\n\n\n\n 'WORGEN' is a program that will help you with your personal and random wordlist preparation.\n\n If you want, \nyou can start using the program directly with the '-u' command. \nAfter typing this command, you will  have two options:\n \n1. By selecting the letter (l) option, you can process the letters that you want among themselves. \n \n(NOTE: if your alphabet is different, or if you don't want to permutate all uppercase letters and all lowercase letters, etc., \nor if you have special letters to include in the process, answer all questions as 'No' (N) \nafter selecting the letter option, Do you want to add anything? 'to the question' Yes' (Y), \nyou can manually enter your own characters or special letters and permutate it.) \n(In case you prefer this path, be careful, you do not need to type a space between letters or write any characters. Correct example is: abcd258.,! -) \n\n2. After selecting the option words (w), you can set the maximum and minimum combinations as you wish, after entering 1-30 keywords about the victim, you can start the permutation progress. \n\n(NOTE: You do not need to enter random numbers in the keywords section. Just say yes to the question  \n'Would you like to add a random number?'\n(Note:In case you want to enter less than 30 words, you can press enter and pass the blank word questions.\nThe blank words and duplicates will be deleted.) \n \n \n \nIf you want to process more than 30 words, write as many keywords as you want in a text file. \nThen, you can continue the operation after typing '-w' and entering it you must write the filename with the type of the file.Then enter the maximum and minimum number of permutations. \nIn this method, you can enter maximum' 6 'in the maximum permutation section.) \nAnd please, write words for each line in your wordlist \n\n\n\nBesides all these, you can see which version you are using by typing the' -v 'command. \n\n:):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):)")
#Show Version Section
elif starting == "-v" or starting == "v" or starting=="-V" or starting == "V":
	print("version v1.1")
#Exit Section
if starting == "e" or starting == "-e" or starting == "E" or starting == "-E":
	raise SystemExit()