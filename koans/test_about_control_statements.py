#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import Koan, __


class AboutControlStatementsTest(Koan):

    def test_if_then_else_statements(self):
        if True:
            result = "true value"
        else:
            result = "false value"
        self.assertEqual(__, result)

    def test_if_then_statements(self):
        result = "default value"
        if True:
            result = "true value"
        self.assertEqual(__, result)

    def test_if_then_elif_else_statements(self):
        if False:
            result = "first value"
        elif True:
            result = "true value"
        else:
            result = "default value"
        self.assertEqual(__, result)

    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        self.assertEqual(__, result)

    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10:
                break
            result = result * i
            i += 1
        self.assertEqual(__, result)

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0:
                continue
            result.append(i)
        self.assertEqual(__, result)

    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase:
            result.append(item.upper())
        self.assertEqual([__, __, __], result)

    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or European Swallow?"),
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")

        text = __

        self.assertRegex(result[2], text)

        self.assertNotRegex(result[0], text)
        self.assertNotRegex(result[1], text)
        self.assertNotRegex(result[3], text)
