#!/usr/bin/python3
"""Package handler"""
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()
storage.reload()


