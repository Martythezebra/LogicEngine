###############################################################################
# 
# 
# 
###############################################################################

import PieceAdministrative

class RootDataManager(PieceAdministrative.AdministrativePiece):

    def __init__(self, parent) -> None:
        super().__init__(parent)

        self.masterlist = {}        #contains every controlPiece
        
        self.listObjects = {}       #
        self.listTypes = {}         #
        self.listProperties = {}    #

        self.listOperations = {}    #
        self.listRules = {}         #

        self.listQueries = {}       #



    def searchbyPrimaryKey(self, key):
        return self.masterlist.get(key)