# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:12:31 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


x,y,z = mc.player.getTilePos()

color = random.randrange(0,16)
mc.setBlocks(x+28,y-1,z+28,
            x-28,y-1,z-28,95,color)