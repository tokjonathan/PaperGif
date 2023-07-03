from PIL import Image


#284,160 width,height of current frame
class Page(Image.Image):    
    width = 0
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        

    def createBlankA4(self):
        paper = Image.new('RGB',(self.width,self.height),color='white')
        return paper
    
    def widthNotOverflow(self,n_width,frameObjWidth):
        nextFrameRequiredSpace = n_width + frameObjWidth
        if (nextFrameRequiredSpace < self.width):
            return True
        else:
            return False
    
    def heightNotOverflow(self,n_height,frameObjHeight):
        nextFrameRequiredSpace = n_height + frameObjHeight
        if (nextFrameRequiredSpace < self.height):
            return True
        else:
            return False
    
    def add_margin_to_all(imgpath, top, right, bottom, left, color):
        im = Image.open(imgpath)
        
        width, height = im.size
        new_width = width + right + left
        new_height = height + top + bottom
        print('adding margin to frames')
        result = Image.new(im.mode, (new_width, new_height), color)
        result.paste(im, (left, top))
        result.save(imgpath, dpi=(300,300))


    
    def generatePagePNG(self,list, filepathObj):
        i=0
        while i < len(list):
            filepath = filepathObj.rootpath + filepathObj.vault + filepathObj.orderFolder + '/Page/page' + str((i+1)) + '.png'
            print(filepath)
            list[i].save(filepath, dpi=(300,300)) 
            i += 1
        print('-----PageService Operations Completed-----')

    
        
class Frame():
    width = 0
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
        


frame_count = 1
pageList = []
def bindFrames(pageObj, imageObj, filepathObj, frameObj, noOfFrames, n_height):
    #n_width and n_height is a mulitple n of Frame class - width/height. (n * frame.width or n*frame.height )
    global frame_count
    
    if imageObj == 0:
        blankImg = pageObj.createBlankA4() 
    else :
        blankImg = imageObj
        
    max_frame = noOfFrames #Constant Var
    n_width = 0 #VAR
    
    while (frame_count <= max_frame) and pageObj.widthNotOverflow(n_width,frameObj.width):
        img = Image.open(filepathObj.getFrameFilePath(frame_count))
        print(filepathObj.getFrameFilePath(frame_count))
        blankImg.paste(img,(n_width, n_height)) 
        frame_count += 1
        n_width += frameObj.width
        
    else :
        #Still space on page, change row height
        n_height += frameObj.height
        if (frame_count <= max_frame) and (pageObj.heightNotOverflow(n_height, frameObj.height)):
            print('New Row -')
            bindFrames(pageObj, blankImg, filepathObj, frameObj, max_frame, n_height) # incremented n_height

            

        # Page Maxed out, New Page  
        elif (frame_count <= max_frame) :
            pageList.append(blankImg)
            print('New Page -')
            newPageObj = Page(pageObj.width, pageObj.height)
            bindFrames(newPageObj, 0, filepathObj, frameObj, max_frame, 0) #new Page Object, reset Frame Height
            
        
        elif (frame_count > max_frame): #All Frames added to a page
            pageList.append(blankImg)
            print('All BlankImg added to pagelist, saving pages to page folder...')
            
            print('running Page Maker')
            pageObj.generatePagePNG(pageList,filepathObj) #generate the PNG Pages
            

        
