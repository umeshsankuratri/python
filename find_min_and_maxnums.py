'''Question:
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.'''

smallest = None
largest = None
while True:
    number = raw_input("Enter a number: ")
    if number == 'done':break
    try:
        num = int(number)
    except:
        print "Invalid input"
        continue
    if smallest is None:
        smallest=num
    elif num<smallest:
        smallest=num
    elif num>smallest:
        largest=num
print "Maximum is", largest
print "Minimum is", smallest
