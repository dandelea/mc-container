import argparse
import json
import numpy as np

from Numberjack import *

def run(filepath):
	with open(filepath) as data_file:
		data = json.load(data_file)
	total_volume = data['total_volume']
	objects = data['objects']

	print("Capacidad del contenedor: " +str(total_volume))

	volumes = []	# Vector vi (Volumen de objeto i)
	customers = []	# Vector ci (Cliente de objeto i)
	ids = []		# Vector ids (Identificador de objeto i)
	for obj in objects:
		ids.append(obj['id'])
		volumes.append(obj['volume'])
		customers.append(obj['customer'])

	print("---Solución al problema 1---")
	'''
		Restricción: El volumen no puede exceder la capacidad del contenedor.
			sum (vi * xi) <= V
		Función objetivo: Máximo volumen
			F(X): max sum (vi * xi)
	'''
	x = VarArray(len(volumes))	# Vector de variables binarias xi (Objeto i entra en contenedor)
	model = Model(np.sum(np.array(volumes)*np.array(x))<=total_volume)	# Restrictions
	model.add(Maximise(np.sum(np.array(volumes)*np.array(x))))			# Objective function
	solver = model.load("Mistral")
	solver.solve()
	
	print_solution(objects, x)

	print("---Solución al problema 2---")
	'''
		Restricción: El volumen no puede exceder la capacidad del contenedor.
			sum (vi * xi) <= V
		Función objetivo: Máxima cantidad
			F(X): max sum (xi)
	'''
	x = VarArray(len(volumes))	# Vector de variables binarias xi (Objeto i entra en contenedor)
	model = Model(np.sum(np.array(volumes)*np.array(x))<=total_volume)	# Restrictions
	model.add(Maximise(np.sum(np.array(x))))										# Objective function
	solver = model.load("Mistral")
	solver.solve()

	print_solution(objects, x)

def restriction_customer(customers, x):
	customers = np.array(customers)
	result = True
	for c in customers:
		ind = np.where(customers==c)[0]
		x_ind = np.take(x, ind)
		print(type(result))
		result &= bool(((x_ind==1).all() or (x_ind==0).all()))
	return result

def print_solution(objects, x):
	for i in range(0,len(x)):
		objects[i]['in_container'] = x[i].__str__()=='1'
		print(objects[i])
	return objects

if __name__=='__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument("-p", "--path", required=True, help="Path to scenario JSON file")
	args = vars(ap.parse_args())
	run(args['path'])