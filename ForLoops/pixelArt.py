from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

blocks = [[35, 99, 35, 12, 35, 35, 55, 35],
          [9, 35, 4, 98, 56, 15, 24, 35],
          [35, 2, 9, 35, 23, 68, 35, 35],
          [11, 35, 35, 34, 69, 35, 53, 1]]
for row in reversed(blocks):
    for block in row:
        mc.setBlock(x, y, z, block)
        x += 1
    y += 1
    x = pos.x
