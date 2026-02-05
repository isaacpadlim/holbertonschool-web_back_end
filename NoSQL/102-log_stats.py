#!/usr/bin/env python3
"""Nginx logs stats with top 10 IPs"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    col = client.logs.nginx

    print("{} logs".format(col.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(method, col.count_documents({"method": method})))
    print("{} status check".format(col.count_documents({"method": "GET", "path": "/status"})))

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 10}
    ]
    for doc in col.aggregate(pipeline):
        print("\t{}: {}".format(doc.get("_id"), doc.get("count")))
