from pyexpat import model
from tkinter import Scale
from xml.dom.minidom import Entity
from ursina import

app = Ursina()
camera.orthographic = True
camera.fov = 10

car = Entity(
    model='quad',
    texture='assets\car',
    collider='box',
    scale=(2,1)
    rotation_z=-90
)

app.run()