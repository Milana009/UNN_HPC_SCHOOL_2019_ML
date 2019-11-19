import sys
import cv2
import logging as log
import argparse

sys.path.append('../src')
from imagefilter import ImageFilter

def build_argparse():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help = 'your input', type = str)
    
    parser.add_argument('-w', '--width', help = 'your width', type = int)
    
    parser.add_argument('-l', '--height', help = 'your height', type = int)
    
    #
    # Add your code here
    #
    
    return parser

def main():
    log.basicConfig(format="[ %(levelname)s ] %(message)s", level=log.INFO, stream=sys.stdout)
    log.info("Hello image filtering")
    args = build_argparse().parse_args()
    
    imagePath = args.input

    log.info(imagePath)
    
    image_source = cv2.imread(imagePath, 1)

    log.info(image_source.shape)
    
    myFilter = ImageFilter(gray = True, shape = (args.width, args.height))
    
    image_final = myFilter.process_image(image_source)
    cv2.imshow("Image", image_final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
   
    
    #
    # Add your code here
    #
    
    
    return
    
if __name__ == '__main__':
    sys.exit(main())