print("- \n      ---       ---           PPPPPP   RRRRRR    EEEEEEEE  SSSSSSS   EEEEEEEE  NNN     NN  TTTTTTTTTT  SSSSSSS\n    --- ---     ---           PP   PP  RR   RR   EE        SS   SSS  EE        NN NN   NN      TT      SS   SSS\n   ---   ---    ---           PPPPPP   RRRRRR    EEEEEEEE  SSS       EEEEEEEE  NN  NN  NN      TT      SSS\n  -----------   ---           PP       RRRR      EE           SSS    EE        NN   NN NN      TT         SSS\n ---       ---  ----------    PP       RR  RR    EE        SS   SS   EE        NN    NNNN      TT      SS   SS\n---         --- ----------    PP       RR   RRR  EEEEEEEE  SSSSSSS   EEEEEEEE  NN     NNN      TT      SSSSSSS\n \n")
starting = input(" -h         --help ==========>Shows how to use. \n -v      --version ==========> Shows software version. \n -w FILENAME       ==========> Use to import your wordlist. \n -u          --use ==========> Use to start program. \n \n Enter your option: \n ")
#Standart Use Section
if starting == "-u" or starting == "u" or starting=="-U" or starting == "U":
     filename= (input("File Name:").strip()) + ".txt"
     f = open(filename, 'wt')
     chc= input ("Do you want to add letters or words? l/w:").strip()
     while chc != "l" and chc != "w":
          print("You must enter a valid value!!!")
          chc= input ("Do you want to add letters or words? l/w:").strip()
     #Word Choice Section
     if chc == "w":
         permi = input("Minimum Combination (1-15):")
         perti = int(permi) -1
         perm = input("Maximum Combination (1-15):")
         pert = int(perm)
         AL1 = input ("Keyword1:").strip()
         AL2 = input ("Keyword2:").strip()
         AL3 = input ("Keyword3:").strip()
         AL4 = input ("Keyword4:").strip()
         AL5 = input ("Keyword5:").strip()
         AL6 = input ("Keyword6:").strip()
         AL7 = input ("Keyword7:").strip()
         AL8 = input ("Keyword8:").strip()
         AL9 = input ("Keyword9:").strip()
         AL10 = input ("Keyword10:").strip()
         AL11 = input ("Keyword11:").strip()
         AL12 = input ("Keyword12:").strip()
         AL13 = input ("Keyword13:").strip()
         AL14 = input ("Keyword14:").strip()
         AL15 = input ("Keyword15:").strip()
         AL16 = input ("Keyword16:").strip()
         AL17 = input ("Keyword17:").strip()
         AL18 = input ("Keyword18:").strip()
         AL19 = input ("Keyword19:").strip()
         AL20 = input ("Keyword20:").strip()
         AL21 = input ("Keyword21:").strip()
         AL22 = input ("Keyword22:").strip()
         AL23 = input ("Keyword23:").strip()
         AL24 = input ("Keyword24:").strip()
         AL25 = input ("Keyword25:").strip()
         AL26 = input ("Keyword26:").strip()
         AL27 = input ("Keyword27:").strip()
         AL28 = input ("Keyword28:").strip()
         AL29 = input ("Keyword29:").strip()
         AL30 = input ("Keyword30:").strip()
         AL31 = "1"
         AL32 = "2"
         AL33 = "3"
         AL34 = "4"
         AL35 = "5"
         AL36 = "6"
         AL37 = "7"
         AL38 = "8"
         AL39 = "9"
         AL40 = "0"
         chd = input("Do you want numbers (1234567890)? (Y or N):")
         #Print Section
         if chd == "Y" and chd == "y":
             while pert > perti:
                 perti += 1
                 from itertools import product
                 for a1 in product((AL1, AL2, AL3, AL4, AL5, AL6, AL7, AL8, AL9, AL10, AL11, AL12, AL13, AL14, AL15, AL16, AL17, AL18, AL19, AL20, AL21, AL22, AL23, AL24, AL25, AL26, AL27, AL28, AL29, AL30,
                 AL31, AL32, AL33, AL34, AL35, AL36, AL37, AL38, AL39, AL40 ), repeat =perti):
                     str(a1)
                     a = "".join(a1)
                     print(a)
                     print(a, file=f)         
         while pert > perti:
             perti += 1
             from itertools import product
             for a1 in product((AL1, AL2, AL3, AL4, AL5, AL6, AL7, AL8, AL9, AL10, AL11, AL12, AL13, AL14, AL15, AL16, AL17, AL18, AL19, AL20, AL21, AL22, AL23, AL24, AL25, AL26, AL27, AL28, AL29, AL30, ), repeat =perti):
                 str(a1)
                 a = "".join(a1)
                 print(a)
                 print(a, file=f)
     #Letter Choice Section
     elif chc == "l":
         permi = input("Min Output Word Length (1-15):")
         perti = int(permi) -1
         perm = input("Max Output Word Length (1-15):")
         pert = int(perm)
         an1 = ""
         ALK = input ("Do you want lowercase letters? y/n:").strip()
         if ALK == "y":
             an1="abcdefghıjklmnoqprstuvyzxw"
         else:
             if ALK == "Y":
                 an1 == "abcdefghıjklmnoqprstuvyzxw"
             else:
                 pass
         while ALK != "y" and ALK != "Y" and ALK != "n" and ALK != "N":
             print("You must enter a valid value!!!")
             ALK = input ("Do you want lowercase letters? y/n:").strip()
         ALK1 = input("Do you want uppercase letters? y/n:")
         if ALK1 == "y":
             an1 += "ABCDEFGHIJKLMNOPRSTUVYZQXW"
         else:
             if ALK1 == "Y":
                 an1 += "ABCDEFGHIJKLMNOPRSTUVYZQXW"
             else:
                 pass
         while ALK1 != "y" and ALK1 != "Y" and ALK1 != "n" and ALK1 != "N":
             print("You must enter a valid value!!!")
             ALK1 = input("Do you want uppercase letters? y/n:")
         ALK2 = input("Do you want numbers? y/n:")
         if ALK2 == "y":
             an1 += "1234567890"
         else:
             if ALK2 == "Y":
                 an1 += "1234567890"
             else:
                 pass
         while ALK2 != "y" and ALK2 != "Y" and ALK2 != "n" and ALK2 != "N":
             print("You must enter a valid value!!!")
             ALK2 = input("Do you want numbers? y/n:")
         ALK3 = input("Do you want special characters (!,-,_,?,*,#,&)? y/n:")
         if ALK3 == "y":
             an1 += "!-*_?#&"
         else:
             if ALK3 == "Y":
                 an1 += "!-*_?#&"
             else:
                 pass
         while ALK3 != "y" and ALK3 != "Y" and ALK3 != "n" and ALK3 != "N":
             print("You must enter a valid value!!!")
             ALK3 = input("Do you want special characters (!,-,_,?,*,#,&)? y/n:")
         ALK4 = input("Do you want to add something different? y/n:")
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
                 print("Successful.")

                 count=0
     with open(filename, 'r') as f:
         for line in f:
             count += 1
     print("Total Lines:", count)
