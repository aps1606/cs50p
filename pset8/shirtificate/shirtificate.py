from fpdf import FPDF
from PIL import Image

class PDF(FPDF): # FPDF class from fpdf library extended by creating own subclass PDF

    def __init__(self, name, shirt_img, orientation = "P", unit = "mm", format = "A4"):
        super().__init__(orientation, unit, format)
        
        # below sets the main header of the page
        self.add_page()
        self.set_font("helvetica","B", size = 30)
        self.text(60,40,text = "CS50 Shirtificate")

        # below import the shirt and writes the name on the shirt
        
        self.image(shirt_img,15,70)
    
        # below writes the name on the shirt
        self.name = name
        self.set_font("helvetica","B",size = 20)
        self.set_text_color(255,255,255)
        self.text(60,125,text = f"{name} took CS50")

def main():
    
    name = input("Name: ")
    shirt_img = Image.open("shirtificate.png")
    shirt_img = shirt_img.resize((500,500))

    pdf = PDF(name, shirt_img) # instantiate an instance of the pdf sub-class

    pdf.output("Shirtificate.pdf")

if __name__ == "__main__":
    main()


'''
Psuedo/notes:

- get user input of name

output pdf:
- The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
- import the shirt image into the pdf
- pdf details:
    - page orientation is portrait
    - A4, 210mm wide and 297mm tall
    - 
- output a pdf cs50 shirtificate in pdf format




'''