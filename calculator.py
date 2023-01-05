
"""
Removes White Space and Replaces Unevaluable Characters
@param string (str) : A Math Expresion
"""
def fix_up(string):

    #characters that need to be changed within the string
    symbols = {"^":"**", "x":"*"}

    string = string.lower()

    #removes whitespace
    string = string.replace(" ", "")

    #replaces unwanted character
    for char in string:
        if char in symbols:
            string = string.replace(char, symbols[char])
        
    return string

"""
Evaluates a String That Represents a Math Expression
@param string (str) : A Readable Math Expresion
"""
def calculate(expr):
    expr = fix_up(expr)

    ans = eval(expr)

    return f"{expr} is equal to {ans}"


def add(x, y):
    return x + y

def subtract(x,y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x,y):
    return x/y


"""
Manually Solves Simple Mathamatic Expressions
Doesn't Follow the Rules of BEDMAS
@param String (str): The math expression that needs to be solved
"""
def calc(string):
    symbols = ['+', '-', '/', '*']
    str_array = string.split(" ")
    num_array = []
    for num in str_array:
        if num.isnumeric():
            num_array.append(int(num))
        elif num in symbols:
            num_array.append(num)
    
    #print(num_array)
    res =0
    for i, char in enumerate(num_array):
        
        
        if i < len(num_array)-1 and char == "+":
            
            if i == 1:
                res += add(num_array[i-1], num_array[i + 1])
            else:
                res = add(res, num_array[i+1] )

        if i < len(num_array)-1 and char == "-":
            
            if i == 1:
                res += subtract(num_array[i-1], num_array[i + 1])
            else:
                res = subtract(res, num_array[i+1] )
        
        if i < len(num_array)-1 and char == "/":
            
            if i == 1:
                res += divide(num_array[i-1], num_array[i + 1])
            else:
                res = divide(res, num_array[i+1] )
        
        if i < len(num_array)-1 and char == "*":
            
            if i == 1:
                res += multiply(num_array[i-1], num_array[i + 1])
            else:
                res = multiply(res, num_array[i+1] )
        
    return(res)


