#!/usr/bin/env python3

import arithmetic_parser
import collections


class Counter(arithmetic_parser.Visitor):

    @staticmethod
    def visit_number(value):
        return collections.Counter({int(value): 1})

    @staticmethod
    def visit_addition(first, tail):
        accumulator = first
        for do_addition, value in tail:
            accumulator += value
        return accumulator

    @staticmethod
    def visit_multiplication(first, tail):
        accumulator = first
        for do_multiplication, value in tail:
            accumulator += value
        return accumulator


c = Counter()
assert (arithmetic_parser.parse('1 + 3 * 3 + 7 * 1 * 8', c) ==
        {1: 2, 3: 2, 7: 1, 8: 1})
