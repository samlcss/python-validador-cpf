# -*- coding: utf-8 -*-
"""
Validador simples de formato de CPF (apenas os 11 números, sem pontos nem hífen).
"""

import re

print("* * * VALIDADOR DE CPF (11 DÍGITOS) * * *\n")
cpf = input("Entre com o número do CPF (apenas números, sem ponto e sem hífen):\n").strip()

# Valida se contém exatamente 11 dígitos numéricos
if re.search(r"^\d{11}$", cpf):
    print("\n[OK] Número de CPF validado no formato correto (11 dígitos)!")
else:
    print("\n[ERRO] Número do CPF fora do padrão. Deve conter exatamente 11 dígitos numéricos.")

input("\nPressione Enter para sair...")
