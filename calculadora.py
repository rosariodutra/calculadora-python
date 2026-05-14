# =============================================================
#  🧮 CALCULADORA
#  Autor: Rosário Dutra
#  GitHub: github.com/rosariodutra
#  Descrição: Calculadora no terminal com operações básicas,
#             avançadas, histórico e exportação de resultados.
# =============================================================

import math
import os
from datetime import datetime

# ── Histórico da sessão ───────────────────────────────────────
historico = []

# ── Utilitários ───────────────────────────────────────────────

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cabecalho():
    print("\033[35m")
    print("╔══════════════════════════════════════╗")
    print("║          🧮  CALCULADORA  🧮           ║")
    print("║      github.com/rosariodutra          ║")
    print("╚══════════════════════════════════════╝")
    print("\033[0m")

def registrar(expressao, resultado):
    hora = datetime.now().strftime("%H:%M:%S")
    historico.append({"hora": hora, "expressao": expressao, "resultado": resultado})

def entrada_numero(mensagem):
    while True:
        try:
            return float(input(f"  {mensagem}: ").strip().replace(",", "."))
        except ValueError:
            print("  ⚠️  Digite um número válido!")

# ── Operações básicas ─────────────────────────────────────────

def operacoes_basicas():
    limpar()
    cabecalho()
    print("  ── Operações Básicas ──\n")
    print("  1. Adição       (+)")
    print("  2. Subtração    (-)")
    print("  3. Multiplicação (×)")
    print("  4. Divisão      (÷)")
    print("  5. Módulo       (%)")
    print("  6. Potência     (^)")
    print("  0. Voltar\n")

    op = input("  Opção: ").strip()
    if op == "0":
        return

    operadores = {"1": "+", "2": "-", "3": "×", "4": "÷", "5": "%", "6": "^"}
    if op not in operadores:
        print("  ⚠️  Opção inválida!")
        input("  [Enter para continuar]")
        return

    a = entrada_numero("Primeiro número")
    b = entrada_numero("Segundo número")

    try:
        if op == "1":   resultado = a + b
        elif op == "2": resultado = a - b
        elif op == "3": resultado = a * b
        elif op == "4":
            if b == 0:
                print("\n  ❌ Erro: divisão por zero!")
                input("  [Enter para continuar]")
                return
            resultado = a / b
        elif op == "5": resultado = a % b
        elif op == "6": resultado = a ** b

        expressao = f"{a} {operadores[op]} {b}"
        print(f"\n  \033[32m✅ Resultado: {expressao} = {resultado}\033[0m\n")
        registrar(expressao, resultado)

    except Exception as e:
        print(f"\n  ❌ Erro: {e}\n")

    input("  [Enter para continuar]")

# ── Operações avançadas ───────────────────────────────────────

def operacoes_avancadas():
    limpar()
    cabecalho()
    print("  ── Operações Avançadas ──\n")
    print("  1. Raiz quadrada  (√)")
    print("  2. Raiz cúbica    (∛)")
    print("  3. Logaritmo base 10")
    print("  4. Logaritmo natural (ln)")
    print("  5. Seno / Cosseno / Tangente")
    print("  6. Fatorial       (!)")
    print("  7. Valor absoluto (|x|)")
    print("  0. Voltar\n")

    op = input("  Opção: ").strip()
    if op == "0":
        return

    try:
        if op == "1":
            a = entrada_numero("Número")
            if a < 0:
                print("\n  ❌ Raiz de número negativo!")
                input("  [Enter]"); return
            resultado = math.sqrt(a)
            expressao = f"√{a}"

        elif op == "2":
            a = entrada_numero("Número")
            resultado = a ** (1/3) if a >= 0 else -((-a) ** (1/3))
            expressao = f"∛{a}"

        elif op == "3":
            a = entrada_numero("Número")
            if a <= 0:
                print("\n  ❌ Log de número não positivo!")
                input("  [Enter]"); return
            resultado = math.log10(a)
            expressao = f"log({a})"

        elif op == "4":
            a = entrada_numero("Número")
            if a <= 0:
                print("\n  ❌ Ln de número não positivo!")
                input("  [Enter]"); return
            resultado = math.log(a)
            expressao = f"ln({a})"

        elif op == "5":
            limpar(); cabecalho()
            print("  1. Seno\n  2. Cosseno\n  3. Tangente\n")
            sub = input("  Opção: ").strip()
            a = entrada_numero("Ângulo em graus")
            rad = math.radians(a)
            if sub == "1":   resultado = math.sin(rad); expressao = f"sen({a}°)"
            elif sub == "2": resultado = math.cos(rad); expressao = f"cos({a}°)"
            elif sub == "3": resultado = math.tan(rad); expressao = f"tan({a}°)"
            else:
                print("  ⚠️  Inválido!"); input("  [Enter]"); return

        elif op == "6":
            a = int(entrada_numero("Número inteiro"))
            if a < 0:
                print("\n  ❌ Fatorial de negativo!"); input("  [Enter]"); return
            resultado = math.factorial(a)
            expressao = f"{a}!"

        elif op == "7":
            a = entrada_numero("Número")
            resultado = abs(a)
            expressao = f"|{a}|"

        else:
            print("  ⚠️  Opção inválida!"); input("  [Enter]"); return

        print(f"\n  \033[32m✅ Resultado: {expressao} = {round(resultado, 10)}\033[0m\n")
        registrar(expressao, round(resultado, 10))

    except Exception as e:
        print(f"\n  ❌ Erro: {e}\n")

    input("  [Enter para continuar]")

