import Lexer as lx
import Parser as pr

def ejeparser ()->None:
    text=input("Enter the text to be analyzed, the file must be in the same folder as the console: ")
    tokens=lx.lexer(text)
    parser=pr.ParserMain(tokens)
    print (parser)

def initializeapp ()->None:
    ejeparser()

initializeapp()