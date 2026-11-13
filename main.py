from fc import fundamentos_de_computadores
from algebra import algebra_final_score
def main():
    print("\033[38;2;0;102;166m" + r"""
██    ██ ██      ██████   ██████   ██████
██    ██ ██      ██   ██ ██       ██
██    ██ ██      ██████  ██   ███ ██
██    ██ ██      ██      ██    ██ ██
 ██████  ███████ ██       ██████   ██████

███████ ██ ██       ███    ██  ██████  ████████  █████  ███████    ██ ███
██      ██ ██       ████   ██ ██    ██    ██    ██   ██ ██        ███ █ █
█████   ██ ██       ██ ██  ██ ██    ██    ██    ███████ ███████    ██ ███
██      ██ ██       ██  ██ ██ ██    ██    ██    ██   ██      ██    ██
███████ ██ ██       ██   ████  ██████     ██    ██   ██ ███████    ██
"""
+ "\033[0m")
    subject = input("Select a subject to calculate your grade\n" \
    "[1] - Habilidades Profesionales para Ingenieros\n" \
    "[2] - Fundamentos de Programación 1\n" \
    "[3] - Fundamentos de Computadores\n" \
    "[4] - Álgebra y Geometría\n" \
    "[5] - Matemática Discreta\n" \
    "Option: ").strip()

    match subject:
        case "1":
            pass
        case "2":
            pass
        case "3":
            fundamentos_de_computadores()
        case "4":
            pass
        case "5":
            pass

main()