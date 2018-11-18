print("What is your first number?")
input1 = input()
x = int(input1)
# May fail!

print("What is your second number?")
input2 = input()
y = int(input2)
# May fail!

total = x + y
finalSentence = f"The sum of the two numbers is {total}"
print(finalSentence)

input("Press Enter to continue.")
