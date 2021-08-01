
input_string = input("Enter please your text:\n").strip().lower()

result = dict()
if not input_string:
    print("Your text is empty!")
else:
    input_words = input_string.split(' ')
    for word in input_words:
        if word in result.keys():
            result[word] += 1
        else:
            result[word] = 1

for k, v in result.items():
    print(f"{k} - {v}")