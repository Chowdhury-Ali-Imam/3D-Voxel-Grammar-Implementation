

import rhinoscriptsyntax as rs
import itertools
import random 
import time 

#user inputs for voxel data

initial_shape = rs.GetObject ('select a voxel. currently the code is supporting only (1x1x1) resolution. A 1mm x 1mm x 1mm voxel is suggested')
voxel_length = rs.GetInteger('specify the length of the voxel')
voxels = []

#user inputs for massing rule sequence

rule_sequence = rs.GetString('enter a list of rule sequence separated by comma')
rule_list = rule_sequence.split (",")
rule_list = [ int (num) for num in rule_list ]

#user inputs for courtyard rule sequence

court_rule_sequence = rs.GetString('enter a list of court_rule sequence separated by comma. Use Capital Letters')
court_rule_list = court_rule_sequence.split (",")
court_rule_list = [str (string) for string in court_rule_list]

# define function for voxel array

def voxel_array(location,x,y,z):

    for i in range(location[0],x,voxel_length):
        for j in range(location[1],y,voxel_length):
            for k in range(location[2],z,voxel_length):
                voxel_coord = (i,j,k)
                voxel = rs.CopyObject(initial_shape, voxel_coord)
                voxels.append (voxel)

#Calling the function for a 3D array of voxels

voxel_array ((0,0,0),3,3,1)

#Defining the base mass by copying the array

point_A = (0,0,0)
point_A = (0, 0, 0)
vector_1 = rs.VectorCreate(point_A, point_A)
base_mass = rs.CopyObjects(voxels,vector_1)

#Initial Setup for the for loop

x=0
y=0
z=0
position = (x,y,z)

#mass_list will contain the solid mass without any perforation.

mass_list = []

#mass_Delete is the list from where I will delete the voxels to form courtyards
#separate list was required because if I delete from the mass_list, it will contain the perforation in the next iteration-  
#-which is unwanted. Therefore, the mass_list will be stored in layers and the layers will be deleted later. Thus, the-
#-mass_list will continue to copy each iteration till the last one. And mass_delete will carry on the creation of courts 

mass_Delete = []

#rule definition and application (the for loop is working for the two rule list simultaneously

for (rule, court_rule) in itertools.izip_longest(rule_list,court_rule_list) :

#sleep function to delay the rule application so that we can better understand the
#generation process while making any video

        time.sleep (0.5)
        if (rule, court_rule) == (1, 'A'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete

            #rule-A has no courtyards. therefore no deletition of voxels. bu, need to copy the mass
            
            
        elif (rule, court_rule) == (1, 'B'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])
            
            
        elif (rule, court_rule) == (1, 'C'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])
            
        elif (rule, court_rule) == (1, 'D'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2])
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2])
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2])
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2])
                
            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass 
            rs.AddLayer(name = 'Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer')
             
            #Deleting voxels from the mass to form court
            #mass_Copy_To_Delete is copying the mass. From this copied mass, the voxels will be deleted.
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])


        elif (rule, court_rule) == (2, 'A'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            mass_Delete[0:9] = mass_Copy_To_Delete
            

        elif (rule, court_rule) == (2, 'B'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])

        elif (rule, court_rule) == (2, 'C'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])
            

        elif (rule, court_rule) == (2, 'D'):

            #randomness for copying mass in each of the 4 sides

            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+3, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-3, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+3, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-3, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer1')
            
            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer1', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer1')
            rs.DeleteObject(mass_Delete[4])

        elif (rule, court_rule) == (3, 'A'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
           
            
            
        elif (rule, court_rule) == (3, 'B'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])
            

        elif (rule, court_rule) == (3, 'C'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])

        elif (rule, court_rule) == (3, 'D'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1], position [2]+1)
            elif random_number == 2:
                point_A = (position[0]-1, position[1], position [2]+1)
            elif random_number == 3:
                point_A = (position[0], position[1]+1, position [2]+1)
            elif random_number == 4:
                point_A = (position[0], position[1]-1, position [2]+1)

            #copying the mass
            
            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer2')

            #Deleting voxels from the mass to form court

            mass_Copy_To_Delete =rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer2', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete, layer='Del_Layer2')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])

        elif (rule, court_rule) == (4, 'A'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            
            
        elif (rule, court_rule) == (4, 'B'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])
            rs.DeleteObject(mass_Delete[5])
            rs.DeleteObject(mass_Delete[7])
            rs.DeleteObject(mass_Delete[8])
            
            
        elif (rule, court_rule) == (4, 'C'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[1])
            rs.DeleteObject(mass_Delete[4])


        elif (rule, court_rule) == (4, 'D'):
             
            #randomness for copying mass in each of the 4 sides
            
            random_number = random.randint (0,4)
            if random_number == 1:
                point_A = (position[0]+1, position[1]+1, position [2])
            elif random_number == 2:
                point_A = (position[0]-1, position[1]+1, position [2])
            elif random_number == 3:
                point_A = (position[0]-1, position[1]-1, position [2])
            elif random_number == 4:
                point_A = (position[0]+1, position[1]-1, position [2])

            #copying the mass

            vector_A = rs.VectorCreate(point_A, position)
            new_mass = rs.CopyObjects(base_mass,vector_A)
            mass_list [0:9] = new_mass
            rs.AddLayer(name = 'Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(new_mass, layer='Layer3')
            
            #Deleting voxels from the mass to form court
            
            mass_Copy_To_Delete = rs.CopyObjects(new_mass,translation=None)
            rs.AddLayer(name = 'Del_Layer3', visible=True, locked=False, parent=None)
            rs.ObjectLayer(mass_Copy_To_Delete , layer='Del_Layer3')
            mass_Delete[0:9] = mass_Copy_To_Delete
            rs.DeleteObject(mass_Delete[4])

        #updating the location the location for copying objects after each iteration

        rs.EnableObjectGrips (mass_list[0], True)
        new_position =  rs.ObjectGripLocation(mass_list[0],0)
        x= int (new_position [0])
        y= int (new_position [1])
        z= int (new_position [2])
        position = (x,y,z)
         
        #updating the mass to be copied
        base_mass = mass_list[0:9]
         
#Deleting the duplicate voxels. 

rs.PurgeLayer('Layer')
rs.PurgeLayer('Layer1')
rs.PurgeLayer('Layer2')
rs.PurgeLayer('Layer3')

#redrawing

rs.EnableRedraw (True)
rs.Redraw ()