'''
 Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
 Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
 Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''


x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))
s = x + y
p = x * y
if p == s:
    print("True")
else:
    print("False")