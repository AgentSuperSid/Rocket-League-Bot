 import math

#Car info

car_position=[0,0] #car_rotation,car_position are just arrays(or Lists as in python). To access each part indexing is used.
car_rotation=[0,math.radians(45),0] 
speed=200                     

#Ball setup

ball_position=[500,500] #wrt the origin

#Direction the car is facing
yaw=car_rotation[1] # [0] means x axis, [1] means y and [2] means z axis
pitch=car_rotation[0] # car_rotation = [roll, pitch, yaw]
roll=car_rotation[2]
car_facing=[math.cos(yaw),math.sin(yaw)] #car_facing is a unit vector.

# Yaw: North South West East direction or just left right on the flat ground. How much angle it does to the x axis while fully resting on this plane.
# Pitch: How much angle the car does(Or the nose of the car does) to the ground(or the XY plane). Or how much it is looking up.
# Roll: Barrel roll basically(Asphalt 8 reference). How much it has rotated that way taking the cars dirextion as the axis of rotation(Explaining in not so simple terms).

#Direction to ball
to_ball=[
         ball_position[0]-car_position[0], ball_position[1]-car_position[1] #This gives the position vector of the ball wrt the car
        ]

#Normalise to_ball
magnitude = math.sqrt(to_ball[0]**2 + to_ball[1]**2) # Just distance formula between the car and the ball.
to_ball_normalized = [to_ball[0]/magnitude, to_ball[1]/magnitude] # Unit vector. To only get the direction, you dont need the magnitude to know where to go.

#Dot & cross to get angle + side                  # a·b = |a||b|cosθ -> |a|=|b|=1         => a.b = cosθ 
                                                  # Also a.b = axbx + ayby. So thats what they did below
dot = car_facing[0]*to_ball_normalized[0] + car_facing[1]*to_ball_normalized[1] # For dot product visualization try the html program "Dot_product_components.html". 
                                                                                 # Dot product is more like the agreement of each components(X and Y) of the individual vectors.
angle = math.acos(dot) #in radians   # angle gives only the magnitude of how much side the ball is. It doesnt give which side it is.
side = car_facing[0]*to_ball_normalized[1]-car_facing[1]*to_ball_normalized[0] #This gives -ve if ball is in right and +ve if ball is in left. 0 means they are facing straight.
                                                                               # You can refer to similiar visualization as the dot product one. 

#steering

if angle<math.radians(5):
    steering="Straight"
elif side>0:
    steering="Left"
else:
    steering="Right"
    
#Move forward

car_position[0] = car_position[0] + car_facing[0]*speed #Here speed is just displacement with a fixed value. Each iteration the car dsplaces that much in the direction to which its multiplied.
car_position[1] = car_position[1] + car_facing[1]*speed

#Ouput
print("car_position", [round(p,2) for p in car_position])
print("Facing:", [round(f,2) for f in car_facing])
print("Steering:", steering)
