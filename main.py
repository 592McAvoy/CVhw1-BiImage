from PIL import Image
import numpy as np
from bi_op import *

if __name__ == '__main__':
    filename = 'example/bi.png'
    im = Image.open(filename)
    
    img = np.array(im)
    print(img.shape)
    print(img)
    SE = np.array([[0,255,0],[255,0,255],[0,255,0]])

    #gimg = GrayImage(img,SE)
    bimg = BiImage(img,SE)
    #mi = bimg.toBiImage()
    #newImg = Image.fromarray(np.uint8(mi))
    #newImg.save('bi.png')
                  
    bimg.setCenter(1,1)

    result = bimg.dilation()
    #result = bimg.erosion()
    
    newImg = Image.fromarray(np.uint8(result))
    newImg.save('result/di.png')
