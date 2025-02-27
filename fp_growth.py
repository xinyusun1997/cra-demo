# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:41:47 2018

@author: Xinyu Sun
"""
# Python 3.6
# This one is based on the FP-growth algorithm.
# Get the frequent items by using FP-growth algorithm.
# Package: Pymining.
# Package Website: https://github.com/bartdag/pymining
# Have attahced the package sourse code in the .zip file.
# Running Time: About one minute. (Based On My Comupter)
# The result will be sorted and then print out. 

from pymining import itemmining

# Function from the package.
class freq_mining(object):
	def __init__(self, transactions, min_sup):		
		self.transactions = transactions  
		self.min_sup = min_sup  

	def fp_growth(self):
		fpgrowth_input = itemmining.get_fptree(self.transactions, None, 100)
		item_sets = itemmining.fpgrowth(fpgrowth_input, self.min_sup)
		return item_sets


def main(transactions, min_sup):
	item_mining = freq_mining(transactions, min_sup)
	freq_items = item_mining.fp_growth()    
	return freq_items

if __name__ == "__main__":
    # Reading from the input_file.
    # Get the transactions.
    input_file=open('freq_items_dataset.txt')
    transactions=[]
    for line in input_file:
        each_line=[]
        for item in line.split():
            each_line.append(int(item))
        transactions.append(each_line)
    input_file.close()
    # Reading Over.
    
    # Minimum support=100
    min_sup=100
    result=main(transactions,min_sup)
    result_fpgrowth=[list(x) for x in result]
    
    # Sort the result and print it out.
    result_fpgrowth.sort()
    print(result_fpgrowth)
