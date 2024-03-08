# https://arnehannappel.de/blog/sortieralgorithmen-vergleich

from PySortAlgos import BubbleSort, SelectionSort, InsertSort, QuickSort, MergeSort, HeapSort, isSorted

import time, random

TEST_E = 30 # ~ 1bil only for test puposes
START_E = 26 # 2^2 = 4
MAX_E = 27 # 2^22 = 4.194.304
TRIES = 1  # default will be 1, maybe a better implementation for final paper

TOTEST = (
    
   #(Class,         Name,            Max)
    #(BubbleSort,    "BubbleSort",    16),
    #(SelectionSort, "SelectionSort", 16),
    #(InsertSort,    "InsertSort",    20),
    #(HeapSort,      "HeapSort",      29),
    #(MergeSort,     "MergeSort",     29),
    (QuickSort,     "QuickSort",     27),
    )

# printing of the top categories
nameList = ""
for r in TOTEST:
    nameList += ("\t\t" if len(nameList) > 0 else "") + r[1]
print("Elements\t\t" + nameList)
# main 

# l  ~   list_to_sort


e = START_E
# process until limit MAX_E is reached.
while e <= MAX_E:
    res = []
    max = -1
    # for each sorting algorithm we take 
    for r in TOTEST:
        if e > r[2]:
            res.append(None)
        else:
            sum = 0
            for _ in range(TRIES):
                # create a list with 2^e Elements
                l = list(range(0, 2**e))
                # shuffle that one list
                random.shuffle(l)

                # time started
                t1 = time.time()
                sortedlist = r[0]().sort(l) #sort by r[0] which is the class algorithm
                                            #apply method .sort from that class to l - list of values

                sum += time.time() - t1     # sum = the times used for sum/ TRIES
                # just to make sure 
                if not isSorted(sortedlist):
                    print("Error in " + r[1])


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
