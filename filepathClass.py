import os
class FilePath():
    def __init__(self, orderID):
        self.rootpath = os.getcwd()
        self.tempMedia = '/tempMedia'
        self.vault = '/vault'
        self.orderFolder = '/' + orderID
        self.frameFolder = self.orderFolder + '/Frame'
        self.pageFolder = self.orderFolder  + '/Page'
        self.PDFFolder = self.orderFolder + '/PDF'

       

    def getFrameFolderPath(self):
        folderpath = self.rootpath + self.vault + self.orderFolder + '/Frame'
        return folderpath
    
    def getPageFolderPath(self):
        folderpath = self.rootpath + self.vault + self.orderFolder + '/Page'
        return folderpath
    
    def getPDFFolderPath(self):
        folderpath = self.rootpath + self.vault + self.orderFolder + '/PDF'
        return folderpath
    
    def getFrameFilePath(self,i):
        framepath = self.rootpath + self.vault + self.orderFolder + '/Frame/Frame' + str(i) + '.png'
        return framepath
    
    def createNewFolder(*args):
        path = os.getcwd() 
        for item in args:
            path = path + '/' + item
        os.makedirs(path, exist_ok=True)
        
        
    
