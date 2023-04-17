#!/usr/bin/python3
import argparse

def method1(pi):

    a=0
    
    for x in pi:
        curdig = int(x)
        if curdig == 0:
            a*=10
        else:
            a=a%curdig
        print(a)

def method2(pi):

    a=0

    for x in pi:
        curdig = int(x)

        if curdig == 0:
            a*=10
        elif a == 0:
            a=curdig
        else:
            a=a%curdig

        print(a)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--file",
                        help="path to pi text file",
                        action="store",
                        required=True)
    parser.add_argument("-l", "--limit-pi",
                        help="Use only the first x characters of the specified pi file",
                        action="store")
    args = parser.parse_args()


    pifile=args.file
    with open(pifile, 'r') as file:
        pi = file.read().replace('.','')

    if args.limit_pi is not None: 
        if int(args.limit_pi) > len(pi):
            print("pi limit set higher than your pi input file")
            sys.exit(1)
        else:
            pi = pi[0:int(args.limit_pi)]

    method2(pi) 
    