# ── Histórico ─────────────────────────────────────────────────

def ver_historico():
    limpar()
    cabecalho()
    print("  ── Histórico da Sessão ──\n")

    if not historico:
        print("  Nenhum cálculo realizado ainda.\n")
        input("  [Enter para voltar]")
        return

    for i, item in enumerate(historico, 1):
        print(f"  {i:>2}. [{item['hora']}]  {item['expressao']} = \033[35m{item['resultado']}\033[0m")

    print(f"\n  Total: {len(historico)} cálculo(s)\n")
    print("  1. Exportar histórico (.txt)")
    print("  2. Limpar histórico")
    print("  0. Voltar\n")

    op = input("  Opção: ").strip()

    if op == "1":
        exportar_historico()
    elif op == "2":
        historico.clear()
        print("\n  ✅ Histórico limpo!")
        input("  [Enter para continuar]")

def exportar_historico():
    nome = f"historico_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(nome, "w", encoding="utf-8") as f:
        f.write("HISTÓRICO DE CÁLCULOS — Calculadora by Rosário Dutra\n")
        f.write(f"Exportado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
        for i, item in enumerate(historico, 1):
            f.write(f"{i}. [{item['hora']}]  {item['expressao']} = {item['resultado']}\n")
    print(f"\n  ✅ Exportado como: {nome}\n")
    input("  [Enter para continuar]")

# ── Conversor de unidades ─────────────────────────────────────

def conversor():
    limpar()
    cabecalho()
    print("  ── Conversor de Unidades ──\n")
    print("  1. Temperatura (°C ↔ °F ↔ K)")
    print("  2. Distância (km ↔ mi ↔ m)")
    print("  3. Peso (kg ↔ lb ↔ g)")
    print("  0. Voltar\n")

    op = input("  Opção: ").strip()
    if op == "0":
        return

    if op == "1":
        limpar(); cabecalho()
        print("  1. °C → °F\n  2. °F → °C\n  3. °C → K\n  4. K → °C\n")
        sub = input("  Opção: ").strip()
        a = entrada_numero("Valor")
        if sub == "1":   r = a*9/5+32;    e = f"{a}°C → °F"
        elif sub == "2": r = (a-32)*5/9;  e = f"{a}°F → °C"
        elif sub == "3": r = a+273.15;    e = f"{a}°C → K"
        elif sub == "4": r = a-273.15;    e = f"{a}K → °C"
        else: print("  ⚠️  Inválido!"); input("  [Enter]"); return

    elif op == "2":
        limpar(); cabecalho()
        print("  1. km → mi\n  2. mi → km\n  3. m → km\n  4. km → m\n")
        sub = input("  Opção: ").strip()
        a = entrada_numero("Valor")
        if sub == "1":   r = a*0.621371; e = f"{a} km → mi"
        elif sub == "2": r = a/0.621371; e = f"{a} mi → km"
        elif sub == "3": r = a/1000;     e = f"{a} m → km"
        elif sub == "4": r = a*1000;     e = f"{a} km → m"
        else: print("  ⚠️  Inválido!"); input("  [Enter]"); return

    elif op == "3":
        limpar(); cabecalho()
        print("  1. kg → lb\n  2. lb → kg\n  3. kg → g\n  4. g → kg\n")
        sub = input("  Opção: ").strip()
        a = entrada_numero("Valor")
        if sub == "1":   r = a*2.20462; e = f"{a} kg → lb"
        elif sub == "2": r = a/2.20462; e = f"{a} lb → kg"
        elif sub == "3": r = a*1000;    e = f"{a} kg → g"
        elif sub == "4": r = a/1000;    e = f"{a} g → kg"
        else: print("  ⚠️  Inválido!"); input("  [Enter]"); return
    else:
        print("  ⚠️  Opção inválida!"); input("  [Enter]"); return

    print(f"\n  \033[32m✅ Resultado: {e} = {round(r, 6)}\033[0m\n")
    registrar(e, round(r, 6))
    input("  [Enter para continuar]")

# ── Menu principal ────────────────────────────────────────────

def main():
    while True:
        limpar()
        cabecalho()
        print(f"  Cálculos realizados: \033[35m{len(historico)}\033[0m\n")
        print("  1. Operações Básicas")
        print("  2. Operações Avançadas")
        print("  3. Conversor de Unidades")
        print("  4. Ver Histórico")
        print("  0. Sair\n")

        op = input("  Opção: ").strip()

        if op == "1":   operacoes_basicas()
        elif op == "2": operacoes_avancadas()
        elif op == "3": conversor()
        elif op == "4": ver_historico()
        elif op == "0":
            limpar(); cabecalho()
            print(f"  Até logo! {len(historico)} cálculo(s) realizados nesta sessão. 💜\n")
            break
        else:
            print("  ⚠️  Opção inválida!")
            input("  [Enter para continuar]")

if __name__ == "__main__":
    main()
