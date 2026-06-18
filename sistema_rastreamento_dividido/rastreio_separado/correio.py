import json
import random
import string
import os

DB_PATH = 'banco_simulado.json'

def carregar_banco():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def salvar_banco(banco):
    with open(DB_PATH, 'w') as f:
        json.dump(banco, f, indent=4)

def gerar_codigo():
    prefixo = 'BR'
    sufixo = 'BR'
    numeros = ''.join(random.choices(string.digits, k=9))
    return f"{prefixo}{numeros}{sufixo}"

def registrar_novo_pacote():
    banco = carregar_banco()
    while True:
        codigo = gerar_codigo()
        if codigo not in banco:
            break
    banco[codigo] = {
        'status': 'Postado',
        'historico': [
            {'local': 'Agência Central', 'status': 'Postado'}
        ]
    }
    salvar_banco(banco)
    return codigo

def rastrear(codigo):
    banco = carregar_banco()
    return banco.get(codigo.upper())
