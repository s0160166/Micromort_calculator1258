from math import *
m_kf = 1.10409
print(6270/5790)
print(7740/6270)
print(10140/7740)
print(14010/10140)
print(22230/14010)
print(31254/22230)
class Calculate():
    def __init__(self,age,credit,micromorts):
        self.age = age
        self.million = credit
        self.micrimorts = micromorts
    def calc(self):
        chance_alive = int(1)
        MICROMORTS = {a: 1.10409**(a-20) for a in range(20,100)}
        START_KF = 0.05
        print(MICROMORTS)
        m = self.micrimorts
        for item in MICROMORTS.items():
            if item[0] == self.age:
                m += item[1]
                for j in range(365):
                    chance_alive *= (1000000-m)/1000000
                m = self.micrimorts

        Chance = round((1-chance_alive)*100, 2)
        KF = Chance/START_KF
        return('Стоимость годового полиса:',self.million*0.0012*KF)

p1 = Calculate(20,1000000,2.76)
print(p1.calc())


age = int(input('Введите свой возраст:'))
million = int(1000000)
chance_alive = int(1)
'''
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
MICROMORTS = {a: 1.10409**(a-20) for a in range(20,100)}
#MICROMORTS = {a: round(1.0002734**(a),2) for a in range(1,365*80)}
print(MICROMORTS)

a = [x for x in MICROMORTS. values()]
print(sum(a))
micrimorts = float(input('Сколько микромортов получаешь ежедневно: '))
CREDITS = int(input('Остаток по кредиту: '))
START_KF = 0.05
m = micrimorts
for i in range(20,age):
    for item in MICROMORTS.items():
    #       if item[0] in range(age, credit_age+age):
        if item[0] == i:
            m += item[1]
            for j in range(365):
                chance_alive *= (million-m)/million
            m = micrimorts

    Chance = round((1-chance_alive)*100, 2)
    chance_alive = int(1)
    print('Вероятность умереть в',i,'лет при',m,'"бонусных" микромортах в день равняется',Chance,'%')

    KF = Chance/START_KF

    print('Повышающий коэффициент равен',KF)
    print('Стоимость годового полиса:',CREDITS*0.0012*KF)
