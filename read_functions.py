# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:32:41 2017

@author: taichi
"""
def read_whole():
    file = open("sample_data\poem.txt", "r" )

    for word in file.read().split() :
        print(word, end=" ")
    
    file.close()
    print("\n")

def read_whole2():
   file = open("sample_data\poem.txt","r")
   for line in file :
       print(line, end="\n")
   file.close()
   print("\n")
   
   
def read_whole3():
    file = open("sample_data\poem.txt","r")
    words = file.read().split()
    length = len(words);
    print(words[length-1], end="")
    print("\n")