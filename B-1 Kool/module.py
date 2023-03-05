def kool(opilased,puudumised):   
    while True:
        print('Toimingu valimine:')
        print('1. Hankige n parimat õpilast')
        print('2. Sorteerige loend truuduse järgi ning kuvage nimed ja jalutuskäigud')
        print('3. Kuva komisjonile saadetud õpilaste nimekiri')
        print('4. Rohkem kui 100-liikmeliste puudumistega õpilaste väljasaatmine')
        print('5. Välja')
        
        valik = input()
        
        if valik == '1':
            # Получаем n лучших учеников
            n = int(input('Sisestage parimate õpilaste arv: '))
            top = sorted(zip(opilased, puudumised), key=lambda x: x[1])[:n]
            print(f'Parimat {n} õpilased:')
            for opilased, puudumised in top:
                print(f'{opilased}: {puudumised} puudumised')
        elif valik == '2':
            # Сортируем список по прогулам и отображаем имена и прогулы
            sorted_list = sorted(zip(opilased, puudumised), key=lambda x: x[1])
            print('Sorteeritud nimekiri töölt puudumise järgi:')
            for opilased, puudumised in sorted_list:
                print(f'{opilased}: {puudumised} puudumised')
        elif valik == '3':
            # Отображаем список учеников, отправленных на комиссию
            print('Komisjonile saadetud õpilaste nimekiri:')
            for opilased, puudumised in zip(opilased, puudumised):
                if puudumised >= 20:
                    print(opilased)
        elif valik == '4':
            # Отчисляем учеников с прогулами больше 100
            for i in range(len(opilased)):
                if puudumised[i] > 100:
                    del opilased[i]
                    del puudumised[i]
                    print(opilased,puudumised)
        elif valik == '5':
            # Выходим из функции
            break
        else:
            print('Vale valik')

# sorted - сортирует 
# zip - соединяет списки
# del - удаляет из списка

