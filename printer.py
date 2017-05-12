#!/usr/bin/env python3

import arithmetic_parser


class Printer(arithmetic_parser.Visitor):

    @staticmethod
    def visit_number(value):
        return value

    @staticmethod
    def visit_addition(first, tail):
        r = '(' + first
        for do_addition, value in tail:
            r += ' + ' if do_addition else ' - '
            r += value
        r += ')'
        return r

    @staticmethod
    def visit_multiplication(first, tail):
        r = '(' + first
        for do_addition, value in tail:
            r += ' * ' if do_addition else ' / '
            r += value
        r += ')'
        return r


c = Printer()
assert (arithmetic_parser.parse('((((73 * (5) + 1238 * (769) * 19))))', c) ==
        '((73 * 5) + (1238 * 769 * 19))')
