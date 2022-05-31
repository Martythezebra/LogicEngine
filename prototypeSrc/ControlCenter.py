###############################################################################
# 
# 
# 
###############################################################################

import RootWindowManager, RootDataManager, RootSaveLoadManager

class ControlCenter:
    def __init__(self) -> None:
        self.myRootWindowManager = RootWindowManager.RootWindowManager(self)
        self.myRootDataManager = RootDataManager.RootDataManager(self)
        self.myRootSaveLoadManager = RootSaveLoadManager.RootSaveLoadManager(self)

        self.currentKey = 0

    def getNextKey(self):
        self.currentKey += 1
        return self.currentKey