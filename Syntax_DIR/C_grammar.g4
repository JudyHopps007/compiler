grammar C;

program: (function | declaration)*;

function: type ID '(' params ')' compound_statement;

declaration: type ID ';';

params: (type ID (',' type ID)*)?;

compound_statement: '{' (statement)* '}';

statement: (declaration | assignment | if_statement | while_statement | return_statement | compound_statement | expression_statement) ';';

assignment: ID '=' expression;

if_statement: 'if' '(' expression ')' statement ('else' statement)?;

while_statement: 'while' '(' expression ')' statement;

return_statement: 'return' expression?;

expression_statement: expression;

expression: (term (op term)*)?;

term: ID | INT | '(' expression ')';

op: '+' | '-' | '*' | '/' | '%' | '>' | '<' | '>=' | '<=' | '==' | '!=' | '&&' | '||';

type: 'int' | 'float' | 'char' | 'double';

ID: [a-zA-Z][a-zA-Z0-9_]*;

INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;
