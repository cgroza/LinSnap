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

#!/usr/bin/env python
# -*- coding: utf-8 -*-


from xml.etree.ElementTree import *

class CollectionManager():
    """
    Collection manipulation will be done through this class. 
    """

    class CollectionElem():
        """
        This class is used to store information about collection elements.
        """
        def __init__(self, name, file_name, tags):
            self.name = name
            self.file_name = file_name
            self.tags = tags

    def __init__(self, collection_file):
        self.collection_file = collection_file
        self.elem_tree = ElementTree(None, self.collection_file)
        self.name = ""
        self.dir = ""

    def GetElementAttribute(self, elem, attr):
        pass

    def SetElementAttribute(self, elem, attr, val):
        pass

    def AddElement(self, elem)

    def DeleteElememnt(self, elem):
        pass

    def RenameElement(self, elem):
        pass

    def MoveElement(self, elem, new_collection):
        pass

