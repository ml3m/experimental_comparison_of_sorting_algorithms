##############################################
# 				                    	     #
#    Experimental Comparison                 #
#               of Sorting Algorithms        #
#              				                 #
# 		        github.com/ml3m		         #
# 					                         #
##############################################

from PySortAlgos import (BubbleSort,
                         SelectionSort,
                         InsertSort,
                         QuickSort,
                         HeapSort,
                         RadixSort,
                         SmoothSort,
                         Timsort,
                         CombSort,
                         isSorted)

import time
import random

TEST_E = 30  # ~ 1bil only for test puposes
START_E = 1  # 2^2 = 4
MAX_E = 5  # 2^22 = 4.194.304
TRIES = 1  # default will be 1, maybe a better implementation for final paper
TOTEST = (
    # (algorithm(class),  Name,       Limit)
    (BubbleSort,    "BubbleSort",    5),
    (SelectionSort, "SelectionSort", 5),
    (InsertSort,    "InsertSort",    5),
    (HeapSort,      "HeapSort",      5),
    (QuickSort,     "QuickSort",     5),
    (RadixSort,     "RadixSort",     5),
    (SmoothSort,    "SmoothSort",    5),
    (Timsort,       "Timsort",       5),
    (CombSort,      "CombSort",      5)
)

# printing of the top categories
# nameList = ""
# for r in TOTEST:
#    nameList += ("\t\t" if len(nameList) > 0 else "") + r[1]
nameList = "\t\t".join(r[1] for r in TOTEST)

print("Elements\t\t" + nameList)
# main


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
                list_to_sort = list(range(0, 10**e))
                # shuffle that one list
                random.shuffle(list_to_sort)

                # time started
                t1 = time.time()
                sortedlist = algorithm().sort(list_to_sort) 
                # sort by r[0] which is the class algorithm
                # apply method .sort from that class to list_to_sort - list of values

                sum += time.time() - t1     # sum = the times used for sum/ TRIES
                # just to make sure
                if not isSorted(sortedlist):
                    print("Error in " + name)

# finds the avg of all tries and then display it bellow
# if TRIES = 1 -> useless
            res.append(sum / TRIES)
            if res[-1] > max:
                max = res[-1]

# printing this happens after each 2^e and e+=1 
# prercentage calculation
    tp = "10^" + str(e) + " = " + str(10**e) + " \t\t"
    for v in res:
        if v is None:
            tp += " \t\t"
        else:
            p = "0"
            if max > 0:
                p = str(round(100*v/max, 2))
            tp += str(round(v, 5)) + "s (" + p + "%)"
            if v == 0: 
                tp += "   "
        tp += "    \t"
    print(tp)
    e += 1



print("\nFinish :)")
