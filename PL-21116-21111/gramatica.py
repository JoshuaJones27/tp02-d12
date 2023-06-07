from lexer import lexer
import ply.yacc as pyacc
import random

class Gramatica:
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = lexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)
    
    def p_S(self, p):
        """ S : com """
        p[0] = p[1]
    
    def p_S1(self, p):
        """ S : S com """
        p[0] = p[1] 
        p[0].append(p[2])

    def p_com(self,p):
        """ com : ESCREVER escreverops
                | VAR variavel 
                | COMENTAR string """
        p[0] = { 'args': p[1], 'ops': p[2] }

    def p_comentar(self, p):
        """ comentar : string """
        p[0] = { 'string': p[2] }

    def p_escreverops(self, p):
        """ escreverops : string
                        | contas
                        | string ',' escreverops 
                        | contas ',' escreverops"""
        if len(p) == 2:
            p[0] = { 'args': p[1] }
        if len(p) == 4:
            p[0] = { 'var': p[1], 'cont': p[3] }

    def p_contas(self, p):
        """ contas : numero '*' contas
                   | numero '+' contas
                   | numero '-' contas 
                   | numero '/' contas 
                   | numero """
        if len(p) == 2:
            p[0] = { 'numero': p[1]}
        if len(p) == 4:
            p[0] = { 'numero': p[1], 'ops': p[2], 'numero2': p[3] }

    def p_variavel(self, p):
        """ variavel : string '=' string
                     | string '=' numero 
                     | string """
        if len(p) == 2:
            p[0] = { 'var': p[1] }
        if len(p) == 4:
            p[0] = { 'var': p[1], 'val': p[3] }

    def p_error(self, p):
        if p:
            print(f"Syntax error: unexpected '{p.type}'")
        else:
            print("Syntax error: unexpected end of file")
        exit(1)