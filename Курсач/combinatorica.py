from math import *


'''
Микроморт является всего лишь единец риска, поэтому принято решение не использовать
для его рассчета события, несущие хронический характер(например алкоголь и курение),
нужно найти приличную выборку рисков другого характера(например езда на автомобиле по 2
часа в день, опасные профессии, хобби и тд)


Альфастрахования тип полиса жизнь остаток по ипотеке 3000000
20 лет муж - 5790
20 лет жен - 3570
25 лет муж - 6270
25 лет жен - 4350
30 лет муж - 6270
30 лет жен - 5100
35 лет муж - 7740
35 лет жен - 6810
40 лет муж - 10140
40 лет жен - 7950
45 лет муж - 14010
45 лет жен - 11910
50 лет муж - 22230
50 лет жен - 18150
55 лет муж - 31254
55 лет жен - 26946


'''
RISK = {
'age': int(input('Введите свой возраст:')),
'gender': input('Введите свой пол:'),
'smoke': int(input('Сколько сигарет в день в среднем курите?:'))/1.4,
'car_sity': float(input('Сколько часов в день ездите в автомобиле по городу?:'))*50/370,
'car_trassa': float(input('Сколько часов в день ездите в автомобиле за городом?:'))*100/370,
'moto_city': int(input('Сколько часов в день за рулем мотоцикла по городу?:'))*70/10,
'moto_trassa': int(input('Сколько часов в день за рулем мотоцикла за городом?:'))*140/10,
'velo': int(input('Сколько часов в среднем проезжаете на велосипеде в день?:'))*15/16,
'peshehod': int(input('Сколько часов в среднем проходите пешкомв день?:'))*5/27,
}
print(RISK)
sum_rick = 0
risk = list(RISK.values())
for value in risk:
    if isinstance(value, float):
        sum_rick += value
print(sum_rick)


age = RISK['age']

credit_age = int(input('Введите на какой срок запрашивают кредит:'))
million = int(1000000)
chance_alive = int(1)

MICROMORTS = {a: 1.10409**(a-20) for a in range(20,100)}
#MICROMORTS = {a: round(1.0002734**(a),2) for a in range(1,365*80)}
print(MICROMORTS)

a = [x for x in MICROMORTS. values()]
print(sum(a))

for i in range(1,250):
    a = i+sum_rick
    print('sdfdsfsfdsfdsfdsfsdfds',a)
    for item in MICROMORTS.items():
#        if item[0] in range(age, credit_age+age):
         if item[0] in range(age, credit_age+age):
            a += item[1]
            for j in range(365):
                chance_alive *= (million-a)/million
            print(a)
         a = i+sum_rick
    print('Вероятность выплатить кредит на',credit_age,'лет при',i,'микромортах в день равняется',round(chance_alive*100, 2),'%')
    chance_alive = int(1)
