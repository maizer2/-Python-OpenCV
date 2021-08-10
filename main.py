from Program.imageReader import ImageReader as Ir
from Program.imageShow import ImageShow as Is
path = "/image"

if __name__ == "__main__":

    image = Ir.Read(path + "/testImg.png")
    Is.Show(image)