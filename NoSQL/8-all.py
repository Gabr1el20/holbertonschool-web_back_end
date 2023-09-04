#!/usr/bin/env python3
"""Task 8:
    List all documents in python"""


def list_all(mongo_collection):
    "A py function that lists all documents in a collection"
    list_of_docs = []
    for doc in mongo_collection.find():
        list_of_docs.append(doc)
    return list_of_docs