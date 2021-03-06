# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from unittest import TestCase
from src.lib.page import Page


class TestPage(TestCase):

    def test__init__(self):
        page = Page(None, 'title', 1)
        self.assertEqual(page.data, None)
        self.assertEqual(page.title, 'title')
        self.assertEqual(page.number, 1)
        self.assertFalse(page._pixmap)
