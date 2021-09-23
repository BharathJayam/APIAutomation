print("Hello")

# List is a data type that can add multiple datatypes

Values = [1, 2, "Bharath", 4, 5, 6]

print(Values[1])
print(Values[1:3])
Values.insert(4 , "Jayam")
Values.append("Balue")
Values[1] = "19"
print(Values)

# Tuple is same as List but it is immutable so we can not modify the Tuple
# One more difference we have is Tuple is declared as () and List is declared as []
Value1 = (1, 2, 2, 2)
print(Value1)

# Dictionaries are with key value pair
# We declare them using flower bracket

dValue = {1: "Bharath", 2: "Jayam", 3: "Balu"}

print(dValue[1])
print(dValue[2])
print(dValue[3])
#Bharath
#Jayam
#Balu

dValue[4] = "Maanya"

print(dValue)
#{1: 'Bharath', 2: 'Jayam', 3: 'Balu', 4: 'Maanya'}
print(dValue[1])
#Bharath






