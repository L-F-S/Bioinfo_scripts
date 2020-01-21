#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:08:08 2020

@author: L-F-S
@ University of Trento, Italy
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datadir="/home/lorenzo/tesitriennale/resuperurgentparazoanthusrevision"
os.chdir(datadir)
seq_of_hap={}
dataname="ITSallspeciesgapincluded"
f=open(dataname+".temp")
for line in f.readlines():
    if line.startswith("FORMAT"):
        lines=line.strip().split()
        missing=lines[2].split("=")[1]
        gap=lines[3].split("=")[1]
        match=lines[4].split("=")[1][0]
        print(missing, gap, match)
    if line.startswith("Hap"):
        seq_of_hap[line.strip().split()[0]]=line.strip().split()[1]
f.close()

ref=seq_of_hap["Hap_1"]
print(ref)
refgap=ref
def find_gap(i):
    for hap, seq in seq_of_hap.items():
        seq=list(seq)
        print(seq[i])
        if seq[i]  != gap:
            return seq[i]
    print("tutti gap qlcs nn va")
    return("-")
            
        
refgaplist=list(refgap)
for i in range(len(refgap)):

    if refgap[i]==gap:
        print("###########",i)        
        refgaplist[i]=find_gap(i)
print(refgaplist)
for hap, seq in seq_of_hap.items():
    seq=list(seq)
    for i in range(len(seq)):
        if seq[i] == match:
            seq[i] = ref[i]
        if seq[i]  == missing:
            print("BOOO")
    seq="".join(seq)
    seq_of_hap[hap]=seq

# print fasta
f=open(dataname+"newfasta.fas", "w")
fastaline=""
for hap, seq in seq_of_hap.items():
    fastaline+=">"+hap+"\n"+seq+"\n"
f.write(fastaline)
f.close
    