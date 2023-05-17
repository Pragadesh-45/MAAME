def get_mbti_type(answers):
    # Calculate scores for each of the four MBTI dimensions
    extraversion = answers[0] + answers[3] + answers[5] + answers[9]
    introversion = answers[1] + answers[2] + answers[4] + answers[6]
    sensing = answers[0] + answers[1] + answers[7] + answers[9]
    intuition = answers[2] + answers[3] + answers[4] + answers[6]
    thinking = answers[1] + answers[3] + answers[6] + answers[8]
    feeling = answers[0] + answers[2] + answers[5] + answers[7]
    judging = answers[4] + answers[5] + answers[8] + answers[9]
    perceiving = answers[0] + answers[2] + answers[3] + answers[6]
    
    # Determine the dominant traits for each dimension
    extraverted = extraversion > introversion
    sensing_dominant = sensing > intuition
    thinking_dominant = thinking > feeling
    judging_dominant = judging > perceiving
    
    # Map the dominant traits to the corresponding MBTI type
    mbti_type = ""
    if extraverted:
        mbti_type += "E"
    else:
        mbti_type += "I"
    if sensing_dominant:
        mbti_type += "S"
    else:
        mbti_type += "N"
    if thinking_dominant:
        mbti_type += "T"
    else:
        mbti_type += "F"
    if judging_dominant:
        mbti_type += "J"
    else:
        mbti_type += "P"
    
    return mbti_type
