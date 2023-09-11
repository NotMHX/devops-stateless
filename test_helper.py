import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    title = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(title, date)

    # Then: The most recently added to-do should have a date
    item = helper.todos[-1]
    assert isinstance(item.date, datetime.date)


def test_sort():
    # Given: I have several to-dos with dates
    todos = [
        ("Universum debuggen", "2023-09-06"),
        ("Sinn des Lebens entdecken", "2023-09-01"),
        ("Superheld werden", "2023-10-25"),
        ("Netto null", "2050-01-01"),
    ]

    # When: I add the items
    for todo in todos:
        helper.add(todo[0], todo[1])

    # Then: They should be sorted by date
    for i in range(len(helper.todos) - 1):
        assert helper.todos[i].date < helper.todos[i + 1].date
