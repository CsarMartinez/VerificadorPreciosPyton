from tkinter import*
from PIL import ImageTk, Image
import requests

codigo=""
    
def key_pressed(event):
    global codigo
    if event.keysym == "Return":
        print(codigo)
        URL = "http://localhost/api/index2.php?codigo=" + codigo
        Respuesta = requests.get(URL)
        
        Datos = Respuesta.json()
        codigo = ""
        if Datos["Status"] == 200:
            # loads the img from the product
            loadImg(".img/" + Datos["Imagen"])
            labelProd.config(text= Datos["Nombre"])
            labelPrice.config(text=Datos["Precio"])
            labelDesc.config(text=Datos["Descripcion"])
        else:
            labelProd.config(text= "No existe")
            labelPrice.config(text="")
            labelDesc.config(text="")
    else:
        codigo+=event.keysym

def loadImg(imgPath):
    # imagen
    # PNG, JPEG and GIF
    render = ImageTk.PhotoImage(Image.open(imgPath))
    img = Label(ventana, image=render, width=500, height=500)
    img.image = render
    img.place(x=Vwidth/2 - 249, y=250)

    productos = readjson()

#Ventana
ventana = Tk()
#ventana.geometry("1536x864")
ventana.geometry(str(ventana.winfo_screenwidth()) + "x" +  str(ventana.winfo_screenheight()))
ventana.title("Titulo")
ventana.update()

fuente = ("Arial", 20, "bold")
Vwidth = ventana.winfo_width()
Vheight = ventana.winfo_height()

#Label 1
label1 = Label(ventana, text="Verificador de precios", font=("Microsoft Sans Serif", "40"))
label1.pack()
ventana.update()
label1.place(x=ventana.winfo_width()/2 - label1.winfo_width()/2,y=0)

#Label 2
label2 = Label(ventana, text="Width = " + str(ventana.winfo_screenwidth()))
label2.pack()
label2.place(x=200,y=100)

#Label 3
label3 = Label(ventana, text="Heigth = " + str(ventana.winfo_screenheight()))
label3.pack()
label3.place(x=200,y=150)

lblpasecodigo = Label(ventana, text="Pase el código de barras por el lector")
lblpasecodigo.pack()
lblpasecodigo.place(x=200, y=200)

# label Product
labelProd = Label(ventana, text="Producto "+str(Vwidth), font=fuente)
labelProd.pack()
labelProd.place(x=10, y=150)

# label Descripcion
labelDesc = Label(ventana, text="Descripcion "+str(Vwidth), font=fuente)
labelDesc.pack()
labelDesc.place(x=10, y=250)


# label Precio
labelPrice = Label(ventana, text="Precio "+str(Vwidth), font=fuente)
labelPrice.pack()
labelPrice.place(x=10, y=350)

#El MainLoop siempre va al final
ventana.mainloop()

