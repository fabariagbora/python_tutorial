import requests
from palindrome_fabari.phrase import Phrase


def main():
    detect_palindromes_url()

def detect_palindromes_url():
    URL = "https://cdn.learnenough.com/phrases.txt"

    palindromes = [line for line in requests.get(URL).content.decode("utf-8").splitlines()
                    if Phrase(line).ispalindrome()]
    
    palindrome_content = "\n".join(palindromes)
    
    with open("palindromes_url.txt", "w") as file:
        file.write(palindrome_content)


if __name__ == "__main__":
    main()

