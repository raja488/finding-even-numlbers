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


