#Подключение библиотек
from ursina import *
import os
import random

app = Ursina()
camera.ortographic = True
camera.fov = 40
counter = 0

#Добавление модельки игрока
car = Entity(
	model='quad',
	texture='assets/car2.png',
	collider='box',
	scale=(2,1),
	rotation_z=-90
	)

#Добавление бэкграунда(дороги)
road1 = Entity(
	model='quad',
	texture='assets/roadnew.png',
	scale=15,
	z=1
	)

#Добавление эффекта бесконечной дороги
road2 = duplicate(road1, y=15)
pair = [road1, road2]


#Добавление машин-припятствий
enemies = []
def newEnemy():
	"""

	:return: has no return
	"""

	val = random.uniform(-2,2)

	new = duplicate(
		car,
		texture='assets/car3.png',
		x = 2*val,
		y = 25,
		color = color.random_color(),
		rotation_z = 
		90 if val < 0
			else -90
		)

	enemies.append(new)
	invoke(newEnemy, delay=0.5)

newEnemy()

#Добавление механики движения WASD
def update():
	"""

	:return: has no return
	"""
	car.x -=held_keys['a']*5*time.dt
	car.x +=held_keys['d']*5*time.dt
	car.y +=held_keys['w']*3*time.dt
	car.y -=held_keys['s']*3*time.dt

	#Добавление эффекта движения дороги
	for road in pair:

		road.y -= 6 * time.dt

		if road.y < -15:
			road.y += 30

	#Движение других машин
	for enemy in enemies:

		if enemy.x < 0:
			enemy.y -= 10 * time.dt

		else:
			enemy.y -= 5 * time.dt

		if enemy.y < -10:
			enemies.remove(enemy)
			destroy(enemy)

	#Добавление эффекта тряски при столкновениях
	if car.intersects().hit:
		os.startfile('Game Over.py')
		quit()

app.run()