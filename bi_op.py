import numpy as np

def toBiImage(img):
    H,W,C = img.shape
    img = img.reshape(C,H,W)
    for c in range(C):
        for h in range(H):
            for w in range(W):
                if img[c,h,w]>128:
                    img[c,h,w]=255
                else:
                    img[c,h,w]=0
    return img.reshape(H,W,C)[:,:,0]
    

class BiImage():
    def __init__(self, img, SE):
        self.img = img  #shape(H,W)
        self.SE = SE    #shape(HH,WW)

    def setCenter(self, row, col):
        self.centR = row
        self.centC = col
                        

    def dilation(self):
        result = self.img.copy()

        H,W = result.shape
        HH,WW = self.SE.shape
    
        for h in range(H-HH+1):
            for w in range(W-WW+1):
                area = self.img[h:h+HH,w:w+WW]
                    
                match = False
                for hh in range(HH):
                    for ww in range(WW):
                        if self.SE[hh,ww] == 255 and area[hh,ww] == self.SE[hh,ww]:
                            match = True
                            break

                if match:        
                    result[h+self.centR,w+self.centC] = 255
                else:
                    result[h+self.centR,w+self.centC] = 0
                              
        return result
    
    def erosion(self):
        result = self.img.copy()

        H,W = result.shape
        HH,WW = self.SE.shape
    
        
        for h in range(H-HH+1):
            for w in range(W-WW+1):
                area = self.img[h:h+HH,w:w+WW]
                    
                match = True
                for hh in range(HH):
                    for ww in range(WW):
                        if self.SE[hh,ww] == 255 and area[hh,ww] != self.SE[hh,ww]:
                            match = False
                            break

                if match:        
                    result[h+self.centR,w+self.centC] = 255
                else:
                    result[h+self.centR,w+self.centC] = 0
                    
        return result
