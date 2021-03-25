from typing import Set, Tuple, Optional
import math

from colorama import Fore, Style
from ascii_canvas import canvas, item


canvas = canvas.Canvas()


def gen_circle_points(
    radius: int,
    n: Optional[int] = 1000,
    terminal_resize: Optional[float] = 1
) -> Set[Tuple[int, int]]:
    """ VS Code resize: 5 / 12 """

    result = set()

    for x in range(0, n + 1):
        point = 2 * math.pi / n * x
        result.add(
            (
                round(math.cos(point) * radius) + radius,
                round(math.sin(point) * radius * terminal_resize) + radius
            )
        )

    return result


points = gen_circle_points(50, terminal_resize=8 / 16)
print(points)
for i in points:
    canvas.add_item(item.Item("@", i))

print(canvas.render())
input()
