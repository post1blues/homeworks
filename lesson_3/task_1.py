
sample_string = input("Enter please your string: ")
if len(sample_string) < 2:
    print("")
else:
    print(f"{sample_string[:2]}{sample_string[-2:]}")
