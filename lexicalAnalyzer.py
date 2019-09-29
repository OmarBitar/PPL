# CS3210 - Principles of Programming Languages - Fall 2019
# A Lexical Analyzer for an expression

from enum import Enum
import sys

# all char classes
class CharClass(Enum):
    EOF        = 1
    LETTER     = 2
    DIGIT      = 3
    OPERATOR   = 4
    PUNCTUATOR = 5
    QUOTE      = 6
    BLANK      = 7
    OTHER      = 8
    KEYWORD    = 9

# reads the next char from input and returns its class
def getChar(input):
    if len(input) == 0:
        return (None, CharClass.EOF)
    c =input[0].lower()
    if c in [
        "program"
        ,"begin"
        ,"then" 
        ,"true" 
        ,"false"
        ,"var"  
        ,"while"
        ,"write"
        ,"program"
        ,"read"
        ,"do"  
        ,"else"
        ,"end."
        ,"end" 
        ,"begin"  
        ,"Boolean"
        ,"integer"    
        ]:
        return (c,CharClass.KEYWORD)
    else: 
        c = list(input[0].lower())
        for index in c:    
            if index.isalpha():
                return (index, CharClass.LETTER)
            if index.isdigit():
                return (index, CharClass.DIGIT)
            if index == '"':
                return (index, CharClass.QUOTE)
            if index in ['+', '-', '*', '/', '>', '=', '<']:
                return (index, CharClass.OPERATOR)
            if index in [':', ',', ';']:
                return (index, CharClass.PUNCTUATOR)
            if index in [' ', '\n', '\t']:
                return (index, CharClass.BLANK)
            return (index, CharClass.OTHER)

# calls getChar and getChar until it returns a non-blank
def getNonBlank(input):
    ignore = ""
    while True:
        c, charClass = getChar(input)
        if charClass == CharClass.BLANK:
            input, ignore = addChar(input, ignore)
        else:
            return input

# adds the next char from input to lexeme, advancing the input by one char
def addChar(input, lexeme):
    if len(input) > 0:
        lexeme += input[0]
        input = input[1:]
    return (input, lexeme)

# all tokens
class Token(Enum): 
    ADDITION         = 1
    ASSIGNMENT       = 2
    BEGIN            = 3
    BOOLEAN_TYPE     = 4 
    COLON            = 5
    DO               = 6
    ELSE = 7
    END = 8
    EQUAL = 9
    FALSE = 10
    GREATER = 11
    GREATER_EQUAL = 12
    IDENTIFIER = 13
    IF = 14
    INTEGER_LITERAL = 15
    INTEGER_TYPE = 16
    LESS = 17
    LESS_EQUAL = 18
    MULTIPLICATION = 19
    PERIOD = 20
    PROGRAM = 21
    READ = 22
    SEMICOLON = 23
    SUBTRACTION = 24
    THEN = 25
    TRUE = 26
    VAR = 27
    WHILE = 28
    WRITE = 29


# lexeme to token conversion
lookup = { 
    "+"      : Token.ADDITION       ,
    ":="      : Token.ASSIGNMENT     ,
    "begin"      : Token.BEGIN         ,
    "Boolean"      : Token.BOOLEAN_TYPE   ,
    ":"      : Token.COLON          ,
    "do"      : Token.DO              ,
    "else"      : Token.ELSE,
    "end"      : Token.END,
    "end."      : Token.END,
    "="      : Token.EQUAL,
    "false"      : Token.FALSE ,
    ">"      : Token.GREATER ,
    ">="      : Token.GREATER_EQUAL , 
    "if"      : Token.IF , 
    "<"      : Token.LESS ,
    "<="      : Token.LESS_EQUAL ,
    "*"      : Token.MULTIPLICATION ,
    "."      : Token.PERIOD ,
    "program"      : Token.PROGRAM ,
    "read"      : Token.READ ,
    ";"      : Token.SEMICOLON ,
    "-"      : Token.SUBTRACTION ,
    "then"      : Token.THEN ,
    "true"      : Token.TRUE ,
    "var"      : Token.VAR ,
    "while"      : Token.WHILE ,
    "write"      : Token.WRITE ,
    "integer"    : Token.INTEGER_LITERAL
}

# returns the next (lexeme, token) pair or None if EOF is reached
def lex(input): 
    input = getNonBlank(input)  

    c, charClass = getChar(input)
    lexeme = ""

    # check EOF first
    if charClass == CharClass.EOF:
        return (input, None, None)

    # reading letters
    if charClass == CharClass.LETTER:
        input, lexeme = addChar(input, lexeme)
        return (input, lexeme, Token.IDENTIFIER)

    # reading quotes
    if charClass == CharClass.QUOTE:
        input, lexeme = addChar(input, lexeme)
        return (input, lexeme, Token.IDENTIFIER)

    # reading digits
    if charClass == CharClass.DIGIT:
        while True:
            input, lexeme = addChar(input, lexeme)
            c, charClass = getChar(input)
            if charClass != CharClass.DIGIT:
                break
        return (input, lexeme, Token.INTEGER_TYPE)

    # reading an operator
    if charClass == CharClass.OPERATOR:
        input, lexeme = addChar(input, lexeme)
        if lexeme in lookup:
            return (input, lexeme, lookup[lexeme])

    # reading an PUNCTUATOR
    if charClass == CharClass.PUNCTUATOR:
        input, lexeme = addChar(input, lexeme)
        if lexeme in lookup:
            return (input, lexeme, lookup[lexeme])

    # reading an KEYWORD
    if charClass == CharClass.KEYWORD:
        input, lexeme = addChar(input, lexeme)
        if lexeme in lookup:
            return (input, lexeme, lookup[lexeme])

    

    # anything else, raise an exception
    print("error at: ",c)
    raise Exception("Lexical Analyzer Error: unrecognized symbol was found!")