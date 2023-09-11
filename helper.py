from dataclasses import dataclass
import datetime
import operator

todos = []


@dataclass
class Todo:
    title: str
    date: datetime = "2024-01-01"
    isCompleted: bool = False


def add(title, date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")

    title = title.replace("b", "bbb").replace("B", "Bbb")
    todos.append(Todo(title, date))  # daten gespeichert
    todos.sort(key=operator.attrgetter("date"))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted


def delete():
    todos.clear()
