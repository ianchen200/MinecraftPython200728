# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:36:09 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

X,Y,Z = mc.player.getTilePos()

mc.setBlock(X+1,Y,Z,1,2)
mc.setBlock(X-1,Y,Z,1,2)
mc.setBlock(X,Y,Z+1,1,2)
mc.setBlock(X,Y,Z-1,1,2)
mc.setBlock(X+1,Y,Z+1,1,2)
mc.setBlock(X-1,Y,Z+1,1,2)
mc.setBlock(X+1,Y,Z-1,1,2)
mc.setBlock(X-1,Y,Z-1,1,2)