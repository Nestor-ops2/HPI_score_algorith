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

    print(f"Theory: {theory}, Lab: {lab}, Final: {final}")
    return final