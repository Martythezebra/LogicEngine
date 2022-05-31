###############################################################################
# 
# 
# 
###############################################################################

class ControlPiece:
    def __init__(self, parent) -> None:
        self.parentReference = parent
        self.personalKey = parent.getNextKey()

        

    def getKey(self):
        return self.personalKey