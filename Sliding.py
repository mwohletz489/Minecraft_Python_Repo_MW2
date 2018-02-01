from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

x, y, z = 10, 11, 12

mc.player.getPos(x, y, z)


while True:
    x += random.uniform(-0.2, 0.2)
    z += random.uniform(-12.0, 12.0)
    y = mc.getHeight(x, z)

    mc.player.setPos(x, y, z)
    time.sleep(0.1)
