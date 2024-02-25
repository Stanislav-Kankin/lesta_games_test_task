"""
На языке Python написать минимум по 2 класса реализовывающих
циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.
Оценивается:
Полнота и качество реализации
Оформление кода
Наличие сравнения и пояснения по быстродействию
"""


class CircularBuffer1:

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def is_empty(self):
        # Возращвет True если пусто, False если нет
        return len(self.buffer) == 0

    def is_full(self):
        # Возращвет True если буфер полон, False если нет
        return len(self.buffer) == self.capacity

    def enqueue(self, value):
        # Ставим данные в очередь
        if self.is_full():
            # удаление самого старого элемента при переполнении
            self.buffer.pop(0)
        self.buffer.append(value)

    def dequeue(self):
        # Убираем данные из очереди(первый элемент)
        if self.is_empty():
            return None
        return self.buffer.pop(0)


class CircularBuffer2:

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, value):
        if self.is_full():
            # переход к следующему индексу по модулю
            self.head = (self.head + 1) % self.capacity
        self.buffer[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self.buffer[self.head]
        self.buffer[self.head] = None  # заменяем значение на None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value


if __name__ == "__main__":
    print("Первый класс тест:")
    test_buffer1 = CircularBuffer1(5)
    test_buffer1.enqueue(10)
    test_buffer1.enqueue(20)
    print(test_buffer1.is_empty())
    print(test_buffer1.is_full())
    print(test_buffer1.buffer)
    test_buffer1.enqueue(11)
    test_buffer1.enqueue(23)
    test_buffer1.enqueue(555)
    test_buffer1.enqueue(999)
    test_buffer1.enqueue(17)
    test_buffer1.enqueue(29)
    test_buffer1.enqueue(1)
    test_buffer1.enqueue(0)
    print(test_buffer1.is_empty())
    print(test_buffer1.is_full())
    print(test_buffer1.buffer)
    test_buffer1.dequeue()
    test_buffer1.dequeue()
    print(test_buffer1.buffer)
    print("Второй класс тест:")
    test_buffer2 = CircularBuffer2(5)
    test_buffer2.enqueue(1)
    test_buffer2.enqueue(2)
    test_buffer2.enqueue(3)
    print(test_buffer2.buffer)
    test_buffer2.enqueue(4)
    test_buffer2.enqueue(5)
    test_buffer2.enqueue(6)
    print(test_buffer2.buffer)
    test_buffer2.dequeue()
    test_buffer2.dequeue()
    test_buffer2.dequeue()
    test_buffer2.dequeue()
    print(test_buffer2.buffer)
    test_buffer2.enqueue(4)
    test_buffer2.enqueue(5)
    test_buffer2.enqueue(6)
    print(test_buffer2.buffer)

"""
CircularBuffer1:
Плюсы:
1 - Простота: использовад встроенный питоновский список
что упрощает реализацию функциональности циклического буфера.
2 - Читаемость: В целом просто и быстро читается, ясно что делает класс.

Минусы:
1 - УДмаю производительность: При переполнении буфера,
удаление самого старого элемента осуществляется с помощью pop(0),
что требует перемещения всех остальных элементов в списке.
2 - Временная сложность операций: Вставка в конец списка
и удаление из начала списка имеют
временную сложность O(n), то есть линейную. Сложность зависит
от размера списка

CircularBuffer2:
Плюсы:
1 - Эффективность: Реализация с использованием массива
позволяет эффективно управлять памятью и достигать
постоянной временной сложности операций.
2 - Производительность: Побитовые операции % и сложение по
модулю позволяют быстро переходить к следующим индексам массива.
Минусы:
1 - Более сложная реализация: Ручное управление индексами и
обработка пересечения границ массива требуют дополнительных усилий
и могут быть сложными для понимания и сопровождения.
2 -Ограничение типа данных: Из-за необходимости использования фиксированного
массива, реализация ограничивается типами данных, переданными
при инициализации.

  """
