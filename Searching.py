#  Copyright (C) 2011  Groza Cristian
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

class SearchElem():
    def __init__(self, elem):
        self.search_index = 0
        self.elem_name = ""
        self.elem_path = ""
        self.matched_tags = []
        self.tags = []

class Search():
    def __init__(self, elements):
        self.elems = elems

    def DoSearch(self):
        pass

    def CalcSearchIndex(self, elem):
        pass

    def GetMatches(self):
        pass
