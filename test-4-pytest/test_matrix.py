import pytest

from broken_recommendations import Matrix


@pytest.fixture(name="matrix")
def matrix_fixture():
    return Matrix()


def test_pop_from_empty_matrix(matrix):
    with pytest.raises(IndexError) as err:
        matrix.pop()

    assert str(err.value) == ""


def test_add_none(matrix):
    with pytest.raises(ValueError) as err:
        matrix.add_item(None)

    assert str(err.value) == ""


@pytest.mark.parametrize(
    argnames="add_items, expected_matrix",
    argvalues=[
        ([1], "1 None\nNone None"),
        ([1, 2, 3, 4], "1 2 3\n4 None None\nNone None None"),
    ]
)
def test_add_item(matrix, add_items, expected_matrix):
    for item in add_items:
        matrix.add_item(item)

    assert str(matrix) == expected_matrix


@pytest.mark.parametrize(
    argnames="add_items, pop_count, expected_matrix",
    argvalues=[
        ([1], 1, "None"),
        ([1, 2, 3, 4], 1, "1 2 3\nNone None None\nNone None None"),
        ([1, 2, 3, 4], 2, "1 2\nNone None"),
    ],
    ids=[
        "pop with resize to zero size",
        "pop without resize",
        "pop with resize",
    ]
)
def test_pop_item(matrix, add_items, pop_count, expected_matrix):
    for item in add_items:
        matrix.add_item(item)

    for i in range(pop_count):
        assert matrix.pop() == add_items[-i - 1]

    assert str(matrix) == expected_matrix
