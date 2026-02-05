#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection"""

def list_all(mongo_collection):
    """Returns a list of all documents in the given MongoDB collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
