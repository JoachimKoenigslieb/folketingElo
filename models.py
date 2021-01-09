#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:57:40 2021

@author: joachim
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, BigInteger, String, Float, DateTime, ARRAY
from sqlalchemy.orm import relationship

from database import Base #base is the base class defined in database.py. i will extend it.

class Picture(Base):
    __tablename__ = 'picture'
    
    elo = Column(Integer)
    image_path = Column(String(100), primary_key = True)