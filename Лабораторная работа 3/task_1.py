# TODO Напишите функцию для поиска индекса товара
def finding_index(list_, item):
    need_index = None
    for index in range(len(list_)):
        if list_[index] in item:
            need_index = index
            break
    return need_index





items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finding_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
