# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:14:15 2019

@author: Septian Dewi Cahyani
"""
import numpy as np
import matplotlib
import requests
import bs4
import agentframework_drunks
import matplotlib.animation
import matplotlib.pyplot



#==============================================================================
# Define the Matrix for making the city map
#==============================================================================
city_map = np.zeros([300, 300])
#define size each bulidings
size = range(0, 15)
#define location and build up the pubs (there are  3 pubs)
for i in size:
    for j in size:
        city_map[269+i, 39+j] = 260
        city_map[269+i, 139+j] = 260
        city_map[269+i, 239+j] = 260
#define location and build up the houses (there are  25 houses)
#The houses assign with different numbers (10-250)
for i in size:
    for j in size:
        city_map[23+i, 39+j] = 250
        city_map[23+i, 79+j] = 240
        city_map[23+i, 119+j] = 230
        city_map[23+i, 159+j] = 220
        city_map[23+i, 199+j] = 210
        city_map[23+i, 239+j] = 200
        city_map[63+i, 59+j] = 190
        city_map[63+i, 99+j] = 180
        city_map[63+i, 139+j] = 170
        city_map[63+i, 179+j] = 160
        city_map[63+i, 219+j] = 150
        city_map[103+i, 39+j] = 140
        city_map[103+i, 79+j] = 130
        city_map[103+i, 119+j] = 120
        city_map[103+i, 159+j] = 110
        city_map[103+i, 199+j] = 100
        city_map[103+i, 239+j] = 90
        city_map[143+i, 59+j] = 80
        city_map[143+i, 99+j] = 70
        city_map[143+i, 139+j] = 60
        city_map[143+i, 179+j] = 50
        city_map[143+i, 219+j] = 40
        city_map[183+i, 39+j] = 30
        city_map[183+i, 139+j] = 20
        city_map[183+i, 239+j] = 10
        
path_map = np.zeros([300, 300])
#==============================================================================
# Define the first position of the drunks
#==============================================================================
#open the file that contain first drunks Positions from web
r = requests.get('https://septiandewi.github.io/dataprogrammingseptian.github.io/') #directory for get the data
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
td_Id = soup.find_all(attrs={"class" : "Id"})
#print(td_ys) #for making sure the code grab the right part of y
#print(td_xs) #for making sure the code grab the right part of x
#print(len(td_ys))#print the lenght of the data from data

num_of_drunks =len(td_ys) #use all of the agents in the data
#num_of_iterations = 10
drunks = [] #making space store the position of the drunks

for i in range(num_of_drunks):
     y = int(td_ys[i].text)#grab y values from file
     x = int(td_xs[i].text)#grab x values from file
     Id = int(td_Id[i].text)#grab Id values from file
     drunks.append(agentframework_drunks.Drunk(city_map, drunks, y, x, Id))#fill the drunks container
     #print ('x',[i],x) #make sure the code grab the right value of x
     #print ('y',[i],y) # make sure the code grab the right values of y
     #print ('Id',[i],Id)#omake sure the code grab the right value of Id 
    
#==============================================================================
# Define activity of the drunks and make the animation of the drunks
#==============================================================================
#set the size of pop up box for showing the animation
#type: %matplotlib qt in IPhython console so the animation will showed up
fig = matplotlib.pyplot.figure(figsize=(10, 10))#set the animation box's size
ax = fig.add_axes([0, 0, 1, 1])

def update(frame_number):
    global carry_on
    fig.clear()
    for i in range(num_of_drunks):
        drunks[i].move()#make the drunks move
        drunks[i].make_path()#make the drunks leave footprints
    matplotlib.pyplot.xlim(00, 299)#set the x axes sizes
    matplotlib.pyplot.ylim(299, 00)#set the y axes sizes
    matplotlib.pyplot.imshow(city_map)
    for i in range(num_of_drunks):
        matplotlib.pyplot.scatter(drunks[i].x,drunks[i].y)#display all the drunks position
    #stopping the animation in certain condition
    for i in range(num_of_drunks):
        if drunks[i].stop():
            carry_on = False
     #export the density map      
    np.savetxt('density_map.txt', city_map, fmt='%.0f')
#set the animation provisions
animation = matplotlib.animation.FuncAnimation(fig, update,frames = drunks[i].stop(), repeat=False)   

matplotlib.pyplot.show()





