#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

from runner.koan import Koan, __


class AboutLambdasTest(Koan):
    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        add_one = lambda n: n + 1
        self.assertEqual(__, add_one(10))

    # ------------------------------------------------------------------

    def make_order(self, order):
        return lambda qty: str(qty) + " " + order + "s"

    def test_accessing_lambda_via_assignment(self):
        sausages = self.make_order("sausage")
        eggs = self.make_order("egg")

        self.assertEqual(__, sausages(3))
        self.assertEqual(__, eggs(2))

    def test_accessing_lambda_without_assignment(self):
        self.assertEqual(__, self.make_order("spam")(39823))
