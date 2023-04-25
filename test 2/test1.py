list = "(program (include_list #include <stdio.h>) (include_list #include <stdbool.h>) (function (type_specifier int) addition ( (params (type_specifier int) a , (type_specifier int) b) ) (compound_statement { (statement (initializing (type_specifier int) result = (expression (term a) (operator +) (term b)) ;) (return_statement return (expression (term result)) ;)) })) (function (type_specifier int) subtraction ( (params (type_specifier int) a , (type_specifier int) b) ) (compound_statement { (statement (initializing (type_specifier int) result = (expression (term a) (operator -) (term b)) ;) (return_statement return (expression (term result)) ;)) })) (function (type_specifier float) multiplication ( (params (type_specifier float) a , (type_specifier float) b) ) (compound_statement { (statement (initializing (type_specifier int) result = (expression (term a) (operator *) (term b)) ;) (return_statement return (expression (term result)) ;)) })) (function (type_specifier float) division ( (params (type_specifier float) a , (type_specifier float) b) ) (compound_statement { (statement (initializing (type_specifier int) result = (expression (term a) (operator /) (term b)) ;) (return_statement return (expression (term result)) ;)) })) (function (type_specifier char) boolCheck ( (params (type_specifier int) a) ) (compound_statement { (statement (declaration (type_specifier char) mychar ;) (if_statement if ( (condition_statement_RFC (expression (term a)) == (expression (term 1))) ) { (statement (assignment mychar = (expression 'T') ;) (return_statement return (expression (term mychar)) ;)) } else { (statement (assignment mychar = (expression 'F') ;) (return_statement return (expression (term mychar)) ;)) })) })) (main_function (type_specifier void) main ( params ) (compound_statement { (statement (initializing (type_specifier bool) state = (expression (term true)) ;) (initializing (type_specifier int) c = (expression (term 3)) ;) (initializing (type_specifier int) d = (expression (term 5)) ;) (initializing (type_specifier float) e = (expression (term 6.0)) ;) (initializing (type_specifier float) f = (expression (term 12.0)) ;) (declaration (type_specifier float) newResult1 ;) (declaration (type_specifier int) newResult2 ;) (initializing (type_specifier int) select = (expression (term 3)) ;) (while_statement while ( (condition_statement_RFC state) ) { (statement (if_statement if ( (condition_statement_RFC (expression (term select)) == (expression (term 1))) ) { (statement (assignment newResult1 = (function_call division ( (expression (term f)) , (expression (term e)) ) ;))) } else if ( (condition_statement_RFC (expression (term select)) == (expression (term 2))) ) { (statement (assignment newResult1 = (function_call multiplication ( (expression (term f)) , (expression (term e)) ) ;))) } else if ( (condition_statement_RFC (expression (term select)) == (expression (term 3))) ) { (statement (assignment newResult2 = (function_call addition ( (expression (term c)) , (expression (term d)) ) ;))) } else { (statement (assignment newResult2 = (function_call subtraction ( (expression (term c)) , (expression (term d)) ) ;))) })) })) })))"
from collections import deque

def print_parse_tree(parse_tree_string: str, prefix: str = '', is_last: bool = True) -> None:
    tokens = deque(parse_tree_string.split("("))
    node = tokens.popleft()
    print(f"{prefix}{'└── ' if is_last else '├── '}{node}")

    def print_children(tokens, prefix):
        while tokens:
            node = tokens.popleft()
            if '(' in node:
                print_parse_tree(' '.join(tokens), prefix + ('    ' if len(tokens) == 1 else '│   '), tokens[-1] == node)
                break
            else:
                print(f"{prefix}{'└── ' if not tokens else '├── '}{node}")

    if any('(' in node for node in tokens):
        print_children(tokens, prefix)
    else:
        while tokens:
            print(f"{prefix}└── {tokens.popleft().replace('(', '').replace(')', '')}")

print_parse_tree(list)
tokens = deque(list.split('('))
print(tokens)

