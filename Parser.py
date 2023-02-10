


def ParseMain(lexemes):
    
    # a program of 5 or more tokens is guaranteed

    if len(lexemes) < 5:
        return "The input is syntactically incorrect"
    
    else:
        return ParseStartSymbol(lexemes)


def ParseStartSymbol(lexemes):

    # If the first token is not the keyword ROBOT_R, the input is syntactically incorrect

    first_token = First_Token(lexemes)
    
    if first_token != 'kw ROBOT_R':
        return "The input is syntactically incorrect"
    
    # In the other case, we parse the remaing lexemes
    else:
        
        ## we obtain the next token and the remaing lexemes and continue parsing
        
        next_token = NextToken(lexemes) 
        remaining_lexemes = Remaining_Lexemes(lexemes)

        return ParseStartSymbolPrime(next_token, remaining_lexemes)
        
def First_Token(lexemes):
    return lexemes[0]


def NextToken(remaing_lexemes):
    return remaing_lexemes[1]


def Remaining_Lexemes(lexemes):
    
    lenght = len(lexemes)
    return lexemes[2:lenght]


def ParseStartSymbolPrime(next_token, remaining_lexemes):
    pass


def getToken(List_Tokens):
    pass

def First_Token(lexemes):
    return lexemes[0]