#Help Section
elif starting == "-h" or starting == "h" or starting=="-H" or starting == "H":
    print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n\nFIRST OF ALL, WELCOME TO 'WORGEN'.\n\n\n\n\n 'WORGEN' is a program that will help you with your personal and random wordlist preparation.\n\n If you want, \nyou can start using the program directly with the '-u' command. \nAfter typing this command, you will  have two options:\n \n1. By selecting the letter (l) option, you can process the letters that you want among themselves. \n \n(NOTE: if your alphabet is different, or if you don't want to permutate all uppercase letters and all lowercase letters, etc., \nor if you have special letters to include in the process, answer all questions as 'No' (N) \nafter selecting the letter option, Do you want to add anything? 'to the question' Yes' (Y), \nyou can manually enter your own characters or special letters and permutate it.) \n(In case you prefer this path, be careful, you do not need to type a space between letters or write any characters. Correct example is: abcd258.,! -) \n\n2. After selecting the option words (w), you can set the maximum and minimum combinations as you wish, after entering 1-30 keywords about the victim, you can start the permutation progress. \n\n(NOTE: You do not need to enter random numbers in the keywords section. Just say yes to the question  \n'Would you like to add a random number?'\n(Note:In case you want to enter less than 30 words, you can press enter and pass the blank word questions.\nThe blank words and duplicates will be deleted.) \n \n \n \nIf you want to process more than 30 words, write as many keywords as you want in a text file. \nThen, you can continue the operation after typing '-w' + 'the location of the mini wordlist you have created' and entering the maximum and minimum number of permutations. \nIn this method, you can enter maximum' 6 'in the maximum permutation section.) \n\n\n\nBesides all these, you can see which version you are using by typing the' -v 'command. \n\n:):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):):)")
#Show Version Section
elif starting == "-v" or starting == "v" or starting=="-V" or starting == "V":
    print("version BETA v1.0")
#Wordlist Section
elif "-w" in starting or "w" in starting or "-W" in starting or "W" in starting:
    permi = input("Minimum Combination:")
    perti = int(permi)
    while permi !="1" and permi !="2" and permi !="3" and permi !="4" and permi !="5" and permi !="6":
        print("You must enter a value lesser than 6.")
        permi = input("Minimum Combination:")
        perti = int(permi)
    perm = input("Maximum Combination:")
    pert = int(perm)
    while perm !="1" and perm !="2" and perm !="3" and perm !="4" and perm !="5" and perm !="6":
        print("You must enter a value lesser than 6.")
        perm = input("Maximum Combination:")
        pert = int(perm)
    starstr = str(starting)
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
    if permi == 1:
        pass
    elif perti == 2:
        with open("outold.txt",'r') as f:
            d=set(f.readlines())
        with open(starst,'r') as f:
            e=set(f.readlines())
        open('output.txt','w').close() 
        with open('output.txt','a') as f:
            for line in list(d-e):
               f.write(line)
    elif perti == 3:
        filenames = [starst, "twice.txt"]
        with open('sub.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
    elif perti == 4:
        filenames = [starst, "twice.txt", "threet.txt"]
        with open('sub.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
    elif perti == 5:
        filenames = [starst, "twice.txt", "threet", "fourt"]
        with open('sub.txt', 'w') as outfile:
            for fname in filenames:
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(line)
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
    with open("output.txt") as result:
             uniqlines = set(result.readlines())
             with open(filename, 'w') as rmdup:
                 rmdup.writelines(set(uniqlines))
                 print("Successful.")

                 count=0
    with open("output.txt", 'r') as f:
        for line in f:
            count += 1
    print("Total Lines:", count)
    #Removing Unnecessary Files
    import os
    os.remove("twice.txt")
    os.remove("threet.txt")
    os.remove("fourt.txt")
    os.remove("fivet.txt")
    os.remove("sixt.txt")
    os.remove("outold.txt")
    os.remove(starst2)
            