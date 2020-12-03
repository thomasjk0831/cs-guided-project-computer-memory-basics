"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here
    # return string.lower()
    '''
    Input: string containing lower and uppercase letters
    Output: the lowercased string 

    ASCII representation of letters maps letters to numbers 
    lowercase letters a..z are mapped to 97..122 
    uppercase letters A..Z are mapped to 65..90
    97 - 65 = 32
    122 - 90 = 32 

    To take a lowercase letter and capitalize it, subtract 32 to its ascii number 
    To take an uppercase letter and lowercase it, add 32 to its ascii number 

    Strategy:
    Look through each letter in the input string 
    If it's an uppercase letter, add 32 to its ascii value 
    If it's already lowercased, then we don't need to do anything 

    How would we check if a letter is upper or lowercased? There are built-ins for 
    this, but we're not allowed to use them. 

    Turn ever letter in the input into its ascii number 
    Iterate through all of the ascii numbers of the input 
        Check and see if any of those numbers falls into the range 65..90 
        add 32 to that ascii value 
    Turn the ascii values back into a string 
    
    '''
    # for l in string:
    #     ascii_values.append(ord(l))

    # 1. turn all letters in the input into their corresponding ascii values 
    # what's the runtime of the `ord` and `chr` functions? O(1)
    ascii_values = [ord(l) for l in string] # O(n) time, O(n) space 

    for i, v in enumerate(ascii_values): # O(n) time 

    # for i in range(len(ascii_values)):
    #     v = ascii_values[i]

        if 65 >= v and v <= 90: # O(1)
            # lowercasing the letter 
            ascii_values[i] += 32 # O(1)
    
    # turn the ascii values back into a string 
    # letters = [chr(v) for v in ascii_values]

    return ''.join(chr(v) for v in ascii_values) # O(n) time


print(to_lower_case("LambdaSchool"))
