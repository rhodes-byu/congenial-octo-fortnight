def hungry(is_hungry = True):

    if is_hungry:
        print("I am hungry")
        return "I am hungry"

    else:
        raise Exception("I am not hungry")