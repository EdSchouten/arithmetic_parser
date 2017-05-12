#!/usr/bin/env python3

import arithmetic_parser


class Calculator(arithmetic_parser.Visitor):

    @staticmethod
    def visit_number(value):
        return int(value)

    @staticmethod
    def visit_addition(first, tail):
        accumulator = first
        for do_addition, value in tail:
            if do_addition:
                accumulator += value
            else:
                accumulator -= value
        return accumulator

    @staticmethod
    def visit_multiplication(first, tail):
        accumulator = first
        for do_multiplication, value in tail:
            if do_multiplication:
                accumulator *= value
            else:
                accumulator /= value
        return accumulator


c = Calculator()
assert arithmetic_parser.parse('73 * 5 + 1238 * 769 * 19', c) == 18088783
