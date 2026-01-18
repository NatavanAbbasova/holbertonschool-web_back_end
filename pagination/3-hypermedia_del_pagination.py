#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

from typing import Dict


def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    """Deletion-resilient hypermedia pagination"""

    if index is None:
        index = 0

    indexed_dataset = self.indexed_dataset()
    assert index >= 0 and index < len(indexed_dataset)

    data = []
    current_index = index

    # Collect page_size items, skipping deleted indices
    while len(data) < page_size and current_index < len(indexed_dataset):
        if current_index in indexed_dataset:
            data.append(indexed_dataset[current_index])
        current_index += 1

    return {
        "index": index,
        "next_index": current_index,
        "page_size": len(data),
        "data": data
    }

