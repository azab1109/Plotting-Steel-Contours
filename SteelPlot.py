<<<<<<< HEAD
#Program to plot steel thickness data from a csv file on a contour plot.

#Imports
import pandas as pd
import numpy
from matplotlib import ticker
from matplotlib import pyplot

#Functions
#Function to import data in csv format and place into an array.
def csv_import(csv_path):
    steel_array=pd.read_csv(csv_path,sep=',',header=0)
    print(steel_array)
    return steel_array

#Function to determine which face of the structure will be mapped.
def direction_choice(steel_array):
    directions=steel_array.f.unique()
    directions_string=",".join(str(x) for x in directions if str(x) != "nan")
    face=input("Input face orientation of Panel (" + directions_string + "): ")
    return face

#Function to determine which panel of the structure will be mapped.  
def panel_choice(face_data): 
    panels=face_data.p.unique()
    panels_string=",".join(str(x) for x in panels if str(x) != "nan")
    panel=input("Input panel ID (" + panels_string + "): ")
    return panel

#Function to extract data for specified panel.
def sort_data_face(steel_array,face):
    face_data=steel_array.loc[steel_array['f']==face,['p','x','y','z']]
    return face_data

def sort_data_panel(face_data,panel):
    data_set=face_data.loc[face_data['p']==panel,['x','y','z']]
    return data_set

#Main code block
#Resetting values of variables used in the program.
steel_array=""
face=""
panel=""
data_set=""

#Calling functions to return user input for data selection and sorting data based on input values.
steel_array=csv_import('D:\\User\\Aaron\\Documents\\GitHub\\Plotting-Steel-Contours\\61_35538_AB_NDT Results.csv')
face=direction_choice(steel_array)
face_data=sort_data_face(steel_array,face)
panel=panel_choice(face_data)
data_set=sort_data_panel(face_data,panel)

#Convert pandas dataframe to numeric values for matplotlib contour map.
x = data_set['x']
pd.to_numeric(x, errors='coerce')
y = data_set['y']
pd.to_numeric(y, errors='coerce')
z = data_set['z']
pd.to_numeric(z, errors='coerce')

#Input of overall panel dimensions for plot extents.
lpanel=input('Enter the length of panel ' + panel + ' on elevation ' + face + ': ')
dpanel=input('Enter the depth of panel ' + panel + ' on elevation ' + face + ': ')

#Plot a contour map showing the steel thickness in relation to x,y coordinates.
contour = pyplot.tricontourf(x,y,z,10,cmap='inferno')
pyplot.title('Steel Wall Thickness of Panel ' + panel + ' on elevation ' + face)
pyplot.colorbar(contour)
pyplot.xlabel('Position Along Length of Panel')
pyplot.xlim(0,float(lpanel))
pyplot.ylabel('Position Along Depth of Panel')
pyplot.ylim(-float(dpanel),0)
pyplot.show()
=======
#Program to plot steel thickness data from a csv file on a contour plot.

#Imports
import pandas as pd
import numpy
from matplotlib import ticker
from matplotlib import pyplot

#Functions
#Function to import data in csv format and place into an array.
def csv_import(csv_path):
    steel_array=pd.read_csv(csv_path,sep=',',header=0)
    print(steel_array)
    return steel_array

#Function to determine which face of the structure will be mapped.
def direction_choice(steel_array):
    directions=steel_array.f.unique()
    directions_string=",".join(str(x) for x in directions if str(x) != "nan")
    face=input("Input face orientation of Panel (" + directions_string + "): ")
    return face

#Function to determine which panel of the structure will be mapped.  
def panel_choice(face_data): 
    panels=face_data.p.unique()
    panels_string=",".join(str(x) for x in panels if str(x) != "nan")
    panel=input("Input panel ID (" + panels_string + "): ")
    return panel

#Function to extract data for specified panel.
def sort_data_face(steel_array,face):
    face_data=steel_array.loc[steel_array['f']==face,['p','x','y','z']]
    return face_data

def sort_data_panel(face_data,panel):
    data_set=face_data.loc[face_data['p']==panel,['x','y','z']]
    return data_set

#Main code block
#Resetting values of variables used in the program.
steel_array=""
face=""
panel=""
data_set=""

#Calling functions to return user input for data selection and sorting data based on input values.
steel_array=csv_import('D:\\User\\Aaron\\Documents\\GitHub\\Plotting-Steel-Contours\\61_35538_AB_NDT Results.csv')
face=direction_choice(steel_array)
face_data=sort_data_face(steel_array,face)
panel=panel_choice(face_data)
data_set=sort_data_panel(face_data,panel)

#Convert pandas dataframe to numeric values for matplotlib contour map.
x = data_set['x']
pd.to_numeric(x, errors='coerce')
y = data_set['y']
pd.to_numeric(y, errors='coerce')
z = data_set['z']
pd.to_numeric(z, errors='coerce')

#Input of overall panel dimensions for plot extents.
lpanel=input('Enter the length of panel ' + panel + ' on elevation ' + face + ': ')
dpanel=input('Enter the depth of panel ' + panel + ' on elevation ' + face + ': ')

#Plot a contour map showing the steel thickness in relation to x,y coordinates.
contour = pyplot.tricontourf(x,y,z,10,cmap='inferno')
pyplot.title('Steel Wall Thickness of Panel ' + panel + ' on elevation ' + face)
pyplot.colorbar(contour)
pyplot.xlabel('Position Along Length of Panel')
pyplot.xlim(0,float(lpanel))
pyplot.ylabel('Position Along Depth of Panel')
pyplot.ylim(-float(dpanel),0)
pyplot.show()
>>>>>>> 22b7e5a4792e228f23b4668a2fb7e57259c5ed9f
