"""Dubugger Example."""

y: int = 0
while y < 2:
    x: int = 0
    while x < 2:
        print(f"({x}, {y})")
        x += 1
    y += 1
print("The end!")
    