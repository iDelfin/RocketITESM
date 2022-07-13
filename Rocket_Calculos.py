import tkinter as tk
import tkinter.ttk as ttk
import math

Pitch = 0.0
Yaw = 0.0
radientsPitch = 0.0
radientsYaw = 0.0
distanceToRocket = 11.0
distanceToLaunchPad = 10.0
altitude = 0.0
velocity = 0.0
aceleration = 0.0
timeOfFlight = 25.0
enVuelo = True
paracaidasActivado = False

#class Window:
#    def __init__(self, master):
#        self.master = master
# 
#        style = ttk.Style()
#        style.theme_settings("default", {
#           "TButton": {
#               "configure": {"padding": 10},
#               "map": {
#                   "background": [("active", "yellow3"),
#                                  ("!disabled", "yellow")],
#                   "foreground": [("focus", "Red"),
#                                  ("active", "green"),
#                                  ("!disabled", "Blue")]
#               }
#           }
#        })
#        
#        style.theme_use("default")
#        
#        button = ttk.Button(self.master, text = str(altitude))
#        button.pack(padx = 5, pady = 5)
        

def DegreesToRadients(degrees):
    return degrees * math.pi / 180

def PithagorasForHight(distance):
    return math.sqrt((distance**2) - (distanceToLaunchPad**2))

def Velocidad(hight):
    return hight/timeOfFlight

def Aceleracion(velocidad):
    return velocidad/timeOfFlight

#loop mientras despegue y camino a AP
while enVuelo:
    #Get pitch
    radientsPitch = DegreesToRadients(Pitch)
    print("radients of Pitch are: " + str(radientsPitch))
    #move pitch motor
    
    #Get Yaw
    radientsYaw = DegreesToRadients(Yaw)
    print("radients of Yaw are: " + str(radientsYaw))
    #move yaw motor
    
    #Get distance to rocket
    altitudeRT = open('RocketAltitude.txt', 'r')
    distanceToRocket = float(altitudeRT.read())
    altitudeRT.close()
    
    print("Distance to Rocket: " + str(distanceToRocket))
    
    altitude = PithagorasForHight(distanceToRocket)
    print("Hight: " + str(altitude) + " m")
    
    velocity = Velocidad(altitude)
    print("Velocity: " + str(velocity) + " m/s")
    
    aceleracion = Aceleracion(velocity)
    print("Aceleracion: " + str(aceleracion) + " m/s^2")
    
    #Lanzar la carga util
    if velocity < 1.50:
        #activar motores para lanzar carga util (lanzador como la idea de starship?)
        print("Activando motores para lanzar carga util!!!")
        
    #Agregar un if talvez para checar que la carga util haya sido lanzada
    if velocity <= 0.40:
        print("Cambiando a loop de caida... Vamos para abajo!!!!")
        enVuelo = False
        
        
        
#loop mientras esta en caida
while !enVuelo:
    if velocity > 0.40:
        #activar mecanismo para activar paracaidas, ya sea motor para abrir nariz o activar explisivos
        print("Paracaidas ha sido activado!!! llegaré pronto")
        paracaidasActivado = True
    
    #Get hight of rocket
    altitude = PithagorasForHight(distanceToRocket)
    print("hight: " + str(altitude) + " m")
    
    #Get velocity just in case
    velocity = Velocidad(altitude)
    print("Velocity: " + str(velocity) + " m/s")
    
    if paracaidasActivado:
        if velocity > 13:
            print("ADVERTENCIA!!!! CAIDA RAPIDA!!! Muy probable daño al cohete!!!")
        elif velocity < 9:
            print("Velocidad para el aterizaje será DURA!, hora de preocupación y ocupación")
        elif velocity < 5:
            print("Velocidad para el aterizaje será FIRME, cruzen los dedos...")
        else:
            print("Velocidad para el aterizaje esta BIEN!! :D todo bien chido")
    
    
    #root = tk.Tk()
    #window = Window(root)
    #root.mainloop()
    
    
    
    