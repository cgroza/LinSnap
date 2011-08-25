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

import os
from CollectionManager import *

class CollectionDatabase():
    """
    All manipulation of CollectionManagers will be done through this class.
    """
    def __init__(self, collections_file):
        self.collections_file = collections_file
        self.collections = {}
        self._ReadCollectionsFile()

    def _ReadCollectionsFile(self):
        with open(self.collections_file, "r") as col_file:
            for line in col_file:
                left_right = line.split("=")
                col_name = left_right[0].strip()
                col_file = left_right[1].strip()
                self.collections[col_name] = CollectionManager(col_file, col_name)

    def _WriteCollectionsFile(self):
        with open(self.collections_file, "w") as col_file:
            col_file.write("")

        with open(self.collections_file, "a") as col_file:
            for col in collections:
                col_file.write(col + " = " + collections[col].dir)
                

    def GetCollection(self, collection_name):
        return self.collections[name]

    def CreateCollection(self, collection_name, collection_folder):
        new_collection = Collection()
        new_collection.name = collection_name
        new_collection.dir = collection_folder
        if self.colloction_name not in collections:
            self.collections[collection_name] = new_collection
        self._WriteCollectionsFile()
        
    def RemoveCollection(self, collection_name):
        del self.collections[collection_name]
        self._WriteCollectionsFile()

    def RenameCollection(self, collection_name, new_collection_name):
        collection = self.collections[collection_name]
        collection.SetName(new_collection_name)
        del self.collections[collection_name]
        self.collections[new_collection_name] = collection
        self._WriteCollectionsFile()
