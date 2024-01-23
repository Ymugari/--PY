users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
statistics = {
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
statistics["Общее количество"] = len(users)
users = set(users)
statistics["Уникальные посещения"] = len(users)
print(statistics)