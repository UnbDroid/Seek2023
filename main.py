#!/usr/bin/env pybricks-micropython
from modules.colors import *
from modules.path import *
from modules.motors import *
from modules.detect import *
from modules.delivery import *
from modules.claw import *

from pybricks.hubs import EV3Brick

# Ajustar axle_track ---------------------------------------------------------------------------

# for i in range(5):                                       # 1212
#     motors.turn(330)                                     # 1212
#     while not is_black():                                # 1216
#         motors.drive(0,5)
#     motors.stop()
#     print(left_motor.angle(), right_motor.angle())
#     brake_motors()

#-----------------------------------------------------------------------------------------------

#* Codigo paraa dar inicio a guerra deth com 😡🤬😶‍🌫️👀🔑 ---------------------------------------------------------------------------------------
entregar_tubos2()
# find_blue_line(0)
# while True:   
#     align_to_begin_scan()
#     scan()
#     go_to_check_point()
#     set_path()

#* Codigo para pegar de ladinho The Ladinho 😎🫡🤠 -------------------------------------------------------------------------------------
# block()
'''find_blue_line(0)
while True:
    align_to_be_ladinho()
    scan_de_ladinho_papai()
    set_path()'''


#* ---------------------------------------------------------

# valores_lidos = []
# while len(valores_lidos) < 10:
#     valores_lidos.append(ultrasound_sensor.distance())

# while (sum(valores_lidos)/len(valores_lidos)) < 135:
#     andar_reto(-500)
#     valores_lidos.pop(0)
#     valores_lidos.append(ultrasound_sensor.distance())
# brake_motors()
# valores_lidos = []
# while len(valores_lidos) < 10:
#     valores_lidos.append(ultrasound_sensor.distance())
# while (sum(valores_lidos)/len(valores_lidos)) < 135:
#     andar_reto(150)
#     valores_lidos.pop(0)
#     valores_lidos.append(ultrasound_sensor.distance())
# brake_motors()
# brake_motors()
# turn_right_pid(90)

# Teste <3

# while not is_red():
#     andar_reto(300)
# brake_motors()
# move_backward(2)
# turn_180()
# while not is_red_left() and not is_red_right():
#     andar_reto(500)
# print(left_motor.angle(), right_motor.angle())
# brake_motors()


# while not is_yellow() or not is_black_left() or not is_black_right():
#     andar_reto(100)
    
#     if is_yellow():
        
#         ajust_color("YELLOW")
#         break
#     elif is_black_left():
        
#         brake_motors()
#         move_backward(6)
#         print("vou virar")
#         turn_left_pid(70) #! Ajustar o valor
#         print("Virei")
#         move_backward(5)
#         turn_right_pid(70)
        
#     elif is_black_right():
        
#         brake_motors()
#         move_backward(5)
#         turn_right_pid(70)
#         move_backward(5)
#         turn_left_pid(70)
    
    # elif color_sensor_floor_left.rgb():
    







# Editando o Range------------------------------------------------------------------------------

# while True:
#     print("Vejo?", tube_is_detected(), "Cor",is_brown_tube() )
    # print("oi novinha", tube_verificator.rgb())
    # Cor (4, 2, 0)
    # Vejo? True Cor (38, 4, 1)

# Teste range sensor auxiliar ------------------------------------------------------------------

# while True:
#     print(red_aux(), green_aux(), blue_aux())
#     wait(500)

# Ajustar curva de 90 graus --------------------------------------------------------------------

# count = 0
# while count < 4:
#     count+=1
#     turn_right_pid(180)
#     print(left_motor.angle(), right_motor.angle())
#     brake_motors()

#-----------------------------------------------------------------------------------------------




# Testar curvas PID ----------------------------------------------------------------------------

# i = 0
# while i < 8 :
#     turn_right_pid(90)
#     wait(500)
#    # brake_motors()
    # i+=1
# move_forward(5)

#-----------------------------------------------------------------------------------------------



# Abrir ou fechar a garra ----------------------------------------------------------------------

# Open()
# wait(2000)
# Close()

#-----------------------------------------------------------------------------------------------



# Ajustar ranges das cores ---------------------------------------------------------------------

# while True:
#     wait(500)
#     print("Esquerda: ",color_sensor_floor_left.rgb() , "Direita: ", color_sensor_floor_right.rgb())
    

#-----------------------------------------------------------------------------------------------



# Ajustar ranges dos tubos ---------------------------------------------------------------------

# while True:
#     print(ultrasound_sensor.distance())

#-----------------------------------------------------------------------------------------------



# Ajustar andar reto ---------------------------------------------------------------------------

# while not is_red_left() and not is_red_right():
#     andar_reto(-500)
# brake_motors()
# wait(3000)
# move_backward(100)
# move_forward(100)

#-----------------------------------------------------------------------------------------------

# Ajustar o ajust color ------------------------------------------------------------------------

# while not is_yellow_left() and not is_yellow_right():
#     andar_reto(500)
    
# cor_vista = "YELLOW"
# brake_motors()
# ajust_color(cor_vista)
# move_backward(10)

#-----------------------------------------------------------------------------------------------

# Ajustar a distância --------------------------------------------------------------------------

# move_backward(43)

#-----------------------------------------------------------------------------------------------

# Teste de girar o motor -----------------------------------------------------------------------

# while True:
#     left_motor.run(40)
#     right_motor.run(-30)


# while True:
#     print(tube_sensor.distance())