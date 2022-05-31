import ControlCenter


x = ControlCenter.ControlCenter()

print("My rootWindowKey is ")
print(x.myRootWindowManager.getKey())

print("My rootDataKey is ")
print(x.myRootDataManager.getKey())

print("My rootSaveLoadKey is ")
print(x.myRootSaveLoadManager.getKey())
