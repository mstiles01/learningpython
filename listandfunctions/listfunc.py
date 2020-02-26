lucky_numbers = [4, 8, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

#.extend adds "luck_numbers to the end of friends"
friends.extend(lucky_numbers)
print(friends)

#adds "creed" to the end of friends list
friends.append("Creed")
print(friends)

#inserts element into the postion of index one
friends.insert(1, "Pam")
print(friends)

#removes element
friends.remove("Karen")
print(friends)

#.clear removes all items from list
#.pop removes last element inside the list

#finds value given
friends.index(("Kevin"))

#.count counts the value and print how many times it appears

#sorts in alphebetical order, with nums puts it in ascending order
friends.sort()
print(friends)

#.reverse reverses the order of the list

#copys the values of selected list
friends2 = friends.copy