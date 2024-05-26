#https://www.codewars.com/kata/5803956ddb07c5c74200144e/train/python
def edad(age):
    if age > 14:
       min = int(age / 2 + 7)
       max = int((age - 7) * 2)
    else:
        min = int(age - 0.10 * age)
        max = int(age + 0.10 * age)
    return f'{min}-{max}'

print (edad(25))