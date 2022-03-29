### assumption
elements in two arrays are integers

# method 1 brute force
generate all a x b pairs

## time complexity
o(m * n)
## space complexity
o(1)

# method 2 sorting
sort array a and array b. then have one pointer in each array. 
calculate the difference between two elements
and move the pointer.  store the global smallest difference and positions.

### corner case
if a and b have common value(s), then the difference is 0
if the min in a is larger than the max in b, then difference = min[a] - max[b]

## time complexity
nlog(n) -> [sorting: mlog(m)+nlog(n) + traverse list: m+n]
## space complexity
o(1)


### Example output
------------------ Method 1 ------------------
Downloaded the tutorial in 0.1064 seconds
element_a: 295163, element_b: 295157, diff: 6
------------------ Method 2 ------------------
Downloaded the tutorial in 0.0009 seconds
element_a: 295163, element_b: 295157, diff: 6


# Q3:
If we need to compare one million lists, it's almost impossible to do it in one machine with a reasonable amont of time.
The common solution is to segment these lists to different sections and calculate local smallest value in each machine(worker),
then compare the final results. Here I listed two ways for parallel computing.
1. Spark / AWS EMR
   Spark is a large scale data processing tool. It is a practical tool that widely used in data engineering. It does the distribution internally and doesn't require 
programming on how to allocate and collect data chunks. it is easy to scale between multiple clusters. AWS EMR is one of the 
   cloud service that uses Spark and it's efficient and easy to use. 
2. MPI(Message Passing Interface) for high performance parallel computing https://mpi4py.readthedocs.io/en/stable/intro.html
   This is more of a scientific computing way. By constantly syncing between different working nodes, we can split the work between different workers and minimize duplicated work.
   This tool will require programming on splitting data to different workers and exchanging process between workers. 
   And also need to collect the results from workers and do the finally comparison. Because this method need customized according
   to the work, it is usually much more efficient. 