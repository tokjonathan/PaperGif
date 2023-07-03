import shortuuid 
import datetimeService

#Generates a unqiue ID for each video-to-frame project made.
def generateOrderID():
    orderID = 'order' + shortuuid.ShortUUID().random(length=12) #re1x2uoii12x
    return orderID

def generateUserID():
    userID ='UU' + shortuuid.ShortUUID().random(length=3) #UUe88
    return userID

def generateVideoID():
    videoID = 'VID' + shortuuid.ShortUUID().random(length=5) #VIDe912z
    return videoID
#def generateVideoID():
    

