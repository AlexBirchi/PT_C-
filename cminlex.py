reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'return': 'RETURN',
    'void': 'VOID',
    'int': 'INT',
}

tokens = [
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',

    'ASIGN',

    'SEMI', 'COMMA',
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',

    'ID', 'NUM',

    'COMMENT'
] + list(reserved.values())

t_ignore           = ' \t'

t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'

t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

t_ASIGN            = r'='

t_SEMI             = r';'
t_COMMA            = r','
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'

t_NUM              = r'\b(?<!\.)[0-9]+(?![\.\d])'

t_COMMENT          = r'/\*(.|\n)*?\*/'


def t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t