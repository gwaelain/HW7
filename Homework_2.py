regions_dalvostok = ['амурская область', 'еврейская автономная область', 'забайкальский край', 'камчатский край', 'магаданская область', 'приморский край', 'республика бурятия', 'республика саха', 'сахалинская область', 'хабаровский край', 'чукотский автономный округ']
base_rate = 10
regions = input('Ваш регион проживания :  ', ).lower()
if regions in regions_dalvostok:
      base_rate = 2
else:
    if int(input('Количество детей: ')) >= 3:
        base_rate -= 1
    if input('Являетесь ли Вы зарплатным клиентом?: ').lower() == 'да':
        base_rate -= 0.5
    if input('Застрахованы ли в нашем банке: ').lower() == 'да':
        base_rate -= 1.5
print('Ваша процентная ставка:',base_rate, 'процентов')



day = int(input("Введите день рождения: ").lower())
month = input("Введите месяц рождения ( январь, февраль, март и т.д): ").lower()

if month =='декабрь':
	astro_sign ='Стрелец' if (day < 22) else 'козерог'
elif month =='январь':
	astro_sign ='Козерог' if (day < 20) else 'водолей'
elif month =='февраль':
	astro_sign ='Водолей' if (day < 19) else 'рыбы'
elif month =='март':
	astro_sign ='Рыбы' if (day < 21) else 'овен'
elif month =='апрель':
	astro_sign ='Овен' if (day < 20) else 'телец'
elif month =='май':
	astro_sign ='Телец' if (day < 21) else 'близнецы'
elif month =='июнь':
	astro_sign ='Близнецы' if (day < 21) else 'рак'
elif month =='июль':
	astro_sign ='Рак' if (day < 23) else 'лев'
elif month =='август':
	astro_sign ='Лев' if (day < 23) else 'дева'
elif month =='сентябрь':
	astro_sign ='Дева' if (day < 23) else 'весы'
elif month =='октябрь':
	astro_sign ='Весы' if (day < 23) else 'скорпион'
elif month =='ноябрь':
	astro_sign ='Скорпион' if (day < 22) else 'стрелец'
print("Ваш знак зодиака :",astro_sign)
