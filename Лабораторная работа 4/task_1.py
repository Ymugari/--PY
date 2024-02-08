# TODO решите задачу
import json


def task() -> float:
    with open("input.json", "r") as file:
        data = json.load(file)
    summa = 0
    for dict_ in data:
        weight_score = 1
        weight_score = dict_.get("score") * dict_.get("weight")
        summa += weight_score
    return round(summa, 3)


print(task())
