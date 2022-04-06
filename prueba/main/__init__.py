from guizero import *
from email.policy import default

def send_name():
    your_name = name_field.value
    name = Text(content_box,text=f'Encantados de conocerte, {your_name}', 
                size=14, color = "red", 
                font="Consolas", height=100)
    name_field.clear()
    
def highlight():
    name_field.bg = "lightblue"

def lowlight():
    name_field.bg = "white"
    
def hover():
    submit.width = 15
    submit.height = 2
    submit.bg = "lightblue"
    
def dishover():
    submit.width = 10
    submit.height = 0
    submit.bg = "lightgrey"
    
app = App(title="Hello World!",height=720, width=1280)

title_box = Box(app,align="top",width="fill", height=110)
title = Text(title_box, text="Como te llamas", height=110,size=20,font="Consolas")

content_box = Box(app,align="top",width="fill", height=100)

form_box = Box(app,align="top",width="500", height=100)

texto = Text(form_box,text="Introduce tu nombre: ", align = "left",size=14, font="Consolas")
name_field = TextBox(form_box,text="", align = "right", width=100)

# When the mouse enters the TextBox
name_field.when_mouse_enters = highlight
# When the mouse leaves the TextBox
name_field.when_mouse_leaves = lowlight

button_box = Box(app,align="top",width="fill", height=100)
submit = PushButton(button_box, text="Enviar", command=send_name,width = 10)
submit.bg = "lightgrey"

# When the mouse enters the PushButton
submit.when_mouse_enters = hover
# When the mouse leaves the PushButton
submit.when_mouse_leaves = dishover

app.display()
