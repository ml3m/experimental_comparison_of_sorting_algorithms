# > [!IMPORTANT]
>
Certainly! Let's walk through a simple hypothetical example to illustrate how the percentage calculation works in the context of sorting algorithms and the provided code.

Assume you have three sorting algorithms: Algorithm A, Algorithm B, and Algorithm C. For a specific list size, the measured times (in seconds) for these algorithms are as follows:

Algorithm A: 2.5 seconds
Algorithm B: 4.0 seconds
Algorithm C: 3.0 seconds
In this case, Algorithm B took the longest time (4.0 seconds), so it becomes the reference for calculating percentages. The percentages for Algorithms A and C are calculated relative to the time taken by Algorithm B.

Calculate Percentages:

For Algorithm A: 
2.5
4.0
×
100
≈
62.5
%
4.0
2.5
​
 ×100≈62.5%
For Algorithm B: 
4.0
4.0
×
100
=
100
%
4.0
4.0
​
 ×100=100% (since it's the reference)
For Algorithm C: 
3.0
4.0
×
100
≈
75
%
4.0
3.0
​
 ×100≈75%
Display Results:

The percentages are then included in the output, showing how much each algorithm's time contributes to the maximum time observed.
In Python code, this might look like:

python
Copy code
# Assuming the times for the algorithms
time_A = 2.5
time_B = 4.0
time_C = 3.0

# Calculate percentages relative to the maximum time (Algorithm B)
percentage_A = (time_A / time_B) * 100
percentage_B = 100  # Reference algorithm
percentage_C = (time_C / time_B) * 100

# Display Results
print("Algorithm A: {:.2f}%".format(percentage_A))
print("Algorithm B: {:.2f}%".format(percentage_B))
print("Algorithm C: {:.2f}%".format(percentage_C))
Output:

yaml
Copy code
Algorithm A: 62.50%
Algorithm B: 100.00%
Algorithm C: 75.00%
These percentages indicate how much slower (or 





