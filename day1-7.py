# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:15:24 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
blockid = int(input("你要放的方塊ID:"))
mc.setBlock(x+1,y,z,blockid )