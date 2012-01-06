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

    # This string is wrintten in any new collection file. The respective fields are updated.
    defaul_xml_tree ="""<?xml version="1.0" encoding="UTF-8"?>

 <Collection name = "SampleCollection" path = "/media/collection.xml" >

<!--    <Element tags = "sample element"  name = "sample_element" path = "/sample/path.png"/> -->

  </Collection>

  """

    def __init__(self, collections_file, collections_dir):
        self.collections_file = collections_file
        self.collections_dir = collections_dir
        self.collections = {}
        self._ReadCollectionsFile()

    def _ReadCollectionsFile(self):
        # for every line in file, split on equal and make the result key : string
        with open(self.collections_file, "r") as col_file:
            for line in col_file:
                left_right = line.split("=")
                col_name = left_right[0].strip()
                col_file = left_right[1].strip()
                if col_file and col_name:
                    if os.path.exists(col_file):
                        collection = CollectionManager(col_file, col_name)
                        if collection.IsOk():
                            self.collections[col_name] = collection

    def _WriteCollectionsFile(self):
        # empty file
        with open(self.collections_file, "w") as col_file:
            col_file.write("")

        # write the format key = string in file 
        with open(self.collections_file, "a") as col_file:
            for col in self.collections:
                col_file.write(col + " = " + self.collections[col].collection_file + "\n")
                
    def FindElement(self, file_path):
        for col_name in self.collections:
            element = self.collections[col_name].FindElementByPath(file_path)
            if element != False:
                return element
        return False

    def FindAndRemoveElement(self, file_path):
        for col_name in self.collections:
            collection = self.collections[col_name]
            element = collection.FindElementByPath(file_path)
            if element != False:
                collection.RemoveElement(element.get("name"))

    def FindFileAndDelete(self, file_path):
        for col_name in self.collections:
            col = self.collections[col_name]
            elem = col.FindElementByPath(file_path)
            if elem != False:
                col.DeleteElement(elem.get("name"))
                return

    def GetCollection(self, collection_name):
        return self.collections[collection_name]

    def GetCollections(self):
        cols = []
        for col in self.collections:
            cols.append(self.collections[col])
        return cols

    def CreateCollection(self, collection_name, collection_folder):
        if collection_name not in self.collections:
            collection_file = os.path.join(self.collections_dir, ".".join([collection_name, "xml"]))

            # create collection file
            with open(collection_file, "w") as col_file:
                col_file.write(CollectionDatabase.defaul_xml_tree)

            #create collection
            new_collection = CollectionManager(collection_file, collection_name)
            new_collection.SetName(collection_name)
            new_collection.SetDir(collection_folder)
            self.collections[collection_name] = new_collection
            new_collection.SaveTree()
            new_collection.IndexFiles()
            
        self._WriteCollectionsFile()
        return new_collection
        
    def RemoveCollection(self, collection_name):
        # remove collection xml file
        os.remove(self.GetCollection(collection_name).collection_file)
        # delete it from the internal dictionaries
        del self.collections[collection_name]
        self._WriteCollectionsFile()

    def RenameCollection(self, collection_name, new_collection_name):
        collection = self.collections[collection_name]
        collection.SetName(new_collection_name)
        new_collection_file = os.path.join(self.collections_dir, new_collection_name)
        os.rename(collection.collection_file, new_collection_file)
        collection.collection_file = new_collection_file
        del self.collections[collection_name]
        self.collections[new_collection_name] = collection
        self._WriteCollectionsFile()

    def MoveElement(self, elem, new_collection):
        new_path = os.path.join(new_collection.dir, elem.get("name"))
        shutil.move(elem.get("path"), new_path)
        elem.set("path", new_path)
        new_collection.AddElement(elem)

    def FindParentCollection(self, element):
        for col_name in self.collections:
            col = self.collections[col_name]
            if col.FindElementByPath(element.get("path")) != False:
                return col
        
    
