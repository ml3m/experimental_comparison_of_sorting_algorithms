# Experimental Comparison

This repository contains code for conducting experimental comparisons of various sorting algorithms. The primary purpose is to analyze the performance of these algorithms under different conditions.

## Introduction

Sorting algorithms are fundamental to computer science and are used extensively in various applications. This project provides a Benchmark to evaluate the efficiency of sorting algorithms by measuring their execution time under different scenarios.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Results](#results)

## Overview

The main code in this repository executes sorting algorithms on different types of input lists and measures their performance. The sorting algorithms included in this project are:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Heap Sort
- Merge Sort
- Quick Sort
- Radix Sort
- Smooth Sort
- Tim Sort
- Comb Sort

The project allows for testing these algorithms on various types of input lists, such as shuffled lists, almost sorted lists, reversed sorted lists, already sorted lists, small range arrays, and arrays of 0s and 1s.

## Files
Implementation of above sorting Algorithms:
[find in this file] (src/PySortAlgos.py)
Implementation of benchmark:
[find in this file] (src/Compare.py)
## Setup

To run the code, you need Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

## Usage
After setting up Python you can run the main code to conduct experimental comparisons. Here's how to do it:

Clone or download this repository to your local machine.
```
git clone https://github.com/ml3m/experimental_comparison_of_sorting_algorithms
```
Navigate to the source directory using the command line.
```
cd src
```
Run the main code using Python (terminal output):
```
python Compare.py
```
or pipe
```
python Compare.py >> results/my_test_results.txt
```

The code will execute the sorting algorithms on different types of input lists and display the results.

## Results
The results obtained from running this experiment can be used for analysis purposes. The output includes the execution time of each sorting algorithm under different scenarios, allowing for comparisons and insights into their performance characteristics.
