fruits=["strawwbery","kiwi","banana","lemon","watermelon","tomato","orange","berrier","plum","blueberry"]
fruits_tuples=("strawwberry","kiwi","banana","lemon","watermelon","tomato","orange","barrier","plum","blueberry")

print(fruits[1])
fruits[1]="rasberies"
print(fruits[1])
#cannot change item in a tuple
#fruits_tuples[1]="rasberies"
#print(fruits_tuples[1])
"""
items in a tuple cannot change where as in a normal list they are able to change 
"""
#print the last item of the list 
print(fruits[9])
print(fruits[-1])
print(fruits[len(fruits)-1])

#print first three items
print(fruits [0:3])


#print the number of items inside the fruits 
print(len(fruits))
#print the type of fruits
print(type(fruits))
#print the type of fruits tuples
print(type(fruits_tuples))
#print the last item of your list
print(fruits[9])


#pupils using different data types
tupleExInt =(70,80,90,100)
tupleExFlo =(70.7,80.8,90.99,100,10)
tupleExStri=("hello","how","are","you")
tupleExbool=(True,False)
tupleMixedDataTypes=(70,70.7,"how",False)

friends=("raja","umar","engjul","asad","ali","umar","ali","ali")
print(friends[0:5])
for friend in friends:
    print(friend)
for i in range(len(friends)):
    print(friends[i])


print(friends.count("umar"))
print(friends.count("asad"))
print(friends.count("ali"))


fruits = ["strawberry", "kiwi", "banana", "lemon", "watermelon", "tomato", "orange", "berrier", "plum", "blueberry"]


for fruit in fruits:
    print(f"Fruit: {fruit}")
    for letter in fruit:
        print(letter)

print(fruits.count(fruit))
print(len(fruits))






    
    
    




