from dataclasses import dataclass
from datetime import datetime

todos = []

@dataclass
class Todo:
    title: str
    isCompleted: bool = False
    date: datetime = datetime(2023, 1, 1)
    


def add(title, date=None):
    title = title.replace('b', 'bbb').replace('B', 'Bbb') #hier wird bbb-siert lmao
    date = datetime.strptime(date, '%Y-%m-%d')
    todos.append(Todo(title, date)) # daten gespeichert


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted

def delete():
    todos.clear()