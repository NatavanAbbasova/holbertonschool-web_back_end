#!/usr/bin/env python3
"""Type annotaded function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum as a float"""
    return sum(input_list)
