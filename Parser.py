


def ParseMain(lexemes):
    
    # a program of 5 or more tokens is guaranteed

    if len(lexemes) < 5:
        return "The input is syntactically incorrect"

    # if the last lexem isn't a bracket, then the program is incorrect

    if lexemes[len(lexemes)-1] != 'sp ]':

        return "The input is syntactically incorrect"
    
    else:
        return ParseStartSymbol(lexemes)


def ParseStartSymbol(lexemes):

    # If the first token is not the keyword ROBOT_R, the input is syntactically incorrect

    first_token = NextToken(lexemes) 
    remaining_lexemes = Remaining_Lexemes(lexemes)

    if first_token != 'kw ROBOT_R':
        return "The input is syntactically incorrect"
    
    # In the other case, we parse the remaing lexemes
    else:
        
        ## we obtain the next token and the remaing lexemes and continue parsing
        
        next_token = NextToken(remaining_lexemes) 
        remaining_lexemes = Remaining_Lexemes(remaining_lexemes)
        
        return Parse_Start_Symbol_Prime(next_token, remaining_lexemes)
        

def NextToken(remaing_lexemes):
    return remaing_lexemes[0]


def Remaining_Lexemes(lexemes):
    
    lenght = len(lexemes)
    return lexemes[1:lenght]


def Parse_Start_Symbol_Prime(first_token_remaing_lexemes, remaining_lexemes):
    
    # If the first token of the remaining lexemes is a "[", then a block of instructions will follow 
    
    if first_token_remaing_lexemes == 'sp [':
        
        next_token = NextToken(remaining_lexemes) 
        remaining_lexemes = Remaining_Lexemes(remaining_lexemes)

        return Parse_Block_of_Instructions(next_token, remaining_lexemes)


    # If the first token of the remaining lexemes is the keyword VARS, then a block of instructions will follow 
         
    elif first_token_remaing_lexemes == 'kw VARS':
        
        next_token = NextToken(remaining_lexemes) 
        remaining_lexemes = Remaining_Lexemes(remaining_lexemes)

        return Parse_VARS_and_PROCS(next_token, remaining_lexemes)

    # In the other case, the input would be syntactically incorrect

    else:
        return "The input is syntactically incorrect"

def Parse_Block_of_Instructions(first_token_remaing_lexemes, remaining_lexemes):
    pass

def Parse_VARS_and_PROCS(first_token_remaing_lexemes, remaining_lexemes):
    pass