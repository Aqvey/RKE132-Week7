def get_greeting(daytime):
    
    if daytime < 12:
        return "Tere hommikust"
    elif daytime < 18:
        return "Tere päevast"
    else:
        return "Tere õhtust"

