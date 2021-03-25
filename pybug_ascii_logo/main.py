from typing import List, Tuple

# from colorama import Fore, Style
# from ascii_canvas import canvas
#
#
# canvas = canvas.Canvas()


def gen_circle_points(radius: int) -> List[Tuple[int, int]]:
    results = list()

    x = 0
    y = radius
    delta = 2 * (1 - radius)
    lim = 0

    while True:
        results.append((x, y))
        print(x, y)

        if y <= lim:
            break

        elif delta < 0:
            delta = (2 * delta) + (2 * y) - 1

            if delta <= 0:
                x -= 1
                delta += 2 * x + 1
                continue

        elif delta > 0:
            delta = (2 * delta) - (2 * x) - 1

            if delta > 0:
                y -= 1
                delta = delta - (2 * y) + 1
                continue

        x += 1
        y -= 1
        delta += (2 * x) + (2 * y) + 2
    return results


print(gen_circle_points(5))
