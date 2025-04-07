"""
Write a function that checks if a string is a palindrome.
"""

def check_palindrome(string_to_check: str):
        if string_to_check == string_to_check[::-1]:
            print(f"Congrats, '{string_to_check}' is a palindrome!")
        else:
            print(f"Sorry, '{string_to_check}' is NOT a palindrome")

while True:
    phrase_to_check = (input("What phrase would you like to check? (q to quit)"))

    if phrase_to_check in ["q", "Q"]: 
        print(f"Thank you for playing!")
        break
    else:
         check_palindrome(phrase_to_check)

    
