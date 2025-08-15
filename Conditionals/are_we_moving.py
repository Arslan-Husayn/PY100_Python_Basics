speed = 0
acceleration = 5
braking_force = 1
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

is_moving2 = braking_force < acceleration and speed > 0 or acceleration > 0

print(is_moving2)