#!/usr/bin/python3
"""Defines a class City for city object"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for city"""
    state_id = ""
    name = ""
