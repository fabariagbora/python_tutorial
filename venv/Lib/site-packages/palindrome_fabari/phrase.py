import re
class Phrase:
    """A class to represent phrases."""
    def __init__(self, content):
        self.content = str(content)
    def processed_content(self):
        """Process the content for palindrome testing."""
        return self.letters_and_digits().lower()
    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self.processed_content() == reverse(self.processed_content())
     
    def letters(self):
        """Return only the letters in the content."""
        return "".join(re.findall(r"[A-Za-z]", self.content))
    
    def letters_and_digits(self):
        """Return only the letters and digits in the content."""
        return "".join(re.findall(r"[A-Za-z0-9]", self.content))

def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string));

    