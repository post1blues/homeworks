
expressions = [
    ('2 + 2', '4'),
    ('100 / 1', '100'),
    ('15 * 3', '45'),
    ('2 + 2 * 2', '6'),
    ('2 ** 2 + 2 ** 2 + 100', '108')
]

user_score = 0

print("Hello! Let's check your math knowledge! Answer on this simple mathematical expressions")

for expression in expressions:
    print(f"Read the expression and answer:\n\t{expression[0]}")
    answer = input("Your answer (only numerical): ").strip()

    if answer == expression[1]:
        user_score += 1
        print(f"That's right answer. Your score: {user_score}")
    else:
        print("Wrong answer =(\n")

print(f"That's all. Your score: {user_score}/{len(expressions)}")


