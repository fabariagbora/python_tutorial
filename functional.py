states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]

def urlify(state):
    return "-".join(state.lower().split());


#urls: imperative version
def imperative_urls(states):
    urls = []
    for state in states:
        urls.append("-".join(state.lower().split()))
    return urls

print(imperative_urls(states));


# urls: functional version
def functional_urls(states):
    return [urlify(state) for state in states]

print(functional_urls(states));
 
# Web Urls function

def web_urlify(state):
    return f'https://example.com/{urlify(state)}'

def web_urls(states):
    return [web_urlify(state) for state in states]