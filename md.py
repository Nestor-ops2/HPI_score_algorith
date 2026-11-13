def MD_final_score(ordinary_exam, participation):

    # get the grades
    ordinary_exam = float(input("Enter your ordinary exam grade: "))
    participation = float(input("Enter your participation grade: "))

    # calculates final score
    final = (ordinary_exam * 0.90) + (participation * 0.10)

    # return result
    return final