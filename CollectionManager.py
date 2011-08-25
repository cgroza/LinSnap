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
import shutil
import os

class CollectionManager():
    """
    Collection manipulation will be done through this class. 
    """

    def __init__(self, collection_file, name):
        self.collection_file = collection_file
        self.elem_tree = ElementTree(None, self.collection_file)
        self.name = name
        iterator = self.elem_tree.iter("Collection")
        for col in iterator:
            self.dir = col.get("path")

    def SetName(self, new_name):
        iterator = self.elem_tree.iter("Collection")
        for col in iterator:
            col.set("name", new_name)

    def SaveTree(self):
        self.elem_tree.write(self.collection_file, "utf-8")

    def CreateElement(self, attrs):
        SubElement(self.elem_tree, "Element", attrs)
        self.SaveTree()
        
    def GetElementAttribute(self, name, attr):
        iterator = self.elem_tree.iter("Element")
        for e in iterator():
            if e.get("name") == name: return e.get(attr)
        return None

    def SetElementAttribute(self, name, attr, val):
        iterator = self.elem_tree.iter("Element")
        for e in iterator():
            if e.get("name") == name:
                e.set(attr, val)


    def AddElement(self, element):
        self.elem_tree.getroot().insert(1, element)
        self.SaveTree()

    def DeleteElement(self, name):
        iterator = self.elem_tree.iter("Element")
        for e in iterator():
            if e.get("name") == name:
                self.elem_tree.getroot().remove(e)
                self.SaveTree()                

    def RenameElement(self, name, new_name):
        iterator = self.elem_tree.iter("Element")
        for e in iterator():
            if e.get("name") == name:
                e.set("name", new_name)
                new_path = os.join(os.split(e.get("path"))[0], new_name)
                os.rename(e.get("path"), new_path)
                e.set("path", path) 
                self.SaveTree()

    def MoveElement(self, elem, new_collection):
        iterator = self.elem_tree.iter("Element")
        for e in iterator():
            if e.get("name") == name:
                new_collection.AddElement(e)
                self.rename(e.get("path"), os.join(new_collection.dir, elem.get("name")))
                self.elem_tree.getroot().remove(e)
                self.SaveTree()
