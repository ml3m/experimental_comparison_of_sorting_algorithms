##############################################
#    Experimental Comparison of Sorting      #
#                  Benchmark              	 #
# 		        github.com/ml3m		         #
##############################################

import time
import random
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

# !Make sure to read README.md for running guidance

# this part can be tweeked
# individual algorithms can be tested or only a range of e can be tested
# by commenting out the algorithms you don't want to test
# by changing the values of START_E and MAX_E

# !Be Careful, make sure to put manageable inputs in order to have reachable runtimes :)

# !Mention I would recommand to pipe the output of this program to a file in order to analyze it
#       cause the printing is still a bit of a mess, didn't bothered with beautify
#           cause I just edit it with vim for the paper



START_E = 3  # 2^START_E         (paper choice: 2^3 = 8)
MAX_E = 10  # 2^MAX_E             (paper choice: 2^14 = 16384)
TRIES = 1  # precision average   (paper choice: TRIES = 100 ~ !caution long waiting times)
TOTEST = (
   #(algorithm(class),  Name,       Limit)
    (BubbleSort,    "BubbleSort",    8),
    (SelectionSort, "SelectionSort", 8),
    (InsertSort,    "InsertSort",    8),
    (HeapSort,      "HeapSort",      8),
    (MergeSort,     "MergeSort",     8),
    (QuickSort,     "QuickSort",     8),
    (RadixSort,     "RadixSort",     8),
    (SmoothSort,    "SmoothSort",    8),
    (Timsort,       "Timsort",       8),
    (CombSort,      "CombSort",      8)
   #(CombSort,      "CombSort",      8)   comment unwanted algorithms like this 
)


# printing the name of participating algorithms
nameList = "\t\t".join(r[1] for r in TOTEST)
print("Elements\t\t" + nameList)

def generate_random_list(length):
    """the function that generates a list with random number from range (0, 999999), assuring a correct testing on totally random numbers"""
    return [random.randint(0, 999999) for _ in range(length)]
def generate_random_list_small_range(length):
    """used for list_kind==5"""
    return [random.randint(0, 10) for _ in range(length)]

print_ok1 = False
print_ok2 = False
print_ok3 = False
print_ok4 = False
print_ok5 = False
print_ok6 = False

list_kind = 1

# doing the process for each type of list 
while list_kind <= 6:
    e = START_E
    # process until limit MAX_E is reached by e.
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
                        list_to_sort.sort()

                        while True:
                            list_length = len(list_to_sort)
                            choice1 = random.choice(list(range(0, list_length - 1)))
                            choice2 = random.choice(list(range(0, list_length - 1)))
                            if choice1 != choice2:
                                break

                        aux = list_to_sort[choice1]
                        list_to_sort[choice1] = list_to_sort[choice2]
                        list_to_sort[choice2] = aux
                        # bug fixed

                    elif list_kind == 3:
                        # reversed Sorted

                        if print_ok3 is False:
                            print("\n\n\tReversed Sorted\n\n")
                            print_ok3 = True


                        list_to_sort = generate_random_list(2**e)
                        list_to_sort = list_to_sort[::-1]
                    elif list_kind == 4:
                        # Already sorted

                        if print_ok4 is False:
                            print("\n\n\tSorted\n\n")
                            print_ok4 = True
                        list_to_sort = generate_random_list(2**e)
                        list_to_sort.sort()
                    elif list_kind == 5:
                        # small range array 1-10
                        if print_ok5 is False:
                            print("\n\n\tsmall range array shuffled 0-10\n\n")
                            print_ok5 = True
                        list_to_sort = generate_random_list_small_range(2**e)

                    else:
                        if print_ok6 is False:
                            print("\n\n\t0 and 1 shuffled Array\n\n")
                            print_ok6 = True
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
    # for the percentage calculation I thought of a way to see the performance of the algorithms
    # by having a relatie percentage we can see which algorithm is the worst one (100%) and we can
    # easily compare thir results.

        tp = "2^" + str(e) + " = " + str(2**e) + " \t\t"
        for v in res:
            if v is None:
                tp += " \t\t"
            else:
                p = "0"
                if max > 0:
                    p = str(round(100*v/max, 2))
                tp += "{:.8f}s ({:.2f}%)".format(v, float(p))
                if v == 0: 
                    tp += "   "
            tp += "    \t"
        print(tp)
        e += 1
    list_kind += 1



print("\nFinish! from mlem :)")
