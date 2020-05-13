#coding:utf-8

import argparse

 

parser = argparse.ArgumentParser(description='some integers')

 

parser.add_argument('inte', metavar='N', type=int, nargs='+',help='an integer for accumulator')

parser.add_argument('--sum', dest='accumulate', action= 'store_const', const=sum, default=max,help='sum the integers (default: find the max)')

 

args = parser.parse_args()
print(args)

print(args.accumulate(args.inte))