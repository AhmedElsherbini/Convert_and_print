#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:47:19 2021

@author: ahmed_elsherbini
mail: drahmedsherbini@yahoo.com

"""

###########################################
import os as os
import sys
from io import StringIO
from Bio import SeqIO
from os import listdir
import fnmatch

#########################################3
#convert multi-fasta to fasta then print all names in a list
#for batch mode press b where this cript is going to loop on every file you have in your dir.
gg = input("do you want to convert a multi-fasta to numerous fasta files? y/b/n:")
if gg == "y":

	f = input("what is the name of your multi-fasta file?")

	count = 0 
	for seq_record in SeqIO.parse(f,"fasta"):
	     count +=1 #so we can give every seq a number
	     file = open("%s_seq_%d.fna"%(str(f),int(count)),"w") 
	     file.write(">"+str(seq_record.id)+"\n")
	     file.write(str(seq_record.seq)+ "\n")
	     file.close()

if gg == "b":
    type_exten = input("What is the (*.extension) of your files (Example of the answer:*.fasta,*.faa)?:")
    for f in os.listdir():
    		if fnmatch.fnmatch(f,type_exten):
                   	count = 0 
                   	for seq_record in SeqIO.parse(f,"fasta"):
                   	     count +=1 #so we can give every seq a number
                   	     file = open("%s_seq_%d.fna"%(str(f),int(count)),"w") 
                   	     file.write(">"+str(seq_record.id)+"\n")
                   	     file.write(str(seq_record.seq)+ "\n")
                   	     file.close()
      

###################################################################
#print all files names in a list
gg = input("do you want to print your files names in a list? y/n:")

if gg == "y":
	print("make sure that the files you want to print has a distinguished extension")
	type_exten = input("What is the (*.extension) of your files (Example of the answer:*.fna)?:")

	with open("manyfiles.list", "w") as file:
	    for f in os.listdir():
    		if fnmatch.fnmatch(f,type_exten):
    		        file.write(str(f+"\n"))

