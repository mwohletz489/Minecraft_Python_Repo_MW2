from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import time

time.sleep(60)

blockHits = mc.pollBlockHits()

blockHitsLength = len(blockHits)
mc.postToChat("Your score is" + str(blockHitsLength))
