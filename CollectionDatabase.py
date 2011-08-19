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

from CollectionManager import *


class CollectionDatabase():
    """
    All manipulation of CollectionManagers will be done through this class.
    """
    def __init__(self, collections_file):
        self.collections_file = collections_file
        self.collections = {}

    def __ReadCollectionsFile(self):
        pass

    def __WriteCollectionsFile(self):
        pass

    def GetCollection(self, collection_name):
        return self.collections[name]

    def CreateCollection(self, collection_name, collection_folder):
        new_collection = Collection()
        new_collection.name = collection_name
        new_collection.dir = collection_folder
        if self.colloction_name not in collections:
            self.collections[collection_name] = new_collection

    def RemoveCollection(self, collection_name):
        del self.collections[collection_name]

    def RenameCollection(self, collection_name, new_collection_name):
        collection = self.collections[collection_name]
        collection.name = new_collection_name
        del self.collections[collection_name]
        self.collections[new_collection_name] = collection
