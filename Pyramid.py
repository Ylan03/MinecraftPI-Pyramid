# Import standard libraries
import time
import math

# Import specific Minecraft libraries
import mcpi.minecraft as minecraft
import mcpi.block as block

# Block definitions
# See http://www.raspberrypi-spy.co.uk/2014/09/raspberry-pi-minecraft-block-id-number-reference/ for more blocks
AIR       = 0
DIRT      = 3
SAND      = 12
SANDSTONE = 24
GOLD      = 41

mc = minecraft.Minecraft.create()

def CreatePyramid(posx, posy, posz, width, mybase, mywalls, mytopblock):
    mc.postToChat("creating")
    print(width)
    if width%2==0:
        width=width+1

    print(width)
    #height = (width+1)/2
    height = int((width+1)/2)
    print(height)
    halfsize = int(math.floor(width/2))
    print ("player : {} {} {}".format(posx,posy,posz))
    print ("size : {} H : {} Halfsize : {}".format(width,height,halfsize))

    print ("create base")
    mc.setBlocks(posx-halfsize-2,posy-2,posz-halfsize-2,posx+halfsize+2,posy-2,posz+halfsize+2,DIRT)
    mc.setBlocks(posx-halfsize-2,posy-1,posz-halfsize-2,posx+halfsize+2,posy-1,posz+halfsize+2,mybase,1)
    #mc.setBlocks(posx-halfsize-2,posy-2,posy-halfsize-2,posx+halfsize+2,posy-2,posz+halfsize+2,DIRT)
    #mc.setBlocks(posx-halfsize-2,posy-1,posy-halfsize-2,posx+halfsize+2,posy-1,posz+halfsize+2,mybase)

    print ("create pyramid")
    for y in range (posy,posy+height):
        mc.setBlocks(posx-halfsize,y,posz-halfsize,posx+halfsize,y,posz+halfsize,mywalls)
        #mc.setBlocks(posx-halfsize,y,posy-halfsize,posx+halfsize+2,posy,y,posz+halfsize,mywalls)
        halfsize=halfsize-1

    print ("set top block")
    mc.setBlock(posx,posy+height-1,posz,mytopblock)
    print ("player on top")
    mc.player.setPos(posx,posy+height,posz)

# Get player position
mc.player.setPos(0,1,0)
playerPos = mc.player.getPos()
playerPos = minecraft.Vec3(int(playerPos.x),int(playerPos.y),int(playerPos.z))

# Set lower half of world to Sandstone
mc.setBlocks(-128,0,-128,128,-128,128,SANDSTONE)

# Set upper half to air
mc.setBlocks(-128,1,-128,128,128,128,AIR)  

# Create Pyramids
CreatePyramid(0,1,0,51,24,24,41)

CreatePyramid(-40,1,40,21,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(-40,1,-40,21,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(40,1,40,21,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(40,1,-40,21,SANDSTONE,SANDSTONE,SANDSTONE)

CreatePyramid(0,1,45,31,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(0,1,-45,31,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(45,1,0,31,SANDSTONE,SANDSTONE,SANDSTONE)
CreatePyramid(-45,1,0,31,SANDSTONE,SANDSTONE,SANDSTONE)
