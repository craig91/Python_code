 #--> Takes a sequence (string, list, tuple) returns first/last element of that sequence
def firstLast(sequence):
     return sequence[:1] + sequence[-1:]
        

#print(firstLast([1,2,3,4,5,6,7]))
#print(firstLast('hello'))
#food = tuple(("broccoli", "cheese", "Apple", "Basil"))
#print(firstLast(food))




# Write a function that takes a list or a tuple of numbers. Return a two-element list, containing the sum of the even indexed numbers and the sum of the odd-indexed numbers. 
# even_odd_sums([10,20,30,40,50,60]) --> [90, 120]

def even_odd_sums(sequence):
     for val in sequence:
         sum = val += val
     return sequence


print(even_odd_sums([1,2,3,34,45,6,7,6]))
