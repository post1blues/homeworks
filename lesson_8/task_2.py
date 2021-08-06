def sqr_and_divide():
    try:
        a, b = input("Enter two numbers (space is separate): ").strip().split(" ")
        return (int(a)**2 / int(b))
    except ValueError:
        raise ValueError("You need to enter two numbers")
    except ZeroDivisionError:
        raise ZeroDivisionError("Second argument shouldn't be a zero")


print(sqr_and_divide())