import sys
import requests

from bs4 import BeautifulSoup

# Return the paragraphs from a Wikipedia link, stripped of reference numbers.
# Especially useful for text-to-speech (both native and foreign).

# Get URL from the command line.
url = sys.argv[1]


# Create Beautiful Soup document from live URL.
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; LearnEnoughPython/1.0)"
}

response = requests.get(url, headers=headers)
content = response.text

doc = BeautifulSoup(content, features="html.parser")

# Remove references.
for reference in doc("sup", class_="reference"):
    reference.decompose()

print(len(doc("p")))


# Print the paragraphs.
for paragraph_tag in doc("p"):   
    print(paragraph_tag.text)