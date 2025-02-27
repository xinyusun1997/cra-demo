# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 16:43:19 2018

@author: Xinyu Sun
"""
# Python 3.6
# This one is based on the relim algorithm.
# First get the frequent items by using relim algorithm.
# Then from these items to construct the closed frequent itemsets and maximal frequent items.
# Package: Pymining.
# Package Website: https://github.com/bartdag/pymining
# Have attahced the package sourse code in the .zip file.
# Running Time: About 10 minutes. (Based On My Comupter)

from pymining import itemmining

# From package.
class freq_mining(object):
	def __init__(self, transactions, min_sup):		
		self.transactions = transactions  
		self.min_sup = min_sup  
	def freq_items(self):
		relim_input = itemmining.get_relim_input(self.transactions)
		item_sets = itemmining.relim(relim_input, self.min_sup)
		return item_sets

def main(transactions, min_sup):
	item_mining = freq_mining(transactions, min_sup)
	freq_items = item_mining.freq_items()    
	return freq_items

if __name__ == "__main__":
    # This part is from relim.
    input_file=open('freq_items_dataset.txt')
    transactions=[]
    for line in input_file:
        each_line=[]
        for item in line.split():
            each_line.append(int(item))
        transactions.append(each_line)
    input_file.close()
    min_sup=100
    result=main(transactions,min_sup)
    result_list=[list(x) for x in result]
    
    # Relim part end.
    
    # Here get the closed and maximal frequent itemsets.
    closed_freq_item={}
    max_freq_item={}
    count_dict={}     
    count_max={}
    for i in result:
        if i not in count_dict:
            count_dict[i]=1
            count_max[i]=1
        for j in result:
            # This is the condition for Closed:
            # 1. Immediate Supersets
            # 2. Counts are not same
            if i!=j and i.issubset(j) and result[i]==result[j] and abs(len(i)-len(j))==1:
                count_dict[i]+=1
            # 1. Immediate Supersets
            # 2. No Immediate Supersets are frequent.
            if i!=j and i.issubset(j) and abs(len(i)-len(j))==1:
                count_max[i]+=1
                
    # If the count equal to one, the it satisfied the condition.            
    for x in count_dict:
        if count_dict[x]==1:
            closed_freq_item[x]=1
    
                
    for x in count_max:
        if count_max[x]==1:
            max_freq_item[x]=1
            
    # This part is for print them out.
    result_closed=[list(x) for x in closed_freq_item]
    result_max=[list(x) for x in max_freq_item]
    print(result_closed)
    print(result_max)
