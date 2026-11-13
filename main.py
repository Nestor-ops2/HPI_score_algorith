def theory_score(partial1, partial2, partial3, exam_score):
    average_controls = (partial1 + partial2 + partial3) / 3
    return 0.30 * average_controls + 0.70 * exam_score


def ask_grade(message):
    return float(input(message))

def fundamentos_de_computadores():
    """
    Ask users score in diferent evalation measures and process data
    calling different functions

    return the final score in fundamentos de computadores
    """
    partial1 = ask_grade("Enter your score in first partial exam: ")
    partial2 = ask_grade("Enter your score in second partial exam: ")
    partial3 = ask_grade("Enter your score in third partial exam: ")
    ordinary_score = ask_grade("Enter your score in ordinary exam (theory): ")

    practical_exam = ask_grade("Enter your score in practical exam: ")
    ae_score = ask_grade("Enter your average score in exercise quizzes (AE): ")
    ap_score = ask_grade("Enter your average score in lab quizzes (AP): ")

    theory = theory_score(partial1, partial2, partial3, ordinary_score)
    lab = practical_exam

    final = 0.40 * theory + 0.40 * lab + 0.10 * ae_score + 0.10 * ap_score

    if theory < 5 or lab < 5:
        final = min(final, 4)

    print(f"Theory: {theory:.2f}, Lab: {lab:2.f}, Final: {final:.2f}")
    return final

def HPI_final_score(linguistic_component: float, computing_component: float) -> float:
    """
    Calculates the final ordinary grade for 'Habilidades Profesionales para Ingenieros'
    as a single float.
    """
    if linguistic_component >= 5 and computing_component >= 5.0:
        final_score: float = (0.30 * linguistic_component) + (0.70 * computing_component)
        return round(final_score, 2)
    else:
        return 0.0

def algebra_final_score(ordinary):
    mark = input("put your ordinary mark here")
    mark = input("put your cuestionary percent mark here")
    type(mark) == type(float) or type(int)

def MD_final_score(ordinary_exam, participation):

    # get the grades
    ordinary_exam = float(input("Enter your ordinary exam grade: "))
    participation = float(input("Enter your participation grade: "))

    # calculates final score
    final = (ordinary_exam * 0.90) + (participation * 0.10)

    # return result
    return final
