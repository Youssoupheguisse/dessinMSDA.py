# Polygone paramétrable (Pentagone, Octogone…)
cote=int(input("entre le nombre de cote"))
from turtle import*
for i in range(cote):
         forward(200)
         left(360/cote)