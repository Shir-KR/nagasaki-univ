#!/usr/bin/env python2.7

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

print "Start...."
#mc = minecraft.Minecraft.create("bes-master.cis.nagasaki-u.ac.jp")
mc = minecraft.Minecraft.create("cvcis01.progrape.jp")
pos = mc.player.getPos()

print mc.player.getPos()
print pos.x, pos.y, pos.z
#pos.x = 10
#pos.y = 10
#pos.z = 10

# genarate the wall
for i in range(0,40):
    for j in range(0,12):
        mc.setBlock(pos.x +i, pos.y +j, pos.z    , block.STONE)
        mc.setBlock(pos.x +i, pos.y +j, pos.z +20, block.STONE)

for j in range(0,12):
    for k in range (0,20):
        mc.setBlock(pos.x    , pos.y +j, pos.z +k, block.STONE)
        mc.setBlock(pos.x +40, pos.y +j, pos.z +k, block.STONE)

for j in range(0,12):
    mc.setBlock(pos.x +40, pos.y +j, pos.z +20, block.STONE)

for i in range(0,40):
    for k in range (0,20):
        mc.setBlock(pos.x +i, pos.y +j, pos.z +k, block.STONE)
        
