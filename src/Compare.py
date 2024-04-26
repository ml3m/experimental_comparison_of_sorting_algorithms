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
                         MergeSort,
                         HeapSort,
                         RadixSort,
                         SmoothSort,
                         Timsort,
                         CombSort,
                         isSorted)

import time
import random

TEST_E = 30  # ~ 1bil only for test puposes
START_E = 9  # 2^2 = 4
MAX_E = 14  # 2^22 = 4.194.304
TRIES = 10  # default will be 1, maybe a better implementation for final paper
TOTEST = (
     #(algorithm(class),  Name,       Limit)
    (BubbleSort,    "BubbleSort",    14),
    (SelectionSort, "SelectionSort", 14),
    (InsertSort,    "InsertSort",    14),
    (HeapSort,      "HeapSort",      14),
    (MergeSort,     "MergeSort",     14),
    (QuickSort,     "QuickSort",     14),
    (RadixSort,     "RadixSort",     14),
    (SmoothSort,    "SmoothSort",    14),
    (Timsort,       "Timsort",       14),
    (CombSort,      "CombSort",      14)
)

# printing of the top categories
# nameList = ""
# for r in TOTEST:
#    nameList += ("\t\t" if len(nameList) > 0 else "") + r[1]
nameList = "\t\t".join(r[1] for r in TOTEST)

print("Elements\t\t" + nameList)
# main

list_kind = 1
print_ok1 = False
print_ok2 = False
print_ok3 = False
print_ok4 = False
print_ok5 = False

def generate_random_list(length):
    return [random.randint(0, 999999) for _ in range(length)]


# process until limit MAX_E is reached.
while list_kind <= 5:
    e = START_E
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
                    
                    if list_kind == 1:
                        # Shuffled
                        
                        if print_ok1 is False:
                            print("\n\n\tShuffled\n\n")
                            print_ok1 = True

                        list_to_sort = generate_random_list(2**e)
                        random.shuffle(list_to_sort)
                    elif list_kind == 2:
                        # Almost Sorted

                        if print_ok2 is False:
                            print("\n\n\tAlmost Sorted\n\n")
                            print_ok2 = True

                        list_to_sort = generate_random_list(2**e)
                        random.shuffle(list_to_sort)
                        # need to get a better way here
                        while True:
                            list_length = len(list_to_sort)
                            choice1 = random.choice(list(range(0, list_length - 1)))
                            choice2 = random.choice(list(range(0, list_length - 1)))
                            if choice1 != choice2:
                                break

                        aux = list_to_sort[choice1]
                        list_to_sort[choice1] = list_to_sort[choice2]
                        list_to_sort[choice1] = aux

                    elif list_kind == 3:
                        # reversed Sorted
                        if print_ok3 is False:
                            print("\n\n\tReversed Sorted\n\n")
                            print_ok3 = True


                        list_to_sort = generate_random_list(2**e)
                        list_to_sort = list_to_sort[::-1]
                    elif list_kind == 4:
                        if print_ok4 is False:
                            # Already sorted
                            print("\n\n\tSorted\n\n")
                            print_ok4 = True
                        list_to_sort = generate_random_list(2**e)
                    else:
                        if print_ok5 is False:
                            print("\n\n\t0 and 1 shuffled Array\n\n")
                            print_ok5 = True
                        list_to_sort = [random.randint(0, 1) for _ in range(2**e)]

                    
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
        tp = "2^" + str(e) + " = " + str(2**e) + " \t\t"
        for v in res:
            if v is None:
                tp += " \t\t"
            else:
                p = "0"
                if max > 0:
                    p = str(round(100*v/max, 2))
                tp += "{:.8f}s ({:.2f}%)".format(v, float(p))
                if v == 0: tp += "   "
            tp += "    \t"
        print(tp)
        e += 1
    list_kind += 1



print("\nFinish :)")
