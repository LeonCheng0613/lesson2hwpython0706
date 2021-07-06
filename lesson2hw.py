math_score=float(input ('what is the math score?'))
english_score=float(input('what is the english score?'))
if math_score>=90 and english_score>=90:
    print('you get a gift!')
elif math_score<60 and english_score<60:
    print('you get a punishment!')
elif math_score<60 or english_score<60:
    print('gogogo!')