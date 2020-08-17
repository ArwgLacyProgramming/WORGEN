print("- \n      ---       ---           PPPPPP   RRRRRR    EEEEEEEE  SSSSSSS   EEEEEEEE  NNN     NN  TTTTTTTTTT  SSSSSSS\n    --- ---     ---           PP   PP  RR   RR   EE        SS   SSS  EE        NN NN   NN      TT      SS   SSS\n   ---   ---    ---           PPPPPP   RRRRRR    EEEEEEEE  SSS       EEEEEEEE  NN  NN  NN      TT      SSS\n  -----------   ---           PP       RRRR      EE           SSS    EE        NN   NN NN      TT         SSS\n ---       ---  ----------    PP       RR  RR    EE        SS   SS   EE        NN    NNNN      TT      SS   SS\n---         --- ----------    PP       RR   RRR  EEEEEEEE  SSSSSSS   EEEEEEEE  NN     NNN      TT      SSSSSSS\n \n")
starting = input(" -h                  --help ==========> Shows how to use. \n -v               --version ==========> Shows software version. \n -w       --wordlist_import ==========> Use to import your wordlist. \n -u                   --use ==========> Use to start program. \n -e                  --exit ==========> Use to exit WORGEN \n\n Enter your option: \n ").strip()
while starting != 'u' and starting != '-u' and starting != 'U' and starting != '-U' and starting != 'h' and starting != '-h' and starting != 'H' and starting != '-H' and starting != 'v' and starting != '-v' and starting != 'V' and starting != '-V' and starting != "w" and starting != "-w" and starting != "W"  and starting != "-W" and starting != "e" and starting != "-e" and starting != "E" and starting != "-E":
    print("\n______________________________________________________\n______________YOU MUST SELECT AN OPTION!______________\n-------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    starting = input(" -h                  --help ==========> Shows how to use. \n -v               --version ==========> Shows software version. \n -w       --wordlist_import ==========> Use to import your wordlist. \n -u                   --use ==========> Use to start program. \n -e                  --exit ==========> Use to exit WORGEN \n\n Enter your option: \n ").strip()
#Standart Use Section
if starting == "-u" or starting == "u" or starting=="-U" or starting == "U":
     filename= (input("File Name: ").strip()) + ".txt"
     f = open(filename, "wt")
     chc= input ("Do you want to add letters or words? l/w: ").strip()
     while chc != "l" and chc != "w":
          print("You must enter a valid value!!!")
          chc= input ("Do you want to add letters or words? l/w: ").strip()
     #Word Choice Section
     if chc == "w":
         permi = input("Minimum Combination (1-15): ").strip()
         while permi != '1' and permi != '2' and permi != '3' and permi != '4' and permi != '5' and permi != '6' and permi != '7' and permi != '8' and permi != '9' and permi != '10' and permi != '11' and permi != '12' and permi != '13' and permi != '14' and permi != '15':
             print("You must enter valid value (1-15): ")
             permi = input("Minimum Combination (1-15): ").strip()
         rsltminmax = int(permi)
         perti = rsltminmax -1
         perm = input("Maximum Combination (1-15): ").strip()
         while perm != '1' and perm != '2' and perm != '3' and perm != '4' and perm != '5' and perm != '6' and perm != '7' and perm != '8' and perm != '9' and perm != '10' and perm != '11' and perm != '12' and perm != '13' and perm != '14' and perm != '15':
             print("You must enter valid value (1-15): ")
             perm = input("Maximum Combination (1-15): ").strip()
         pert = int(perm)
         while rsltminmax > pert:
             print("You can't enter the minimum combination greater than the maximum combination, please try again")
             permi = input("Minimum Combination (1-15): ").strip()
             perti = int(permi) -1
             perm = input("Maximum Combination (1-15): ").strip()
             pert = int(perm)
         print("\n-_-_-_-Please don't put spaces in your keywords-_-_-_-\n")
         AL1 = input ("Keyword1: ").strip()
         AL2 = input ("Keyword2: ").strip()
         AL3 = input ("Keyword3: ").strip()
         AL4 = input ("Keyword4: ").strip()
         AL5 = input ("Keyword5: ").strip()
         AL6 = input ("Keyword6: ").strip()
         AL7 = input ("Keyword7: ").strip()
         AL8 = input ("Keyword8: ").strip()
         AL9 = input ("Keyword9: ").strip()
         AL10 = input ("Keyword10: ").strip()
         AL11 = input ("Keyword11: ").strip()
         AL12 = input ("Keyword12: ").strip()
         AL13 = input ("Keyword13: ").strip()
         AL14 = input ("Keyword14: ").strip()
         AL15 = input ("Keyword15: ").strip()
         AL16 = input ("Keyword16: ").strip()
         AL17 = input ("Keyword17: ").strip()
         AL18 = input ("Keyword18: ").strip()
         AL19 = input ("Keyword19: ").strip()
         AL20 = input ("Keyword20: ").strip()
         AL21 = input ("Keyword21: ").strip()
         AL22 = input ("Keyword22: ").strip()
         AL23 = input ("Keyword23: ").strip()
         AL24 = input ("Keyword24: ").strip()
         AL25 = input ("Keyword25: ").strip()
         AL26 = input ("Keyword26: ").strip()
         AL27 = input ("Keyword27: ").strip()
         AL28 = input ("Keyword28: ").strip()
         AL29 = input ("Keyword29: ").strip()
         AL30 = input ("Keyword30: ").strip()
         N =  "0"
         N1 = "1"
         N2 = "2"
         N3 = "3"
         N4 = "4"
         N5 = "5"
         N6 = "6"
         N7 = "7"
         N8 = "8"
         N9 = "9"
         c1 = "!"
         c2 = "#"
         c3 = "@"
         c4 = "$"
         c5 = "&"
         c6 = "/"
         c7 = "\\"
         c8 = "?"
         c9 = "*"
         c10 = "-"
         c11 = "_"
         c12 = "%"
         c13 = "+"
         c14 = "="
         c15 = "|"
         result = AL1, AL2, AL3, AL4, AL5, AL6, AL7, AL8, AL9, AL10, AL11, AL12, AL13, AL14, AL15, AL16, AL17, AL18, AL19, AL20, AL21, AL22, AL23, AL24, AL25, AL26, AL27, AL28, AL29, AL30
         q1 = input("Do you want numbers (1234567890)? ('y' or 'n'): ").strip()
         while q1 != 'y' and q1 != 'Y' and q1 != 'n' and q1 != 'N':
             print("You must enter y or n !")
             q1 = input("Do you want numbers (1234567890)? ('y' or 'n'): ").strip()
         if q1 == 'y' or q1 == 'Y':
             result += N1, N2, N3, N4, N5, N6, N7, N8, N9, N
         if q1 == 'n' or q1 == 'N':
             pass 
         q2 = input(r"Do you want to add special characters (!,#,@,$,&,/,\,?,*,_,-,%,+,|,=)? ('y' or 'n'): ").strip()
         while q2 != 'y' and q2 != 'Y' and q2 != 'n' and q2 != 'N':
             print("You must enter y or n !")
             q2 = input(r"Do you want to add special characters (!,#,@,$,&,/,\,?,*,_,-,%,+,|,=)? ('y' or 'n'): ").strip()
         if q2 == 'y' or q2 == 'Y':
             result += c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15
         if q2 == 'n' or q2 == 'N':
             pass
         #Print Section
         while pert > perti: 
             perti += 1
             from itertools import product
             for a1 in product((result), repeat =perti):
                 str(a1)
                 a = "".join(a1)
                 print(a, file=f)   
                
                 #print(a.replace(" ", ""))
     #Letter Choice Section
     elif chc == "l":
         permi = input("Minimum Combination (1-15): ").strip()
         while permi != '1' and permi != '2' and permi != '3' and permi != '4' and permi != '5' and permi != '6' and permi != '7' and permi != '8' and permi != '9' and permi != '10' and permi != '11' and permi != '12' and permi != '13' and permi != '14' and permi != '15':
             print("You must enter valid value (1-15): ")
             permi = input("Minimum Combination (1-15): ").strip()
         perti = int(permi) -1
         perm = input("Maximum Combination (1-15): ").strip()
         while perm != '1' and perm != '2' and perm != '3' and perm != '4' and perm != '5' and perm != '6' and perm != '7' and perm != '8' and perm != '9' and perm != '10' and perm != '11' and perm != '12' and perm != '13' and perm != '14' and perm != '15':
             print("You must enter valid value (1-15): ")
             perm = input("Maximum Combination (1-15): ").strip()
         pert = int(perm)
         an1 = ""
         ALK = input ("Do you want lowercase letters? ('y' or 'n'): ").strip()
         if ALK == "y":
             an1="abcdefghıjklmnoqprstuvyzxw"
         else:
             if ALK == "Y":
                 an1 == "abcdefghıjklmnoqprstuvyzxw"
             else:
                 pass
         while ALK != "y" and ALK != "Y" and ALK != "n" and ALK != "N":
             print("You must enter a valid value!!!")
             ALK = input ("Do you want lowercase letters? ('y' or 'n'): ").strip()
         ALK1 = input("Do you want uppercase letters? ('y' or 'n'): ").strip()
         if ALK1 == "y":
             an1 += "ABCDEFGHIJKLMNOPRSTUVYZQXW"
         else:
             if ALK1 == "Y":
                 an1 += "ABCDEFGHIJKLMNOPRSTUVYZQXW"
             else:
                 pass
         while ALK1 != "y" and ALK1 != "Y" and ALK1 != "n" and ALK1 != "N":
             print("You must enter a valid value!!!")
             ALK1 = input("Do you want uppercase letters? ('y' or 'n'): ")
         ALK2 = input("Do you want numbers? ('y' or 'n'): ")
         if ALK2 == "y":
             an1 += "1234567890"
         else:
             if ALK2 == "Y":
                 an1 += "1234567890"
             else:
                 pass
         while ALK2 != "y" and ALK2 != "Y" and ALK2 != "n" and ALK2 != "N":
             print("You must enter a valid value!!!")
             ALK2 = input("Do you want numbers? ('y' or 'n'): ")
         ALK3 = input("Do you want special characters (,#,@,$,&,/,?,*,_,-,%,+,|,=)? ('y' or 'n'): ")
         if ALK3 == "y":
             an1 += "#@$&/?*_-%+|="
         else:
             if ALK3 == "Y":
                 an1 += "#@$&/?*_-%+|="
             else:
                 pass
         while ALK3 != "y" and ALK3 != "Y" and ALK3 != "n" and ALK3 != "N":
             print("You must enter a valid value!!!")
             ALK3 = input("Do you want special characters (,#,@,$,&,/,?,*,_,-,%,+,|,=)? ('y' or 'n'): ")
         ALK4 = input("Do you want to add something different? ('y' or 'n'): ")
         if ALK4 == "y":
             ALK5 = input("WARNING:Do not put spaces or any other thing between the words.Correct Example:abcdefg \n \nAdd: \n")
             an1 += ALK5
         else:
             if ALK4 == "Y":
                 ALK5 == input("WARNING:Do not put spaces or any other thing between the words.Correct Example:abcdefg \n \nAdd: \n")
                 an1 +=ALK5
             else:
                 pass
         while ALK4 != "y" and ALK4 != "Y" and ALK4 != "n" and ALK4 != "N":
             print("You must enter a valid value!!!")
             ALK4 = input("Do you want to add something different? y/n:")
     #Print Section 
     while pert > perti:
         perti += 1    
         from itertools import product
         for klm1 in product((an1), repeat = perti):
             klm = "".join(klm1)
             print(klm, file=f)  
     f.close()
     with open(filename) as result:
             uniqlines = set(result.readlines())
             with open(filename, 'w') as rmdup:
                 rmdup.writelines(set(uniqlines))

     import time
     import os   
     printquestion= input("Do you want to display print?(Y or N):").strip()  
     while printquestion != "y" and printquestion != "Y" and printquestion != "n" and printquestion != "N" :
          print("You must enter a valid value!!!")
          printquestion= input("Do you want to display print?(Y or N):").strip()
     if printquestion == "Y" or printquestion == "y":
         hyperq= input ("Do you want to print at hyperspeed?(Y or N):")
         while hyperq != "y" and hyperq != "Y" and hyperq != "n" and hyperq != "N" :
             print("You must enter a valid value!!!")
             hyperq= input ("Do you want to print at hyperspeed?(Y or N):")
         if hyperq == "Y" or hyperq == "y":
             f
             with open(filename, "r+") as wlist:
                      data = wlist.readlines()
                      for line in data:
                           print("\033[1;32m[" + filename + "] \033[1;33m" + line)
                           time.sleep(00000.09)
                           if os.name == "posix":
                               os.system("clear")
                           elif os.name == "nt":
                               os.system("cls")
         else:
             with open(filename, "r+") as wlist:
                 data = wlist.readlines()
                 for line in data:
                     liner= os.linesep.join([s for s in line.splitlines() if s])
                     print(liner)
                     time.sleep(0.03)      
     else:pass
     print("Successful.") 
     with open(filename, 'r') as f:
         count=0
         for line in f:
             count += 1
     print("Total Lines:", count) 
#Help Section
elif starting == "-h" or starting == "h" or starting=="-H" or starting == "H":
    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nFIRST OF ALL, WELCOME TO 'WORGEN'.\n\n\n\n\n 'WORGEN' is a program that will help you with your personal and random wordlist preparation.\n\n If you want, \nyou can start using the program directly with the '-u' command. \nAfter typing this command, you will  have two options:\n \n1. By selecting the letter (l) option, you can process the letters that you want among themselves. \n \n(NOTE: if your alphabet is different, or if you don't want to permutate all uppercase letters and all lowercase letters, etc., \nor if you have special letters to include in the process, answer all questions as 'No' (N) \nafter selecting the letter option, Do you want to add anything? 'to the question' Yes' (Y), \nyou can manually enter your own characters or special letters and permutate it.) \n(In case you prefer this path, be careful, you do not need to type a space between letters or write any characters. Correct example is: abcd258.,! -) \n\n2. After selecting the option words (w), you can set the maximum and minimum combinations as you wish, after entering 1-30 keywords about the victim, you can start the permutation progress. \n\n(NOTE: You do not need to enter random numbers in the keywords section. Just say yes to the question  \n'Would you like to add a random number?'\n(Note:In case you want to enter less than 30 words, you can press enter and pass the blank word questions.\nThe blank words and duplicates will be deleted.) \n \n \n \nIf you want to process more than 30 words, write as many keywords as you want in a text file. \nThen, you can continue the operation after typing '-w' and entering it you must write the filename with the type of the file.Then enter the maximum and minimum number of permutations. \nIn this method, you can enter maximum' 6 'in the maximum permutation section.) \nAnd please, write words for each line in your wordlist \n\n\n\nBesides all these, you can see which version you are using by typing the' -v 'command. \n\n:):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):)")
