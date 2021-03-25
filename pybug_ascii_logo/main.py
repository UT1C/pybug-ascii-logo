from typing import Set, Tuple, List, Optional
import itertools
import math

from colorama import Fore, Style
from ascii_canvas import canvas, item


canvas = canvas.Canvas()


def gen_circle_points(
    radius: int,
    n: Optional[int] = 10000
) -> Set[Tuple[int, int]]:
    result = set()

    for x in range(0, n + 1):
        point = 2 * math.pi / n * x
        result.add(
            (
                int(math.cos(point) * radius) + radius,
                int(math.sin(point) * radius * (24 / 48)) + radius
            )
        )

    return result


points = gen_circle_points(50)
print(points)
for i in points:
    canvas.add_item(item.Item(f"@", i))

print(canvas.render())
