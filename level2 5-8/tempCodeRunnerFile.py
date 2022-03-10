d2={"a":"burger","b":"pizza","c":"indian"}
print(d2.keys())
print(d2.values())
print(d2.items())

list1=[["a",1],["b",3],["c",4]]
for i in list1:
    print(i)

for name,book in list1:
    print(name," reads ",book)


dict1=dict(list1)
print(dict1)
print(dict1.items())
for name,book in dict1.items():
    print(name,"reads",book,"book in a day")
