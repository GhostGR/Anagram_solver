# Anagram solver
# Copyright (c) 2016 Lykourgos Tanious
# Read LICENCE.txt
# Description :      A script made to solve anagrams by rearranging
#               the letters in a word and comparing them to words in
#               a wordlist text file.
# Author      : Lykourgos Tanious
# date        : 01/03/2016
# Version     : V1.0


while True:
    print("################################################\n"
          "#                Anagram solver                #\n"
          "#==============================================#\n"
          "#     Copyright (c) 2015 Lykourgos Tanious     #\n"
          "#----------------------------------------------#\n"
          "#     Version : V1.0                           #\n"
          "#     Author  : Lykourgos Tanious              #\n"
          "################################################\n")
    word = input("Input the words separated with space :  ")
    wrdlst = input("Input the path to the wordlist :  ")
    wordl = word.split("")
    wordlist = open(wrdlst, 'r')
    words = wordlist.readlines()
    c = int(0)
    c0 = int(0)
    res = []
    while c0 < len(wordl):
        c = int(0)
        while True:
            cword = words[c]
            cword = cword.strip("\n")
            c2word = wordl[c0]
            lword = list(c2word)
            lwords = list(cword)
            lword.sort()
            lwords.sort()
            if lword == lwords:
                res.append(cword)
                break
            c += 1
        c0 += 1
    print(",".join(res))
