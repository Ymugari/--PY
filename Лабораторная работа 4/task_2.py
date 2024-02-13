# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r") as file_input:
        data = [i for i in csv.DictReader(file_input)]
    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as file_output:
        json.dump(data, file_output, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, "r") as output_f:
        for line in output_f:
            print(line, end="")
