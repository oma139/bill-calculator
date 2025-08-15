print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? $"))
tip = int(input("How much percentage tip would u like to give? 10, 12 or 15"))
y = tip / 100
z = Bill * y
x = Bill + z
Split = float(input("How many people to split the bill?"))
Pay = float(x / Split)
final = round(Pay, 2)
print(f"Each person will pay{final}")
