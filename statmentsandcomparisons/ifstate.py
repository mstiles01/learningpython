is_male = True
is_tall = False

#or is triggered if one or more value is true
#and is triggered when both/all requirments are true
if is_male and is_tall:
    print("You are a tall male")

#Elif = Else if statment
elif is_male and not(is_tall):
    print("You are a short male")

elif not(is_male) and is_tall:
    print("You are not a male, but you are tall.")

else:
    print("You are not a male and not tall. ")
