#!python

import argparse
import sys
import os

def slowsearch(pi,smax,allanswers=False):
    
    answers=[]
    #loop through entire search space
    maxsearch=pow(10,smax)
    prevx=0
    for x in range(0,maxsearch):
        
        if len(str(x)) > len(str(prevx)) and answers and not allanswers:
            return(answers) 
    
        if str(x) not in pi: 
            answers.append(x) 

        prevx=x

    return(answers)
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file",
                        help="path to pi text file",
                        action="store",
                        required=True)
    parser.add_argument("-m", "--max-search",
                        help="max length of search space",
                        action="store")
    parser.add_argument("-j", "--just-the-answers",
                        help="doesn't print and pre/post run info",
                        action="store_true")
    parser.add_argument("-l", "--limit-pi",
                        help="Use only the first x characters of the specified pi file",
                        action="store")
    args = parser.parse_args()
    
    #print("hello world")

    pifile=args.file
    with open(pifile, 'r') as file:
        pi = file.read().replace('.','')

    if args.limit_pi is not None: 
        if int(args.limit_pi) > len(pi):
            print("pi limit set higher than your pi input file")
            sys.exit(1)
        else:
            pi = pi[0:int(args.limit_pi)]

    if args.max_search is None:
        searchlength=len(pi)
    else:
        searchlength=int(args.max_search)
        

    #answers=slowsearch(pi,searchlength) 
    answers=slowsearch(pi,searchlength) 

    if args.just_the_answers:
        print(answers)
        exit()
    if not answers:
        print("We didn't find any missing values in the speicifed search space") 
    elif len(answers) == 1:
        print("The shortest missing value is {}".format(answers)) 
    else:
        print("The following values are tied for shortest missing value : {}".format(answers)) 

    print("----- SEARCH SPACE ------")
    print("pi length : {}".format(len(pi)))
    print("max search length : {}".format(searchlength))
