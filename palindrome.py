def reverse(string):
    """Reverse a String."""
    return "".join(reversed(string));

def ispalindrome(string):
    """Return True if the given string is a palindrome, False Otherwise."""
    processed_content = string.lower() 
    return processed_content == reverse(processed_content)

