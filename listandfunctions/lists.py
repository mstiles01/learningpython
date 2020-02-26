#Value "friends" is a list. String, Number, Boolean
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)

#Indicating the Index
print(friends[0])

#Denotes grabbing element from index one and over
print(friends[1:])

#Grabs range of index, not the last index though
print(friends[1:3])

#Changing index position value
friends[1] = "Pam"

print(friends[1])
