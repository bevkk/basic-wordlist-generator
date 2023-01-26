import itertools
import os
import sys
import time as t
from datetime import timedelta

class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

def main():
    banner()
    an=0
    r=0
    sc=0
    s=[]
    uc=0
    k_words = []
    x = input(bcolors.OKGREEN + "KeyWords[Use ,] :")
    k_words = x.split(",")
    x = input(bcolors.OKGREEN + "AddNumbers[y,n] :")
    if x == "y" or x=="Y":
        an = 1
        r = str(input(bcolors.OKGREEN + "NumbersRange[Use ?-?] :"))
        r = str(r).split("-")
        if(r[0].isnumeric() != True or r[1].isnumeric() != True):
            os.system("clear")
            print(bcolors.FAIL + "That's not a valid range")
            sys.exit()
    elif x == "n" or x== "N":
        pass
    else:
        os.system("clear")
        print(bcolors.FAIL + "That's not a valid range")
        sys.exit()

    x = input(bcolors.OKGREEN + "UpperCase[y,n] : ")
    if x == "y" or x=="Y":
        print(bcolors.WARNING + "!This feature makes the whole password uppercased or only the first letters uppercase!")
        uc = 1
    x = input(bcolors.OKGREEN + "SpecialCharacters[y,n] : ")
    if x == "y" or x=="Y":
        sc = 1
        print(bcolors.WARNING + "!This feature only adds special characters at the end of a password!")
        s = input(bcolors.OKGREEN + "Which special characters[Use space between] : ")
        s = s.split(" ")
    f_name = "wl_" + input(bcolors.OKGREEN + "Save as : ")
    file = open(f_name + ".txt", "w")
    print(bcolors.BOLD + "\nThis may take a while ...\n\n")
    keyWords(k_words,an,r,sc,s,uc,file)
    get_size(f_name[3:] + ".txt")

def banner():
    
    print(bcolors.OKGREEN + ("""
 ____            _   __          ___      
|  _ \          (_)  \ \        / / |     
| |_) | __ _ ___ _  __\ \  /\  / /| |     
|  _ < / _` / __| |/ __\ \/  \/ / | |     
| |_) | (_| \__ \ | (__ \  /\  /  | |____ 
|____/ \__,_|___/_|\___| \/  \/   |______|                  
    \n A basic wordlist generator made by bevkk\n\n"""))

def keyWords(my_list,an,r,sc,s,uc,file):
    start_time = t.time()
    if(an == 1 and sc == 1 and uc == 1):
        for i in range(1,int(len(my_list))+1):
            combinations = list(itertools.combinations(my_list, i))
            for combination in combinations:
                output_string = ''.join(list(combination))
                for j in range(int(r[0]),int(r[1]) +1):
                    for k in s:
                        output_string1 = (output_string + str(j) + k).upper()
                        output_string2 = (output_string + str(j) + k).capitalize()
                        file.write(output_string1+"\n"+output_string2+"\n")
    
    elif(an==1 and sc ==1):
        for i in range(1,int(len(my_list))+1):
            combinations = list(itertools.combinations(my_list, i))
            for combination in combinations:
                output_string = ''.join(list(combination))
                for j in range(int(r[0]),int(r[1]) +1):
                    for k in s:
                        output_string1 = output_string + str(j) + k
                        file.write(output_string1+"\n")

    elif(an==1 and uc==1):
        for i in range(1,int(len(my_list))+1):
            combinations = list(itertools.combinations(my_list, i))
            for combination in combinations:
                output_string = ''.join(list(combination))
                for j in range(int(r[0]),int(r[1]) +1):
                    output_string1 = (output_string + str(j)).upper()
                    output_string2 = (output_string + str(j)).capitalize()
                    file.write(output_string1+"\n"+output_string2+"\n")

    elif(sc==1 and uc==1): #DİKKAT BURAYA!
        for i in range(1,int(len(my_list))+1):
            combinations = list(itertools.combinations(my_list, i))
            for combination in combinations:
                output_string = ''.join(list(combination))
                for k in s:
                    output_string = output_string + k
                    output_string1 = output_string.capitalize()
                    output_string2 = output_string.upper()
                    file.write(output_string1+"\n"+output_string2+"\n")


    elif(an==1):
        for i in range(1,int(len(my_list))+1):
            combinations = list(itertools.combinations(my_list, i))
            for combination in combinations:
                output_string = ''.join(list(combination))
                for j in range(int(r[0]),int(r[1])):
                    output_string1 = output_string + str(j)
                    file.write(output_string1+"\n")

    elif(sc==1):
        for i in range(1,int(len(my_list))+1):
            combinations = list(itertools.combinations(my_list, i))
            for combination in combinations:
                output_string = ''.join(list(combination))
                for k in s:
                    output_string1 = output_string + k
                    file.write(output_string1+"\n")

    elif(uc==1):
        for i in range(1,int(len(my_list))+1):
                combinations = list(itertools.combinations(my_list, i))
                for combination in combinations:
                    output_string = ''.join(list(combination))
                    output_string1 = output_string.capitalize()
                    output_string2 = output_string.upper()
                    
                    file.write(output_string1+"\n"+output_string2+"\n")

    else:
        for i in range(1,int(len(my_list))+1):
                combinations = list(itertools.combinations(my_list, i))
                for combination in combinations:
                    output_string = ''.join(list(combination))
                    file.write(output_string+"\n")
    end_time = t.time()
    duration = end_time - start_time
    print("Duration: ", str(duration)[0:5] + " seconds...")

                    
def get_size(filename):
    file_path = os.getcwd() + r'\wl_' + filename 
    sz = os.path.getsize(file_path)
    print(f'Size of this wordlist : ', sz, 'bytes')
main()
