# assigns the number of people to the variable
types_of_people = 10

# creates a new vairable that is a string formated to hold a vairable 
x = f"There are {types_of_people} types of people."

# creates the binary variable
binary = "binary"

#creates the do_not variable
do_not = "don't"

# creates a new vairable that is a string too and is formated to hold 2 variables
y = f"Those who know {binary} and those who {do_not}."

# prints vairable x
print(x)

# prints vairable y
print(y)

# prints the formatted string containing vairable x
print(f"I said: {x}")

#prints the formated string containing vairable y
print(f"I also said: '{y}'")

# creates a new variable holding the boolean value False
hilarious = False

# creates a new variable that is a string formated with a placeholder {}
joke_evaluation = "Isn't that joke so funny?! {}"

# prints the variable joke_evaluation and formats to show the vairable hilarious
print(joke_evaluation.format(hilarious))

# creates a new string vairable w
w = "This is the left side of... "

# creates a new string vairable e
e = "a string with a right side."

# concatenantes the variables w and e
print(w + e)