import json
import io
from collections import Counter

#стаж вождения
def driving_expirience(name_bd):
    dr_ex_list = []
    try:
        with io.open(name_bd, encoding='utf-8') as read_file:
            data = json.load(read_file)
            for i in range(len(data['features'])):
                if len(data['features'][i]['properties']['vehicles']) >= 2:
                    for j in range(len(data['features'][i]['properties']['vehicles'])):
                        if len(data['features'][i]['properties']['vehicles'][j]['participants']) >= 2:
                            for k in range(len(data['features'][i]['properties']['vehicles']['participants'])):
                                dr_ex_list.append(data['features'][i]['properties']['vehicles'][j]['participants'][k]['years_of_driving_experience'])
                        else:
                            dr_ex_list.append(data['features'][i]['properties']['vehicles'][j]['participants'][0]['years_of_driving_experience'])
                else:
                    dr_ex_list.append(data['features'][i]['properties']['vehicles'][0]['participants'][0]['years_of_driving_experience'])

    except Exception as ex:
        print(ex)

    finally:
        counter = Counter(dr_ex_list)
        print(counter)

# Выбираем цвет ТС
# в функцию передаем аргумент - файл .json
def color_of_vehicle(name_bd):
    # пустой список для хранения цветов ТС
    co_of_veh = []

    try:
        # открываем и читаем файл
        with io.open(name_bd, encoding='utf-8') as read_file:
            # получаем весь файл в переменную read_file
            # форматируем его в .json и присваеваем переменой data
            data = json.load(read_file)
            # Сколько элементов в файле и словаре
            print(f"В файле {name_bd} находится {len(data['features'])} элементов")
            # Выводим N элемент из 9089
            print(data['features'][478])
            # с помощью цикла проходимся по файлу
            for i in range(len(data['features'])):
                # если количество ТС больше 2, то запускаем цикл
                if len(data['features'][i]['properties']['vehicles']) >= 2:
                    # цикл для всех ТС
                    for j in range(len(data['features'][i]['properties']['vehicles'])):
                        # добавление цвета в список
                        co_of_veh.append(data['features'][i]['properties']['vehicles'][j]['color'])
                elif len(data['features'][i]['properties']['vehicles']) == 0:
                    co_of_veh.append("нет ТС")
                else:
                    co_of_veh.append(data['features'][i]['properties']['vehicles'][0]['color'])
    except Exception as ex:
        print(ex)

    finally:
        counter = Counter(co_of_veh)
        print(counter)










name_object = "smolenskaia-oblast.json"
driving_expirience(name_object)
color_of_vehicle(name_object)