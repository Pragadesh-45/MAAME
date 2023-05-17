def get_mbti_type(answer1, answer2, answer3, answer4, answer5, answer6,
                  answer7, answer8, answer9, answer10):
    """
    Given the answers to the 10 questions, return the corresponding MBTI type.
    """
    a,b,c,d='','','',''
    extrovert = introvert = sensing = intuitive = thinking = feeling = \
        judging = perceiving = 0

    # Calculate the values for each dimension
    if answer1 <= 2:
        extrovert += 1
    else:
        introvert += 1

    if answer2 <= 2:
        sensing += 1
    else:
        intuitive += 1

    if answer3 <= 2:
        thinking += 1
    else:
        feeling += 1

    if answer4 <= 2:
        judging += 1
    else:
        perceiving += 1

    if answer5 <= 2:
        extrovert += 1
    else:
        introvert += 1

    if answer6 <= 2:
        sensing += 1
    else:
        intuitive += 1

    if answer7 <= 2:
        thinking += 1
    else:
        feeling += 1

    if answer8 <= 2:
        judging += 1
    else:
        perceiving += 1

    if answer9 <= 2:
        extrovert += 1
    else:
        introvert += 1

    if answer10 <= 2:
        sensing += 1
    else:
        intuitive += 1

    # Determine the MBTI type
    # mbti_type = ""
    if extrovert > introvert:
        a += "E"
    else:
        a += "I"

    if sensing > intuitive:
        b += "S"
    else:
        b += "N"

    if thinking > feeling:
        c += "T"
    else:
        c += "F"

    if judging > perceiving:
        d += "J"
    else:
        d += "P"

    return a,b,c,d
	  
