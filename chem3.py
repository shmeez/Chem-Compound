lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
l = ""
n = ""
d = {}

a = input("Enter in a chemical compund: ")
a1 = list(a)   #turns input into list
for x in reversed(a1):    #reverses the list(it's easier to seperate the elements when reversed)
    if x in lowercase:     #checks for lowercase
        l = x      #gives variable
    elif x in numbers:    #checks for numbers
        n = x + n     #adds x to numbers variable, the previous number would get overrided if not added
    elif x in uppercase:    #checks for uppercase
        if n == "":       #checks if there's no number before a lowercase/uppercase (remember it's going backwards)
            n = '1'      #makes the element(s) equal 1
        c = x + l         #puts lowercase and uppercase together to make element
        if not c in d: d[c] = 0      #if c(element) not in d(dict), add element to d
        d[c] += int(n)       #gives c a number
        n = ""       #resets variables
        l = ""

print(d)
