import json

def task():
    # Открываю файл
    with open('input.json', 'r') as f:
        data = json.load(f)

    total = 0
    for item in data:
        score = item["score"]
        weight = item["weight"]
        total = total + (score * weight)

    result = round(total, 3)
    return result

print(task())