from world import europe
print(europe.greece)
# print(europe.spain)
import world
print(world.europe.norway)
import world.europe.spain
print(europe.spain)
from world.europe import norway

# print(world.africa.zimbabwe)

from world.africa import zimbabwe
print(world.africa.zimbabwe)


