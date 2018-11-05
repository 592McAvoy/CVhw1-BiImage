from PIL import Image
import numpy as np
from bi_op import *

if __name__ == '__main__':
    filename = 'example/2.jpg'  #input image - shape(H,W,C)

    #read image and translate to binary image
    im = Image.open(filename)    
    img = np.array(im)
    img = toBiImage(img)    #binary image - shape(H,W)

    #init SE
    #SE = np.array([[0,255,0],[255,0,255],[0,255,0]])
    SE = np.array([[255,0],[0,255]])

    #set SE
    bimg = BiImage(SE)                  
    bimg.setCenter(1,1)

    #do morphological operations - dilation/erosion/open/close
    result = bimg.dilation(img)
    #result = bimg.erosion(img)
    #result = bimg.open(img)
    #result = bimg.close(img)

    #save result
    newImg = Image.fromarray(np.uint8(result))
    newImg.save('result/2di.png')
