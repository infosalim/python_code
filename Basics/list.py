string = 'helllooo'

amazon_cart = [
    'notebook',
    'sunglasses',
    'toys',
    'grapes'
]

# strings ar immutable
# greet = 'hello'
# that's why we'll get error
# greet[0] = 'z'
# string slicing
# list_name[start:stop:step]
# print(string[0:2:1])

# lists are mutable, we can replace list's item
amazon_cart[0] = 'laptop'

new_cart = amazon_cart # creating new cart based on amazon cart, it won't take any memory,just a ref
new_cart_copy = amazon_cart[:] # creating a new cart by copying the amazon cart ant take it's own memory

# print(amazon_cart)

# Some list methods 
basket = [1,2,3,4,5,6,7,8,9]

# adding in end of the list
basket.append(100)
basket.append(100)

# insert an item of any index
# list_name.insert(index_where_to_insert, item)

basket.insert(3, 200)
# list extend
basket.extend([6, 60])
# print(basket)

# removing from list

# remove one item from end of the list 
basket.pop()
# remove one item by index
basket.pop(0)

# remove one by value
basket.remove(100)
# print(basket)
# removing all items in list
# basket.clear()

# print(basket)
# list index
# list_name(index, start looking, end looking)

# print(basket.index(100))
# print(basket.index(4, 2, 5))

# checking item exists or not with in

# print(9 in basket)

# same items count
# print(basket.count(6))

abcd = ['a', 'b', 'e', 's']

# sort() - sort the list 
# basket.sort()

# sorted() take the list and make a copy of sorted list 

# reverse() - sort the list 
# basket.reverse()
# basket.reverse()


basket.sort()
# print(basket)
basket.reverse()
# print(basket)

# range() create a list range(star, end)
# print(list(range(1,100)))

name = ''
joined = name.join(['h','o','s','s','a','i','n'])

# print(joined)


# LIST UNPACKING
a,b,c, *other, d = [1,2,3,4,5,6,7]

# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# print(type(None))