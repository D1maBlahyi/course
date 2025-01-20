#1 #2 #3
enter = input("Enter your text: ")
if enter.isalpha():
    print(f'Your text "{enter}" consist only of letters. Their length is {len(enter)}')
elif enter.isdigit():
    print(f'Your text "{enter}" consist only of numbers')
    if int(enter) % 2 == 0:
        print(f"Your number '{enter}' is paired")
    else:
        print(f"Your number '{enter}' is non-paired")
else:
    print(f'Your text "{enter}" has non-alphabetic and non-numeric meanings')

