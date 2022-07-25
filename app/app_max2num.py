from app.max2num.max2num import max2num


def main():
    try:
        a = int(input("Enter number a: "))
        b = int(input("Enter number b: "))

        print("Max of a and b is " + str(max2num(a, b)))
    except Exception as err:
        print(f"Unexpected error : {err}")
