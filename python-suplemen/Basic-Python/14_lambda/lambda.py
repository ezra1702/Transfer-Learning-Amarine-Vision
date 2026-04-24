"""
    Lambda
        1. Lambda adalah fungsi anonim yang digunakan untuk membuat fungsi yang sederhana.
        2. Lambda juga disebut sebagai anonymous function karena tanpa nama.
        3. Lambda biasanya digunakan untuk membuat fungsi yang sederhana dan tidak terlalu kompleks.
        4. Lambda menerima lebih dari satu argumen.
"""

# Satu argumen 
double = lambda x: x * 2
print(double(5))  # Output: 10

# Dua argumen
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Tiga argumen
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # Output: 24


# unlimited argument **kwargs
avg_score_kwargs = lambda **kwargs: sum(kwargs.values()) / len(kwargs)
scores = {"Math": 80, "Science": 85, "English": 90}
print(avg_score_kwargs(**scores))
print(avg_score_kwargs(biology=80, chemistry=85, physics=90))

# unlimited arguments **args

