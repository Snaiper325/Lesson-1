print("Привет, мир!")

age = input("Введите ваше любимое время года:")
print("И мой любимое время года ",age)
number = int(input("Введите число:"))
print("Ваше число в квадрате:",number*number)
num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))
print("Сумма чисел:",num2+num1)
print("Произведение чисел:",num2*num1)
print("Разность чисел:",num1-num2)
if num2 != 0:
    print("Деление чисел:",num1/num2)
    print("Деление произошло успешно")
else:
    print("Деление на ноль невозможно")

i = int(input("Введите число 1-12: "))
if i == 1:
    print("Январь")
elif i == 2:
    print("Февраль")
elif i == 3:
    print("Март")
elif i == 4:
    print("Апрель")
elif i == 5:
    print("Май")
elif i == 6:
    print("Июнь")
elif i == 7:
    print("Июль")
elif i == 8:
    print("Август")
elif i == 9:
    print("Сентябрь")
elif i == 10:
    print("Октябрь")
elif i == 11:
    print("Ноябрь")
elif i == 12:
    print("Декабрь")

#Это комментарий

Str1 = "Саша "
Str2 = "Колодижанский"
Str3 = Str1 + Str2
print(Str3)

time = int(input("Введите текущее время: "));
if time<25 and time>-1:
    if time>22 or time<6:
        print("Надо спать")
    else:
        print("Занимайся другими делами")
else:
    print("В сутках нету ",time)

p = int(input("Любиш ли ты любиш програмировать (1(да)/0(нет))"))
if p == 1:
    print("Привет дружище!")
    l = int(input("Точно ты любиш програмировать  (1(да)/0(нет))"))
    if l == 1:
        print("Рад знакомству")
    if l == 0:
        print("Уйди от сюда лгун! Пока тебя не пере программировал")
else:
    print("Давай досвидание!")
    
print("Пока")
