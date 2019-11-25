grammar AsmGrammar;

LPAREN : '(';
RPAREN : ')';
INTEGER : [0-9]+;
REGISTER: '%e'[a-d]'x';
PLUS : '+';
MINUS : '-';
MUL : '*';
INTERRUPT: 'int 0x80';
MOV: 'mov ';
XOR: 'xor ';
PUSH: 'push ';
SEPARATOR: ',';
END: [\n];
WS : (' ' | '\t') -> skip;
factor : INTEGER | REGISTER | LPAREN expr RPAREN;
term : factor | (factor MUL term);
expr : term | expr (PLUS | MINUS) term;
push_cmd : PUSH expr ;
int_cmd : INTERRUPT;
mov_cmd: MOV expr SEPARATOR REGISTER;
xor_cmd: XOR expr SEPARATOR REGISTER;
commands: (int_cmd | push_cmd | mov_cmd | xor_cmd) END ;


