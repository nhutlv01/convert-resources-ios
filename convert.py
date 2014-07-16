from PIL import Image
import os

# Config here
directoryPath = r'Resized'
deviceType = '' #iphone 1 --- ipad 2

iphone4_retina_suffix = '@2x~iphone'
iphone5_retina_suffix = '-568h@2x~iphone'
iphone_non_retina_suffix = '~iphone'

ipad_non_retina_suffix = '~ipad'
ipad_retina_suffix = '@2x~ipad'




opt = raw_input('Enter device type (iPhone 1 --- iPad 2): ')

if  opt == '1' or opt == '2':
    deviceType = opt
else:
    print('Device type is invalid')
    exit()


def isImage(path):
    try:
        Image.open(path)
    except IOError:
        return False;
    return True;

def getImages():
    imagesArray = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        if isImage(f):
            imagesArray.append(f)
    return imagesArray

def resizeImage():
    imagesArray = getImages()
    
    if len(imagesArray):
        if not os.path.exists(directoryPath):
            os.makedirs(directoryPath)

    for i in xrange(0, len(imagesArray)):
        fileName = imagesArray[i]
        name = fileName[:len(fileName)-4]
        ext = fileName[len(fileName)-4:]

        image = Image.open(os.path.join('.', fileName))

        # Get retina size
        originalWidth = image.size[0]
        originalHeight = image.size[1]

        if deviceType == '1': #iPhone
            # Retina
            image.save(os.path.join(directoryPath, name + iphone4_retina_suffix + ext))
            image.save(os.path.join(directoryPath, name + iphone5_retina_suffix + ext))
            
            # Resize it to non-retina
            image = image.resize((originalWidth / 2, originalHeight / 2), Image.BILINEAR)
            image.save(os.path.join(directoryPath, name + iphone_non_retina_suffix + ext))
        else : #iPad
            image.save(os.path.join(directoryPath, name + ipad_retina_suffix + ext))
            
            # Resize it to non-retina
            image = image.resize((originalWidth / 2, originalHeight / 2), Image.BILINEAR)
            image.save(os.path.join(directoryPath, name + ipad_non_retina_suffix + ext))
    
    print "Done!"

if __name__ == "__main__":
    resizeImage()