#!/usr/bin/env python3
from models.base_model import BaseModel
from models.engine import file_storage

classes = {"BaseModel": BaseModel}
storage = file_storage.FileStorage()
storage.reload()
