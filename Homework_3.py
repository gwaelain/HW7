boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard' ]
girls = ['Kate', 'Lisa', 'Kira', 'Emma', 'Trisha']
if len(boys) != len(girls):
    print('Ни кого знакомить не будем!')
else:
    boys.sort()
    girls.sort()
    together = zip(boys, girls)
    print(f'Идеальные пары:')
    for a, b in together:
        print(f'{a} и {b}')


print('____________________________________')


person = int(input('Введите количество персон: '))
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]


for i in cook_book:
    print(f'\n{i[0].title()}:')
    for j in i[1]:
        print(f'{j[0]}, {j[1] * person}{j[2]}')
