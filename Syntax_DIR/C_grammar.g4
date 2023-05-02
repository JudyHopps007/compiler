grammar C_grammar;


program             : statement+;
statement           : assignment
                    | conditional
                    | loop
                    | print_statement
                    | function_definition
                    | procedure_definition
                    | function_call
                    | procedure_call
                    | return_statement
                    | array_declaration
                    | list_declaration
                    | array_access
                    | list_access
                    | class_declaration;

assignment          : identifier '=' expression;
conditional         : 'if' expression ':' program ('else' ':' program)?;
loop                : 'while' expression ':' program;
print_statement     : 'print' expression;
function_definition : 'def' identifier '(' parameter_list? ')' ':' program;
procedure_definition: 'procedure' identifier '(' parameter_list? ')' ':' program;
parameter_list      : parameter (',' parameter)*;
parameter           : identifier;
function_call       : identifier '(' argument_list? ')';
procedure_call      : identifier '(' argument_list? ')';
argument_list       : expression (',' expression)*;
return_statement    : 'return' expression?;
array_declaration   : identifier '[' expression ']';
list_declaration    : identifier '[' expression_list ']';
expression_list     : expression (',' expression)*;
array_access        : identifier '[' expression ']';
list_access         : identifier '[' expression ']';
class_declaration   : 'class' identifier (':' identifier)? '{' class_body '}';
class_body          : member+;
member              : attribute_declaration | method_declaration;
attribute_declaration: identifier (':' datatype)?;
method_declaration  : function_definition;

expression          : log_expr;
log_expr            : relation (log_op relation)*;
relation            : arith_expr (rel_op arith_expr)?;
arith_expr          : term (add_op term)*;
term                : factor (mul_op factor)*;
factor              : number | identifier | '(' expression ')' | '-' factor;
identifier          : ALPHA (ALPHA_NUM)*;
number              : DIGIT+;
datatype            : 'int' | 'float' | 'string' | 'bool';

ALPHA               : [a-zA-Z];
ALPHA_NUM           : [a-zA-Z0-9];
DIGIT               : [0-9];

add_op              : '+' | '-';
mul_op              : '*' | '/';
rel_op              : '<' | '<=' | '>' | '>=' | '==' | '!=';
log_op              : 'and' | 'or';

WS                  : [ \t\r\n]+ -> skip;


