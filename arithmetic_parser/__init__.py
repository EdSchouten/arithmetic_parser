import pypeg2
import re


class Visitor:

    def visit_number(self, value):
        pass

    def visit_addition(self, first, tail):
        pass

    def visit_multiplication(self, first, tail):
        pass


_visitor = None


class _Number:
    grammar = re.compile(r'\d+')

    def __init__(self, value):
        self.value = _visitor.visit_number(value)


class _TerminalExpression:
    grammar = None

    def __init__(self, operand):
        self.value = operand.value


class _MultiplicationExpression:
    grammar = _TerminalExpression, pypeg2.maybe_some(
        re.compile(r'\*|/'),
        _TerminalExpression,
    )

    def __init__(self, operands):
        if len(operands) == 1:
            self.value = operands[0].value
        else:
            processed_operands = []
            for i in range(1, len(operands), 2):
                if operands[i] == '*':
                    processed_operands.append((True, operands[i + 1].value))
                else:
                    processed_operands.append((False, operands[i + 1].value))
            self.value = _visitor.visit_multiplication(
                operands[0].value, processed_operands)


class _AdditionExpression:
    grammar = _MultiplicationExpression, pypeg2.maybe_some(
        re.compile(r'\+|-'),
        _MultiplicationExpression,
    )

    def __init__(self, operands):
        if len(operands) == 1:
            self.value = operands[0].value
        else:
            processed_operands = []
            for i in range(1, len(operands), 2):
                if operands[i] == '+':
                    processed_operands.append((True, operands[i + 1].value))
                else:
                    processed_operands.append((False, operands[i + 1].value))
            self.value = _visitor.visit_addition(
                operands[0].value, processed_operands)


class _ParenthesizedExpression:
    grammar = "(", _AdditionExpression, ")"

    def __init__(self, operand):
        self.value = operand.value

_TerminalExpression.grammar = [
    _Number,
    _ParenthesizedExpression,
]


def parse(text, visitor):
    global _visitor
    _visitor = visitor
    return pypeg2.parse(text, _AdditionExpression).value
