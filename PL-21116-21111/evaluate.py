from pprint import PrettyPrinter

pp = PrettyPrinter()


class Evaluate:

    operators = {
        "ESCREVER": lambda args: Evaluate.escrever(args),
        "VAR": lambda args: Evaluate.variaveis(args),
        "COMENTAR": lambda args: Evaluate.comentar(args),
    }
    

    @staticmethod
    def evaluate(args):
        if type(args) is list:
            ans = None
            for a in args:
                ans = Evaluate.evaluate(a)
            return ans
        if args['args'] in Evaluate.operators:
            f = Evaluate.operators[args['args']]
            return f(args)
        
    @staticmethod
    def escrever(args):
        ops = args['ops']
        frase = ''
        conta = ''
        if 'var' in ops and 'string' in ops['var']:
            frase = ops['var']['string']

        verifica = False
        if 'cont' in ops:
            ops = ops['cont']
        while verifica == False:
            if 'cont' not in ops:
                verifica = True

            if 'var' in ops:
                if 'numero' in ops['var']:
                    contaARV = ops['var']
                    veri = False
                    while veri == False:
                        if 'numero2' not in contaARV:
                            veri = True

                        if 'numero' in contaARV:
                            conta = conta + str(contaARV['numero']['numero'])

                        if 'ops' in contaARV:
                            conta = conta + contaARV['ops']

                        if 'numero2' in contaARV:
                            contaARV = contaARV['numero2']
                    frase = frase + "%d"

                if 'string' in ops['var']:
                    frase = frase + ops['var']['string']

            if 'args' in ops:
                frase = frase + " " + ops['args']['string']

            if 'cont' in ops:
                ops = ops['cont']

        resultado = eval(conta)

        frase = frase % resultado

        print(frase)

    @staticmethod
    def variaveis(args):
        ops = args['ops']
        #print(ops)
        variavel = ''
        valor = ''
        if 'var' in ops and 'string' in ops['var']:
            variavel = ops['var']['string']

        if 'val' in ops:
            if 'string' in ops['val']:
                valor = ops['val']['string']

            if 'numero' in ops['val']:
                valor = ops['val']['numero']

        if variavel != '' and valor != '':
            print(f"Variavel {variavel} = {valor}")
            return {variavel: valor}
        else:
            print("Erro ao declarar variavel")
            return None
        
    @staticmethod
    def comentar(args):
        ops = args['ops']
        comment = ''
        if 'string' in ops:
            comment = ops['string']
        print(f"//{comment}")



    