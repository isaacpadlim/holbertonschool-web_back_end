#!/usr/bin/env python3
"""Inserts a new document in a MongoDB collection based on kwargs"""

def insert_school(mongo_collection, **kwargs):
    """Inserts a document into mongo_collection and returns the new _id"""
    if mongo_collection is None or not kwargs:
        return None
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
