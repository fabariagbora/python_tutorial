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

# singles: Imperative  version
def imperative_singles(states):
    singles = []
    for state in states:
        if len(state.split()) == 1:
            singles.append(state)
    return singles

print(imperative_singles(states));

#singles: functional version
def functional_singles(states):
    return [state for state in states if len(state.split()) == 1]

print(functional_singles(states));


# lengths: Imperative version
def imperative_lengths(states):
    lengths = {}
    for state in states:
        lengths[state] = len(state)
    return lengths

print(imperative_lengths(states));


# lengths: functional version
def functional_lengths(states):
    return {state: len(state) for state in states}

print(functional_lengths(states));


