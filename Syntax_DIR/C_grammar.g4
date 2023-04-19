grammar C_grammar;

program: (include_list | declaration | function)* main_function?;

include_list: '#include' INCLUDE_DIRECTIVE;

function: type_specifier IDENTIFIER '(' params ')' compound_statement;

main_function: type_specifier 'main' '(' params ')' compound_statement;

declaration: type_specifier IDENTIFIER ';';

params: (type_specifier IDENTIFIER (',' type_specifier IDENTIFIER)*)?;

compound_statement: '{' statement '}';

statement: (declaration | initializing | function_call | assignment | if_statement | while_statement | return_statement)*;

assignment: (IDENTIFIER '=' expression ';') | (IDENTIFIER '=' function_call) ;

function_call: IDENTIFIER '(' expression (',' expression)*  ')' ';';

initializing: type_specifier IDENTIFIER '=' expression ';';

if_statement: 'if' '(' condition ')' '{' statement '}' ('else if' '(' condition ')' '{' statement '}')* ('else' '{' statement '}')?;

while_statement: 'while' '(' condition ')' '{' statement '}';

condition : (expression CONDITIONAL_OPERATOR expression) | IDENTIFIER;

return_statement: 'return' expression ';';

expression: (term (operator term)*) | CHAR_LITERAL | STRING_LITERAL;

term: IDENTIFIER | INTEGER | FLOAT| BOOLEAN;

operator: '+' | '-' | '*' | '/' | '%' | '&&' | '||';

CONDITIONAL_OPERATOR : '==' | '!=' | '<' | '>' | '<=' | '>=';

LOGICAL_OPERATOR: '&&' | '||' | '!';

type_specifier: 'int' | 'float' | 'char' | 'double' | 'void' | 'bool' | 'long';

IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

INTEGER: [0-9]+;

FLOAT: [0-9]+ '.' [0-9]+;

INCLUDE_DIRECTIVE : '<' [A-Za-z]+ '.h>';

CHAR_LITERAL : '\'' . '\'';

STRING_LITERAL : '"' ~('"')* '"';

BOOLEAN: 'true' | 'false';

SING_LINE_COMMENT: '//' ~[\n\r]* -> skip;

WS: [ \t\r\n]+ -> skip;

