import math
position = [0, 0, 90]         # Start slightly in air
velocity = [0, 30, 10]
gravity = -1.2
boost_force = 3
yaw = 0                        # Facing right (X-axis)
pitch = -0.3                   # Slightly tilted upward

for time_step in range(40):
    # Calculate forward direction from pitch and yaw
    forward = [
        math.cos(yaw) * math.cos(pitch),
        math.sin(yaw) * math.cos(pitch),
        math.sin(pitch)
    ]

    # Apply boost
    velocity[0] += forward[0] * boost_force
    velocity[1] += forward[1] * boost_force
    velocity[2] += forward[2] * boost_force

    # Apply gravity
    velocity[2] += gravity

    # Update position
    position[0] += velocity[0]
    position[1] += velocity[1]
    position[2] += velocity[2]

    # Stop at ground
    if position[2] < 0:
        position[2] = 0
        velocity[2] = 0

    print(f"Step {time_step}: Z = {round(position[2])}")
