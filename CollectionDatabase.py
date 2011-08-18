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

    def GetCollection(self, name):
        pass

    def CreateCollection(self, collection_name, collection_folder):
        pass

    def RemoveCollection(self, collection):
        pass

    def RenameCollection(self, collection):
        pass

