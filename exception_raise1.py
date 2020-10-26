a = input("Enter your name: ")
b = int(input("Enter your salary: "))
if b == 0:
    raise Exception("Stopping execution as salary is zero.")
if a.isnumeric():
    raise Exception("Numbers are not allowed.")

print(f"Hello {a}")