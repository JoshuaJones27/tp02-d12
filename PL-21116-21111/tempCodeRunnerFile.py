import ply.lex as lex
from gramatica import Gramatica
from pprint import PrettyPrinter
from evaluate import Evaluate

pp = PrettyPrinter()
g = Gramatica()
g.build()

with open("entradas.ea", "r") as file:
    lines = file.read().splitlines()
    
    for line in lines:
        try:
            ans = g.parse(line.replace(';', ''))
            #pp.pprint(ans)
            answer = Evaluate.evaluate(ans)
            if answer is not None:
                print(f"<< {answer}")
        except Exception as e:
            print(f'\033[91m-> {e}\033[0m')
