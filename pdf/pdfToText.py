# https://github.com/UB-Mannheim/tesseract/wiki
# pip install pytesseract
from PIL import Image
from pytesseract import pytesseract
import enum
from pdf2image import convert_from_path
import os
from docx import Document

class OS(enum.Enum):
    Mac = 0
    Windows = 1
      
class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    
class ImageReader:
    def __init__(self,os: OS,pdfPath: str):
        if os == OS.Windows:
            self.windowsPath = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = self.windowsPath
            print('[+] Running on windows\n')
            self.doc = Document()         
                    
            self.pdfPath = pdfPath
            self.pdfToImage()
            
            self.folderImg = r'./pdfImages'
            
    def extractText(self,image:str,lang:str) -> str:
        img = Image.open(image)
        extractedText = pytesseract.image_to_string(img, lang=lang)
        return extractedText
        
    def pdfToImage(self):
        self.images = convert_from_path(self.pdfPath,500,poppler_path=r"C:\Program Files\poppler-24.02.0\Library\bin")
        
        for img in range(len(self.images)):
            self.images[img].save('./pdfImages/page'+str(img)+'.jpg','JPEG')
            
    def imgToText(self):
        for fileName in os.listdir(self.folderImg):
            if fileName.endswith(".jpg") or fileName.endswith(".png"):
                imgPath = os.path.join(self.folderImg,fileName)
                print(imgPath)
                extractedText = self.extractText(imgPath,lang='eng')
                # print(extractedText)+
                self.saveToDocx(extractedText)
                
    def saveToDocx(self, data: str):
        # for d in data:
        self.doc.add_paragraph(data)  
        self.doc.save("./output.docx")
        
        
def main():
    app = ImageReader(OS.Windows,'./pp.pdf')
    # text = app.extractText('./a.jpg',lang='eng')
    # print(text)
    app.imgToText()
    
if __name__ == "__main__":
    main()