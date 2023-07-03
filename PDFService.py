from PIL import Image
from filepathClass import FilePath
def openFile(fileLocation):
    try:
        imageObj = Image.open(fileLocation)
        return imageObj
    except (FileNotFoundError, Image.UnidentifiedImageError) as err:
        print('openFile operation from PDFService.py failed [ISSUE BELOW]')
        print(err)
    

def convertFormat(openedFile):
    try:
        imageObj = openedFile.convert('RGB')  
        return imageObj
    except:
        print('convertFile operation from ConvertToPDF.py failed [ISSUE]')


def generatePDF(imgList, filepathObj):
    try:
        folder_directory = filepathObj.getPDFFolderPath() 
        filepath = folder_directory + '/printable.pdf'

        imgList[0].save(filepath, save_all=True, append_images = imgList[1:] )
    except (ValueError, OSError) as err:
        print(err)
        print('PDFService.generatePDF error [ISSUE PRINTED ABOVE]')
    
    