#Show Version Section
elif starting == "-v" or starting == "v" or starting=="-V" or starting == "V":
    print("version BETA v1.0")
#Wordlist Section
elif "-w" in starting or "w" in starting or "-W" in starting or "W" in starting:
    listname= input("Filename(ENTER WITH FILE TYPE! Correct Example:list.txt):")
    permi = input("Minimum Combination: ")
    while permi !="1" and permi !="2" and permi !="3" and permi !="4" and permi !="5" and permi !="6":
        print("You must enter a value lesser than 6.")
        permi = input("Minimum Combination: ")
        perti = int(permi)
    perti = int(permi)
    perm = input("Maximum Combination: ")
    while perm !="1" and perm !="2" and perm !="3" and perm !="4" and perm !="5" and perm !="6":
        print("You must enter a value lesser than 6.")
        perm = input("Maximum Combination:")
        pert = int(perm)
    pert = int(perm)
    starstr = str(listname)
    starst = starstr.replace("-w ","")
    #Duplicating File
    starst2 = "2" + starst
    from shutil import copyfile
    copyfile(starst, starst2)
    #Creating Extra Files
    with open(starst, 'r') as l1, open(starst2, 'r') as l2, open('twice.txt', 'w') as l3:
     for left_part in l1:
        for right_part in l2:
            l3.write('%s%s\n' % (left_part.replace("\n",""), right_part.replace("\n","")))
        l2.seek(0)
    with open(starst, 'r') as l1, open("twice.txt", 'r') as l2, open('threet.txt', 'w') as l3:
     for left_part in l1:
        for right_part in l2:
            l3.write('%s%s\n' % (left_part.replace("\n",""), right_part.replace("\n","")))
        l2.seek(0)
    with open(starst, 'r') as l1, open("threet.txt", 'r') as l2, open('fourt.txt', 'w') as l3:
     for left_part in l1:
        for right_part in l2:
            l3.write('%s%s\n' % (left_part.replace("\n",""), right_part.replace("\n","")))
        l2.seek(0)
    with open(starst, 'r') as l1, open("fourt.txt", 'r') as l2, open('fivet.txt', 'w') as l3:
     for left_part in l1:
        for right_part in l2:
            l3.write('%s%s\n' % (left_part.replace("\n",""), right_part.replace("\n","")))
        l2.seek(0)
    with open(starst, 'r') as l1, open("fivet.txt", 'r') as l2, open('sixt.txt', 'w') as l3:
     for left_part in l1:
        for right_part in l2:
            l3.write('%s%s\n' % (left_part.replace("\n",""), right_part.replace("\n","")))
        l2.seek(0) 
    if pert == 2:
     filenames = [starst, "twice.txt"]
     with open('outold.txt', 'w') as outfile:
         for fname in filenames:
             with open(fname) as infile:
                 for line in infile:
                     outfile.write(line)              
    elif pert == 3:
     filenames = [starst, "twice.txt", "threet.txt"]
     with open('outold.txt', 'w') as outfile:
         for fname in filenames:
             with open(fname) as infile:
                 for line in infile:
                     outfile.write(line)
    elif pert == 4:
     filenames = [starst, "twice.txt", "threet.txt", "fourt.txt"]
     with open('outold.txt', 'w') as outfile:
         for fname in filenames:
             with open(fname) as infile:
                 for line in infile:
                     outfile.write(line)
    elif pert == 5:
     filenames = [starst, "twice.txt", "threet.txt", "fourt.txt", "fivet.txt"]
     with open('outold.txt', 'w') as outfile:
         for fname in filenames:
             with open(fname) as infile:
                 for line in infile:
                     outfile.write(line)               
    elif pert == 6:
     filenames = [starst, "twice.txt", "threet.txt", "fourt.txt", "fivet.txt", "sixt.txt"]
     with open('outold.txt', 'w') as outfile:
         for fname in filenames:
             with open(fname) as infile:
                 for line in infile:
                     outfile.write(line)   
    #Merging and Subtracting Files
    if perti == 1:
        import shutil
        shutil.move('outold.txt', 'output.txt')
    elif perti == 2:
        with open("outold.txt",'r') as f:
            d=set(f.readlines())
        with open(starst,'r') as f:
            e=set(f.readlines())
        open('output.txt','w').close() 
        with open('output.txt','a') as f:
            for line in list(d-e):
               f.write(line)
        import os
        os.remove("outold.txt")
    elif perti == 3:
        filenames = [starst, "twice.txt"]
        with open('sub.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
        import os
        os.remove("outold.txt")
    elif perti == 4:
        filenames = [starst, "twice.txt", "threet.txt"]
        with open('sub.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
        import os
        os.remove("outold.txt")
    elif perti == 5:
        filenames = [starst, "twice.txt", "threet", "fourt"]
        with open('sub.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
        import os
        os.remove("outold.txt")
    if perti != 2 and perti != 1:
        with open("outold.txt",'r') as f:
            d=set(f.readlines())
        with open("sub.txt",'r') as f:
            e=set(f.readlines())
        open('output.txt','w').close() 
        with open('output.txt','a') as f:
            for line in list(d-e):
               f.write(line)
        import os
        os.remove("sub.txt")
        os.remove("outold.txt")
    with open("output.txt") as result:
         uniqlines = set(result.readlines())
         with open("output.txt", 'w') as rmdup:
             rmdup.writelines(set(uniqlines))
    #Removing Unnecessary Files
    import os
    os.remove("twice.txt")
    os.remove("threet.txt")
    os.remove("fourt.txt")
    os.remove("fivet.txt")
    os.remove("sixt.txt")
    os.remove(starst2)
    import time
    import os  
    with open("output.txt",) as f:
        with open ("out.txt", "wt") as q:
            q.writelines("".join(line for line in f if not line.isspace()))
    import os 
    os.remove("output.txt")
    os.rename("out.txt","output.txt") 
    printquestion= input("Do you want to display print?(Y or N):").strip()  
    while printquestion != "y" and printquestion != "Y" and printquestion != "n" and printquestion != "N" :
         print("You must enter a valid value!!!")
         printquestion= input("Do you want to display print?(Y or N):").strip()
    if printquestion == "Y" or printquestion == "y":
         hyperq= input ("Do you want to print at hyperspeed?(Y or N):")
         while hyperq != "y" and hyperq != "Y" and hyperq != "n" and hyperq != "N" :
             print("You must enter a valid value!!!")
             hyperq= input ("Do you want to print at hyperspeed?(Y or N):")
         if hyperq == "Y" or hyperq == "y":
             with open("output.txt", "r+") as wlist:
                      data = wlist.readlines()
                      for line in data:
                           print("\033[1;32m[" + "output.txt" + "] \033[1;33m" + line)
                           time.sleep(00000.09)
                           if os.name == "posix":
                               os.system("clear")
                           elif os.name == "nt":
                               os.system("cls")
         else:
             with open("output.txt", "r+") as wlist:
                 data = wlist.readlines()
                 for line in data:
                     liner= os.linesep.join([s for s in line.splitlines() if s])
                     print(liner)
                     time.sleep(0.03)   
    print("Successful.")   
    with open("output.txt", 'r') as f:
         count=0
         for line in f:
             count += 1
         print("Total Lines:", count)
#Exit Section
if starting == "e" or starting == "-e" or starting == "E" or starting == "-E":
    raise SystemExit()