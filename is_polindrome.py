palindrome_text = input('Please enter only text: ')
rev_palindrome_text = palindrome_text[::-1]
print('reversed string',rev_palindrome_text)
if  palindrome_text == rev_palindrome_text:
    print('String is palindrome')
else:
    print('String is not palindrome')