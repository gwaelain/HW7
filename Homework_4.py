geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
#result = [rus for rus in geo_logs if 'Россия' in list(rus.values())[0]]
#print(result)
result = [geo_log for geo_log in geo_logs if "Россия" in next(iter(geo_log.values()))]
print(result)







print('________________________________________________________________________')

ids = {"user1": (213, 213, 213, 15, 213),
"user2": (54, 54, 119, 119, 119),
"user3": (213, 98, 98, 35)}
set_of_ids = []
for value in ids.values():
    set_of_ids.extend(value)
    print("Уникальные гео-id пользователей : ", set(set_of_ids))




print('________________________________________________________________________')

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

a_dict = dict()

for query in queries:
    query_len = len(query.split(' '))
    if query_len in a_dict:
        a_dict[query_len] += 1
    else:
        a_dict[query_len] = 1

print(a_dict)

queries_count = len(queries)
for query_len, query_count in sorted(a_dict.items()):
    print('Поисковых запросов, содержащих %d слов(а): %.2f%%' % (query_len, 100 * query_count / queries_count))



print('________________________________________________________________________')


stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max_val = max(stats.items())

print(max_val[0])

print('________________________________________________________________________')


x = ['2018-01-01', 'yandex', 'cpc', 100]

y = {x[-2]: x[-1]}
for i in x[:-2][::-1]:
    y = {i: y}
print(y)


print('________________________________________________________________________')


