amazon_cart = [
    'notebooks', 
    'sunglasses',
    'toys',
    'grapes'
]

# print(amazon_cart)

 # List slicing
# print(amazon_cart[0:2])
# print(amazon_cart[0::2])

amazon_cart[0] = 'laptop'

new_cart = amazon_cart
new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

#Matrix

matrix = [ 
          [1,2,3], 
          [2,4,6], 
          [7,8,9] 
]

# print("Sub Array: ", matrix[0])
# print("Sub Array: ", matrix[1])
# print("Sub Array: ", matrix[2])

# print(matrix[0][1])

# list methods
basket = [1,2,3,4,5]
# print(len(basket))

 # add to list

new_list = basket.extend([100,101])
# print(basket)
# print(new_list) #does not produce a value, so if you want one, assign basket to a new_list variable

# remove
new_list = basket.clear()
print(basket)
 