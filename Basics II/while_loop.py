# i = 0

# while i < 10:
#     print(i)
#     if i == 7:
#         print('got 7')
#         break
#     i+=1
# else:
#     print('didn\'t get 7')

# while True:
#     response = input('Say something: ')
#     if(response == 'bye'):
#         break

numbers = range(1,30)

for i in numbers:
    if '3' in str(i):
        print('This is skipped')
        continue
    print(i)
    
