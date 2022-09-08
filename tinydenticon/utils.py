import webcolors
from Cryptodome.Hash import SHA512


def scale_matrix_1d(
    matrix: list[any], matrix_size: int = 3, multiplier: int = 2
) -> list:
    """Scale a 1-dimensional (flattened) matrix.

    :param matrix: source matrix
    :type matrix: list[any]

    :param matrix_size: initial matrix size
    :type matrix_size: int

    :param multiplier: scale multiplier
    :type multiplier: int

    :return: scaled matrix

    Source:
    ```
    [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]
    ```

    Scaled x2:
    ```
        [
            1, 1, 2, 2, 3, 3,
            1, 1, 2, 2, 3, 3,
            4, 4, 5, 5, 6, 6,
            4, 4, 5, 5, 6, 6,
            7, 7, 8, 8, 9, 9,
            7, 7, 8, 8, 9, 9,
        ]
    ```
    """
    result = []
    row = []

    for idx, i in enumerate(matrix):
        row.extend([i] * multiplier)

        if (idx + 1) % matrix_size == 0:
            result.extend(row * multiplier)
            row = []

    return result


def saturate(value):
    return max(0.0, min(1.0, value))


def hue_to_rgb(hue):
    r = abs(hue * 6.0 - 3.0) - 1.0
    g = 2.0 - abs(hue * 6.0 - 2.0)
    b = 2.0 - abs(hue * 6.0 - 4.0)
    return saturate(r), saturate(g), saturate(b)


def rgb_percent_to_rgb(rgb_percent: tuple[str]) -> tuple[float]:
    return webcolors.rgb_percent_to_rgb(["%i%%" % (p * 100) for p in rgb_percent])


def hsl_to_rgb_percent(hue, saturation, lightness):
    r, g, b = hue_to_rgb(hue)
    c = (1.0 - abs(2.0 * lightness - 1.0)) * saturation
    r = (r - 0.5) * c + lightness
    g = (g - 0.5) * c + lightness
    b = (b - 0.5) * c + lightness
    return r, g, b


def hsl_to_rgb(hue, saturation, lightness):
    return rgb_percent_to_rgb(hsl_to_rgb_percent(hue, saturation, lightness))


def sha512hash(data: bytes, rounds: int = 1):
    """SHA-512 hash with custom rounds amount.

    :param data: data to hash
    :type data: bytes

    :param rounds: rounds amount
    :type rounds: int

    :return: SHA512Hash instance
    """
    sha = SHA512.new(data)
    for i in range(rounds - 1):
        sha = SHA512.new(sha.digest())
    return sha
