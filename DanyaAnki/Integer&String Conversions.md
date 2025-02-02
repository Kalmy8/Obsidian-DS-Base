#🃏
1. Convert the integer `123` to a string.
2. Convert the string `"456"` to an integer.
3. You have the string `"The price is: 10.99"`. Extract the price as a float.
4. Get a number from the user using `input()`. Convert it to a float and print its square.
5. What happens if you try to convert the string `"hello"` to an integer using `int("hello")`?
?
1. `num = 123 str_num = str(num)`
2.  `str_num = "456" num = int(str_num)`
3. `text = "The price is: 10.99" parts = text.split(": ") price = float(parts[1])`
4. `num_str = input("Enter a number: ") num = float(num_str) print(num ** 2)`
5. A `ValueError` will occur because "hello" cannot be converted to an integer.
