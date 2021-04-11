from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    return (x + y) == z

def check_fibonacci(data: Sequence[int]) -> bool:

    result = False
    if not data: 
        result = False
    elif data in ([0], [0, 1], [0, 1, 1]):
        result = True
    elif len(data) > 3:
        a, b, c = data[0], data[1], data[2]

        while data:
            print(a, b, c)
            if not _check_window(a, b, c):
                result = False
                break
            if len(data) > 3:
                data = data[1:]
                a, b, c = b, c, data[2]
            else:
                result = True
                break
        #else:    
        #    result = True

    return result
