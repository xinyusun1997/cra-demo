# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 21:29:30 2018

@author: Xinyu Sun
"""

# Python 3.6
# This one is based on the Apriori algorithm.
# Get the frequent items by using Apriori algorithm.
# Running Time: About 2 hours. (Based On My Comupter)
# The result will be sorted and then print out.

def prune(transactions, generationX, minimum_support):
    # This is the result set.
    itemset_after=[]
    # This is for count the numbers.
    itemset_count={}
    for i in transactions:
        for j in generationX:
            if j.issubset(i):
                if j in itemset_count:
                    itemset_count[j]+=1
                else:
                    itemset_count[j]=1
    # Look into the count.
    for m in itemset_count:
        # If the count larger than min_sup, then add it to the result.
        if itemset_count[m]>=minimum_support:
            itemset_after.append(m)
    return itemset_after
                

def generate(itemset_after,generation_num):
    # New candidate sets.
    new_itemset=[]
    size=len(itemset_after)
    for i in range(size):
        for j in range(i+1, size):
            # As the itemset has been sorted, so here is correct.
            # This is for comparing that n-1 items for two sets are same, then combine them.
            item1=list(itemset_after[i])[0:generation_num-2]
            item2=list(itemset_after[j])[0:generation_num-2]
            # Without sort(), it will have problem.
            # It may not equal.
            item1.sort()
            item2.sort()
            # Combine these two elements.
            if item1==item2:
                # Combine.
                new_itemset.append(itemset_after[i] | itemset_after[j])
    return new_itemset    


"""
MAIN
"""
# Reading from the input_file.
# Get the transactions.
input_file=open('freq_items_dataset.txt')
transactions=[]
for line in input_file:
    each_line=[]
    for item in line.split():
        each_line.append(int(item))
    transactions.append(each_line)
min_sup=100
input_file.close()
# Reading Over.
    
# Start Generation.
generation1 = []  
for transaction in transactions:  
    for item in transaction:  
        if [item] not in generation1:  
            generation1.append([item])  
            
# To make sure that every item in generation 1 is from small to big.
generation1.sort()
# Frozenset for dict()
generation1=[frozenset(item) for item in generation1]  
# Set for using .issubset()
transactions=[set(item) for item in transactions] 
# Prune 1
result_1=prune(transactions, generation1, min_sup)
# The result is from length 1 to length K
result=[]
# Add length 1 result.
result.append(result_1)
# Generaton num. Start from 2 cause have finish generation 1.
generation_num=2

while len(result[generation_num-2])>0:
    # Generate X
    generationX=generate(result[generation_num-2], generation_num)
    # Prune X
    result_X=prune(transactions, generationX, min_sup)
    
    generation_num+=1
    # Add length X result.
    result.append(result_X)

# This part is for print.  
result_temp={}
for i in result:
    # The last one can be none.
    if i!=[]:
        for j in i:
            result_temp[j]=1 
# Print out the sorted result.
result_apriori=[list(x) for x in result_temp]
result_apriori.sort()
print(result_apriori)
