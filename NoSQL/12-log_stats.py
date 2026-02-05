#!/usr/bin/env python3
"""Nginx logs stats"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    col = client.logs.nginx

    print("{} logs".format(col.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(method, col.count_documents({"method": method})))
    print("{} status check".format(col.count_documents({"method": "GET", "path": "/status"})))
