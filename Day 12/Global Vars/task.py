# Modifying Global Scope

enemies = 1
orit = [1,2]

def increase_enemies(orit1):
    global enemies
    enemies += 1
    orit1 = 3
    print(f"enemies inside function: {enemies}")


increase_enemies(orit)
print(f"enemies outside function: {enemies}")
print(f"enemies outside function: {orit}")


