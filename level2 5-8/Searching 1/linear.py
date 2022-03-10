print("This is Linear Search")


def linearsearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


while(True):
    arr = ['i', 'a', 'm', 'a', 't', 'r', 'e', 'e']
    x = input("Enter the element to search: ")

    result = linearsearch(arr, x)
    if(result != -1):
        print("element found at index "+str(result))
    else:
        print("element not found")

# --------------------------------------------without range---------------------------
# def linearSearch(arr,num):
#     a=0
#     for i in arr:
#         print(i)

#         print(arr[a], type(arr[a]))
#         print(num,type(num))
#         if num==arr[a]:
#              return a
#         a+=1


#     return -1

# arr=[12,2,33,45]
# num=int(input("enter the number which you want to find"))
# result=linearSearch(arr,num)

# if(result!= -1):
#     print("word found",result)
# else:
#     print("not found",result)
