import sys

squares_list = [x*x for x in range(1_000_000)]
squares_gen = (x*x for x in range(1_000_000))
 
print("List size:", sys.getsizeof(squares_list))     
print("Generator size:", sys.getsizeof(squares_gen))
 
 