"""
Игра «Изгиб Питона» (Змейка).

Реализация классической игры «Змейка» на Python с использованием Pygame.
"""

from random import randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Начальная позиция объектов (центр экрана):
START_POSITION = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Глубина цвета экрана:
COLOR_DEPTH = 32

# ... остальные константы ...


class GameObject:
    """Базовый класс для всех игровых объектов."""

    def __init__(self) -> None:
        """Инициализирует объект, задавая его начальную позицию."""
        self.position = START_POSITION
        self.body_color = None

    def draw(self) -> None:
        """Отрисовывает объект (переопределяется наследниками)."""
        raise NotImplementedError(
            'Метод draw() должен быть переопределён в наследнике.'
        )


class Apple(GameObject):
    """Класс, описывающий яблоко."""

    def __init__(self) -> None:
        """Инициализирует яблоко, задавая цвет и случайную позицию."""
        super().__init__()
        self.body_color = APPLE_COLOR
        self.randomize_position()

    def randomize_position(self) -> None:
        """Устанавливает случайное положение яблока на игровом поле."""
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )

    def draw(self) -> None:
        """Отрисовывает яблоко на игровой поверхности."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс, описывающий змейку и её поведение."""

    def __init__(self) -> None:
        """Инициализирует змейку с начальными параметрами."""
        super().__init__()
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = SNAKE_COLOR
        self.last = None

    # ... остальные методы без изменений ...

    def reset(self) -> None:
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [START_POSITION]
        self.direction = RIGHT
        self.next_direction = None