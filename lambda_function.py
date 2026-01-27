# Lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have one expression.
# They are often used for short, throwaway functions that are not reused elsewhere in the code.

l = [1,2,3,4,5,6,7,8,9,10]

#map
#It applies the function provided in lambda to all elements of the list
print(list(map(lambda x: x**2, l)))

#filter
#It filters the elements based on condition provided in lambda function
print(list(filter(lambda x: x%2==0, l)))


#reduce
#It gives aggrate value like sum, multiplication etc. of all elements in the list
from functools import reduce
print(reduce(lambda x,y: x+y, l))