'''Напишите программу, в которой считается, сколько задач выполнил Максим за день (8 часов).
Если он хоть раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».'''

i = 0
total_day = 0

while i <  8:
        task = int(input('Сколько задач решит Максим? '))
        phone = int(input('Звонит жена. Взять трубку?'))
        total_day += task
        i+=1
        if phone == 1:
            total_phone = 'Нужно зайти в магазин'
        else:
            total_phone = ''


print(total_day)
print(total_phone)
