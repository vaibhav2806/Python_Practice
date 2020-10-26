c = input ("Enter you name: ")
try:
    print(a)
except Exception as e:
    if c == "himanshu":
        raise ValueError("himanshu is blocked he is not allowed")

    print("Exception handled")

