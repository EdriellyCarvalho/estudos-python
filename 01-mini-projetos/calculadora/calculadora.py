import ast
import operator

# Operadores permitidos
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg
}

print("Seja Bem-vindo a Calculadora da Edri")

def eval_expr(expr):
        node = ast.parse(expr, mode='eval').body
        return _eval(node)
    
def _eval(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.Constant):
        return node.value
    elif isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        return operators[type(node.op)](left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        return operators[type(node.op)](operand)
    raise ValueError("Expressão inválida")

while True:
    print("\nOperaões disponíveis: + - * /")
    expr = input("Digite a expressão completa (ou 'sair' para encerrar): ")
    if expr.lower() == "sair":
        print("Encerrando a calculadora!")
        break
    try:
        resultado = eval_expr(expr)
        print("Resultado:", resultado)
    except Exception as e:
        print("Erro na expressão:", e)
