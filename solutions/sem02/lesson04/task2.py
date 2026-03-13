import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:

    if threshold < 1:
        raise ValueError("threshold must be at least 1")

    pixels = image.ravel()
    pixels_count = np.zeros(256, dtype=int)

    for value in pixels:
        pixels_count[value] += 1

    most_popular_count = 0
    most_popular_color = 0

    for c in range(256):

        left = max(0, c - threshold + 1)
        right = min(255, c + threshold - 1)

        current_color_count = np.sum(pixels_count[left:right + 1])

        if most_popular_count > most_popular_count:
            most_popular_count = current_color_count
            most_popular_color = np.uint8(c)

    percent = (most_popular_count / pixels.size) * 100.0

    return most_popular_color, percent
