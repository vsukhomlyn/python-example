def max2numb():
    try:
        a = int(input("Enter number a: "))
        b = int(input("Enter number b: "))

        if a > b:
            print("Max is a: " + str(a))
        elif a == b:
            print("a equals b: " + str(a))
        else:
            print("Max is b: " + str(b))
    except Exception as err:
        print(f"Unexpected error : {err}", err)


if __name__ == "__main__":
    max2numb()
