###############################################################################
# 
# 
# 
###############################################################################


import tkinter
import PieceAdministrative

class RootWindowManager(PieceAdministrative.AdministrativePiece):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        
        self.childTks = {}
        self.mainTk = tkinter.Tk()

    def startStateWindow():
        pass

    def startTransitionWindow():
        pass

    def startQueryWindow():
        pass