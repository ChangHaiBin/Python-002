
print("How much does a cup of Milo cost?")
input1 = input()
costPerCup = float(input1)
# May fail!

print("How many cups do you want?")
input2 = input()
numCup = float(input2)
# May fail!
# Here we did not prevent decimal numbers of cup. We will temporary ignore this issue.


totalPrice = costPerCup * numCup 




print(f"The total is {totalPrice}")



input("Press Enter to continue")










