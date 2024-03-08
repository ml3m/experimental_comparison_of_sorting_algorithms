##############################################
#				                    	     #
#    Experimental Comparison                 # 
#               of Sorting Algorithms        # 
#              				                 # 
#		        github.com/ml3m		         #
#					                         #
##############################################

from PySortAlgos import (BubbleSort, 
                         SelectionSort, 
                         InsertSort, 
                         QuickSort, 
                         MergeSort, 
                         HeapSort, 
                         isSorted)

import time, random

TEST_E = 30 # ~ 1bil only for test puposes
START_E = 2 # 2^2 = 4
MAX_E = 16 # 2^22 = 4.194.304
TRIES = 1  # default will be 1, maybe a better implementation for final paper

TOTEST = (
    
   #(Class,         Name,            Max)
   # (BubbleSort,    "BubbleSort",    17),
   # (SelectionSort, "SelectionSort", 17),
   # (InsertSort,    "InsertSort",    18),
    (HeapSort,      "HeapSort",      16),
    (MergeSort,     "MergeSort",     16),
    (QuickSort,     "QuickSort",     16),
    )

# printing of the top categories
#nameList = ""
#for r in TOTEST:
#    nameList += ("\t\t" if len(nameList) > 0 else "") + r[1]
nameList = "\t\t".join(r[1] for r in TOTEST)

print("Elements\t\t" + nameList)
# main 

# l  ~   list_to_sort


e = START_E
# process until limit MAX_E is reached.
while e <= MAX_E:
    res = []
    max = -1
    # for each sorting algorithm we take 
    for algorithm, name, limit in TOTEST:
        if e > limit:
            res.append(None)
        else:
            sum = 0
            for _ in range(TRIES):
                # create a list with 2^e Elements
                list_to_sort = list(range(0, 2**e))
                # shuffle that one list
                random.shuffle(list_to_sort)

                # time started
                t1 = time.time()
                sortedlist = algorithm().sort(list_to_sort) #sort by r[0] which is the class algorithm
                                            #apply method .sort from that class to list_to_sort - list of values

                sum += time.time() - t1     # sum = the times used for sum/ TRIES
                # just to make sure 
                if not isSorted(sortedlist):
                    print("Error in " + name)


# what does it do?
            res.append(sum / TRIES)
            if res[-1] > max:
                max = res[-1]

# printing this happens after each 2^e and e+=1 
    tp = "2^" + str(e) + " = " + str(2**e) + " \t\t"
    for v in res:
        if v == None:
            tp += " \t\t"
        else:
            p = "0"
            if max > 0:
                p = str(round(100*v/max, 2))
            tp += str(round(v, 5)) + "s (" + p + "%)"
            if v == 0: tp += "   "
        tp += "    \t"
    print(tp)

# 2^e++ basicaly
    e += 1
       

# end
print("\nFinish :)")
