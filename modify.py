def modify_list(mylist):
    mylist.append(99)
    print("Inside:", mylist)


nums = [1,2,3]
modify_list(nums)

print("Outside: ", nums)



def modify_number(n):
    n = n + 10
    print("Inside: ", n)



x = 5
modify_number(x)
print("Outside: ", x)
