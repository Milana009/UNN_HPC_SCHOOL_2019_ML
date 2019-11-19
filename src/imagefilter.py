import cv2

class ImageFilter():
    def __init__(self, gray = False, shape = None, crop = None):
        self.gray = gray
        if shape:
            self.shape = shape
        if crop:
            self.crop = crop
    
    def process_image(self, image):
        #
        # Put your code here, like example
        #
        #if self.shape:
        #    do something
        # 
        if self.shape:
            image = cv2.resize(image, dsize = self.shape)
        if self.gray:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #if self.crop:
            #image = cv2.cropped(image, )
            
        #width = image.shape[0]
        
        #image[ : width // 2 , : , : ] = 0
        return image