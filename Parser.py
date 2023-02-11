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
        
def Parse_Start_Symbol_Prime(first_token_remaing_lexemes, remaining_lexemes):
    
    # If the first token of the remaining lexemes is a "[", then a block of instructions will follow 

    if first_token_remaing_lexemes == 'sp [':
        
        next_token = NextToken(remaining_lexemes) 
        remaining_lexemes = Remaining_Lexemes(remaining_lexemes)

        return Parse_Block_of_Instructions(next_token, remaining_lexemes)


    # If the first token of the remaining lexemes is the keyword VARS, then a list of variables and procedure definitions must follow
         
    elif first_token_remaing_lexemes == 'kw VARS':

        next_token = NextToken(remaining_lexemes) 
        remaining_lexemes = Remaining_Lexemes(remaining_lexemes)

        return Parse_VARS_and_PROCS(next_token, remaining_lexemes)

    # In the other case, the input would be syntactically incorrect

    else:
        return "The input is syntactically incorrect"

def Parse_Block_of_Instructions(first_token_remaing_lexemes, remaining_lexemes): ## MISSING
    pass

def Parse_VARS_and_PROCS(first_token_remaing_lexemes, remaining_lexemes):
    
    
    # We check whether the first token after kw VARS be an id

    # if (len(first_token_remaing_lexemes) >= 4) and (first_token_remaing_lexemes[0:3] =='id'):


    #     # VARS must end with a semicolon

    #     if "sp ;" not in remaining_lexemes:

    #         return "The input is syntactically incorrect"
        
    #     # after the semicolon there must be a kw PROCS

    #     else:
    #         pos_of_semicolon = remaining_lexemes.index("sp ;")
    #         token_after_semicolon = remaining_lexemes[pos_of_semicolon+1]

    #         if token_after_semicolon == "kw PROCS":

    #             next_token = NextToken(remaining_lexemes) 
    #             remaining_lexemes = Remaining_Lexemes(remaining_lexemes)

    #             #verificamos
    #             correct_vars_syntaxis =  Parse_List_VARS(next_token, remaining_lexemes)
                
    #             if correct_vars_syntaxis
    #         else:





    #         # We check if there's only one var, then the procedure definition must follow
    #         if next_token == "sp ;":
                
    #             next_token = NextToken(remaining_lexemes) 
    #             remaining_lexemes = Remaining_Lexemes(remaining_lexemes)

    #             # After the colon, the kw PROCs must follow

    #             if next_token == "kw PROCS":
                
    #                 next_token = NextToken(remaining_lexemes) 
    #                 remaining_lexemes = Remaining_Lexemes(remaining_lexemes)
                
    #                 return Parse_Procedure_definition(next_token, remaining_lexemes)
                
    #             # if the kw PROCs doesn't follow after the list of variables, it is an error
                
    #             else:
    #                 return "The input is syntactically incorrect"
        
    #         else:

    #             return Parse_List_VARS(next_token, remaining_lexemes)

    # # If the list of VARS is empty, then the input would be syntactically incorrect
    
    # else:
    #     return "The input is syntactically incorrect"

    pass


def Parse_List_VARS(next_token, remaining_lexemes):
    
    # we chech if there are more variables, if so we parse again
    if next_token == 'sp ,':
        
        next_token = NextToken(remaining_lexemes) 
        remaining_lexemes = Remaining_Lexemes(remaining_lexemes)
        
        return Parse_List_VARS_Prime()
    

def Parse_List_VARS_Prime():
    if next_token == 'sp ,':
        
        next_token = NextToken(remaining_lexemes) 
        remaining_lexemes = Remaining_Lexemes(remaining_lexemes)

        return Parse_VARS_and_PROCS(next_token, remaining_lexemes)

    else:
        return "The input is syntactically incorrect"

def Parse_Procedure_definition(next_token, remaining_lexemes):
    pass

## HELPER FUNCTIONS

def NextToken(remaing_lexemes):
    return remaing_lexemes[0]

def Remaining_Lexemes(lexemes):
    
    length = len(lexemes)
    return lexemes[1:length]


# input = ["kw ROBOT_R", "kw VARS","sp ;","kw PROCS","sp [","sp ]"]

# print(ParseMain(input))