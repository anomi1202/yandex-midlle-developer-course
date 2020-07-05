from typing import Optional


class Matrix:
    """
    Код нашего коллеги аналитика
    Очень медленный и тяжелый для восприятия. Ваша задача сделать его быстрее и проще для понимания.
    """
    def __init__(self):
        self._matrix = []
        self._matrix_size = 1

    def add_item(self, element: Optional):
        """
        Добавляем новый элемент в матрицу.
        Если элемент не умещается в (size - 1) ** 2, то расширить матрицу.
        """
        if element is None:
            raise ValueError()

        if len(self._matrix) >= (self._matrix_size - 1) ** 2:
            self._matrix_size += 1

        self._matrix.append(element)

    def pop(self):
        """
        Удалить последний значащий элемент из массива.
        Если значащих элементов меньше (size - 1) * (size - 2) уменьшить матрицу.
        """

        if len(self._matrix) - 1 < 0:
            raise IndexError()

        value = self._matrix.pop()

        if len(self._matrix) <= (self._matrix_size - 1) * (self._matrix_size - 2):
            self._matrix_size -= 1

        return value

    def __str__(self):
        """
        Метод должен выводить матрицу в виде:
        1 2 3\nNone None None\nNone None None
        То есть между элементами строки должны быть пробелы, а строки отделены \n
        """

        matrix = self._matrix + [None] * (self._matrix_size ** 2 - len(self._matrix))

        result = []
        for i in range(self._matrix_size):
            slice = matrix[i * self._matrix_size: (i + 1) * self._matrix_size]
            result.append(' '.join(map(str, slice)))

        return '\n'.join(result)


if __name__ == "__main__":
    m = Matrix()
    n = 10

    for i in range(n):
        m.add_item(i + 1)
    print(m)

    for i in range(n):
        assert m.pop() == n - i
    print(m)
