
def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return '<b>' + result + '</b>'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return '<i>' + result + '</i>'
    return wrapper

@italic
@bold
def powitanie(name):
    return f"Yo {name}. Be awesome!"

print(powitanie("Kuba"))