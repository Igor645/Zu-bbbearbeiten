from dataclasses import dataclass
import datetime

items = []


@dataclass
class Item:
    text: str
    date: datetime
    isCompleted: bool = False


def add(text, date):
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    items.append(Item(text, date))
    items.sort(key=lambda x: x.date)

def get_all():
    return items


def get(index):
    return items[index]


def update(index):
    items[index].isCompleted = not items[index].isCompleted

def get_csv():
    csv_data = []

    for item in items:
        csv_row = f"{item.text},{item.date},{item.isCompleted}"
        csv_data.append(csv_row)

    return "\n".join(csv_data)
