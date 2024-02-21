import random

def generate_random_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        # Generate a random color in hexadecimal format
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors