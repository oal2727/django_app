from PIL import Image, ImageChops, ImageOps, ImageEnhance

class OperationBasics1():

    def __init__(self, img):
        self.img = img

    # part 1 - 5
    def identify(self): # 
        arr=self.img.load()
        for x in range(self.img.size[0]):
            for y in range(self.img.size[1]):
                arr[x,y]=self.img.getpixel((x,y))
        return self.img

    def reverse(self):
        arr=self.img.load()
        for x in range(self.img.size[0]):
            for y in range(self.img.size[1]):
                arr[x,y]=255-self.img.getpixel((x,y))
        return self.img

    def umbral(self,umbral):
        arr=self.img.load()
        for x in range(self.img.size[0]):
            for y in range(self.img.size[1]):
                if self.img.getpixel((x,y))>umbral:
                    arr[x,y]=255
                else:
                    arr[x,y]=0
        return self.img

    def umbralReverse(self,umbral1):
        arr=self.img.load()
        for x in range(self.img.size[0]):
            for y in range(self.img.size[1]):
                if self.img.getpixel((x,y))>umbral1:
                    arr[x,y]=0
                else:
                    arr[x,y]=255
        return self.img

    def umbralBinary(self,umbral1,umbral2):
        arr=self.img.load()
        for x in range(self.img.size[0]):
            for y in range(self.img.size[1]):
                if self.img.getpixel((x,y))>umbral1 & self.img.getpixel((x,y))<umbral2:
                    arr[x,y]=0
                else:
                    arr[x,y]=255
        return self.img

    # part 6 - 10 

    def algortimoInterbaloUmbralBinarioInvertido(self,img, umbral1, umbral2):
        arr = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if img.getpixel((x, y)) > umbral1 & img.getpixel((x, y)) < umbral2:
                    arr[x, y] = 255
                else:
                    arr[x, y] = 0
        return arr

    def algoritmoReduccionGrises(self, img, umbral1, umbral2, umbral3, umbral4):
        arr = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if img.getpixel((x, y)) < umbral1:
                    arr[x, y] = 0
                elif img.getpixel((x, y)) > umbral1 & img.getpixel((x, y)) < umbral2:
                    arr[x, y] = img.getpixel((x, y))
                elif img.getpixel((x, y)) > umbral2 & img.getpixel((x, y)) < umbral3:
                    arr[x, y] = img.getpixel((x, y))
                elif img.getpixel((x, y)) > umbral3 & img.getpixel((x, y)) < umbral4:
                    arr[x, y] = img.getpixel((x, y))
                else:
                    arr[x, y] = img.getpixel((x, y))
        return arr

    
    def algoritmoUmbralInverso(self, img, umbral):
        arr = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if img.getpixel((x, y)) > umbral:
                    arr[x, y] = 0
                else:
                    arr[x, y] = 255
        return arr


    def algoritmoExtension(self, img, umbral1, umbral2):
        arr = img.load()
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                if img.getpixel((x, y)) > umbral1 & img.getpixel((x, y)) < umbral2:
                    primero = 255 * (img.getpixel((x, y)) - umbral1)
                    segundo = (umbral2 - umbral1)
                    primero = primero / segundo
                    primero = int(primero)
                    arr[x, y] = abs(primero)
                else:
                    arr[x, y] = 255
        return arr

    # functions use
    def operadorUmbralBinarioInvertido(self,min,max): # 6 operator # ready
        arr = self.algortimoInterbaloUmbralBinarioInvertido(self.img,min,max)
        return arr

    def escalaGrises(self): # 7 operator (ready)
        newImg = ImageOps.grayscale(self.img)
        return newImg
    def escalaGrisesInvertido(self): # 8 operator (ready)
        self.algoritmoUmbralInverso(self.img, 128)

    def operadorExtension(self): # 9 operator (ready)
        self.algoritmoExtension(self.img, 50, 180)

    def operadorReduccionGrises(self): # 10 operator (ready)
        self.algoritmoReduccionGrises(self.img, 50, 120, 180, 220)

