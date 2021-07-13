# V.S.S.P.R.Koushik;EE19B061

# Importing the modules
import pylab as py				# pylab module is imported as py.
import numpy as np				# numpy module is imported as np. 				
# Question 1 is discussed in report.
# Initialising necessary variables.
N=100						# N is the no. of parts the loop should be broken. As per question, it is 100.
a=10						# a is the radius of the loop. It is given 10.
# Question 2
# Breaking the volume into a 3 by 3 by 1000mesh,with mesh points separated by 1cm.
x=np.linspace(-1,1,3)				# x is assigned 3 points from -1 to 1 seperated by 1 cm.
y=np.linspace(-1,1,3)				# y is assigned 3 points from -1 to 1 seperated by 1 cm.
z=np.arange(1,1001,1)				# z is assigned 1000 points from 1 to 1000 seperated by 1cm.
X,Y,Z=np.meshgrid(x,y,z)			# Breaking the volume into a 3 by 3 by 1000 mesh.
rijk =np.zeros((3,3,1000,3))			# rijk is numpy array that have 9000 set of points.
rijk[:,:,:,0]=X					# x coordinate of rijk is stored in X.
rijk[:,:,:,1]=Y					# y coordinate of rijk is stored in Y.
rijk[:,:,:,2]=Z					# z coordinate of rijk is stored in Z.
# Question 3
# Break the loop into 100 sections.						
phil=np.linspace(0,2*np.pi,101)			# phil is the angle made by lth part of loop with origin.			
phil=phil[:-1]					# remove the 101th value.

I=np.zeros((2,N))				# initialising an array with 2 rows and 100 columns for current values.					 	
r=np.zeros((2,N))				# initialising an array with 2 rows and 100 columns for position values.	
I[0]=-1e7*((np.cos(phil)))*(np.sin(phil))	# x component of current for each element.		
I[1]=1e7*((np.cos(phil)))*(np.cos(phil))	# y component of current for each element.		
r[0]=a*(np.cos(phil))				# x component of position for each current element.				
r[1]=a*(np.sin(phil))				# y component of position for each current element.				
# Plot the current elements in x−y placepoints at the centre points of the elements. Properly label the graph.
py.figure(0)					# creating and naming the figure window		 
py.quiver(r[0],r[1],I[0],I[1],scale=1e8,label='current vectors')# plotting the current vectors using quiver function		 
py.xlabel('X $\longrightarrow$ ')		# naming x-label to the plot
py.ylabel('Y $\longrightarrow$ ')		# naming y-label to the plot
py.title('Current Flow Through The Loop')       # giving title to the plot
py.axis('square')                               # displaying square axes
py.grid('True')                                 # enabling grid in the axes
py.legend ()                                    # describing the elements of the plot
py.figure(1)                                    # creating and naming the figure window
py.plot(r[0],r[1],'bo',label='current elements')# plotting the current elements
py.xlabel('X $\longrightarrow$ ')		# naming x-label to the plot	 
py.ylabel('Y $\longrightarrow$ ')		# naming y-label to the plot	 
py.title('Current Elements In The Loop') 	# giving title to the plot
py.axis('square')				# displaying square axes
py.grid('True')					# enabling grid in the axes
py.legend()                                     # describing the elements of the plot
py.show()					# displaying the output plot					 
# Question 4
# Obtain the vectors rl,dl, where l indexes the segments of the loop.
dl = np.zeros((2,N))				# Initialising the dl vector with all place zeros
rl=np.c_[a*(np.cos(phil)),a*(np.sin(phil)),np.zeros(N)]# defining the rl vector
dl[0] = -(2*np.pi*a/N)*np.sin(phil)		# x coordinate of dl vector
dl[1] = (2*np.pi*a/N)*np.cos(phil)		# y coordinate of dl vector
k=0.1						# assigning k equal to 0.1 given in question.
# Question 5
# Define a functioncalc(l)that calculates and returns Rijkl=∣∣rijk−rl∣∣for all rijk
# Question 6
# Extend calc to generate the terms in Eq. 1 in the sum and return the termto add to A.
def calc(l):					# defining the function calc
    Rijkl=np.linalg.norm(rijk-rl[l],axis=-1)	# finding Rijkl i.e the norm ∣∣rijk−rl∣∣
    Axl=((np.cos(phil[l]))*np.exp((-1j)*k*(Rijkl))*(dl[0][l]))/Rijkl# Defining the x component of magnetic potential(A) where the current values are taken.
    Ayl=((np.cos(phil[l]))*np.exp((-1j)*k*(Rijkl))*(dl[1][l]))/Rijkl# Defining the y component of magnetic potential(A) where the current values are taken.
    Axl1=(np.abs(np.cos(phil[l]))*np.exp((-1j)*k*(Rijkl))*(dl[0][l]))/Rijkl# Defining the x component of magnetic potential(A) where absolute values of current.
    Ayl1=(np.abs(np.cos(phil[l]))*np.exp((-1j)*k*(Rijkl))*(dl[1][l]))/Rijkl# Defining the y component of magnetic potential(A) where absolute values of current.
    return Axl,Ayl,Axl1,Ayl1				# when the function is called, then these values return.
Axl=Ayl=0					# assigning both the initial values of x and y components of magnetic potential(I) to 0.
Axl1=Ayl1=0					# assigning both the initial values of x and y components of magnetic potential(|I|) to 0.
# Question 7
# Use the function to compute Aijk
for i in range(N):				# for i value ranging from 1 to N.
    dxl,dyl,dxl1,dyl1=calc(i)			# calling the calc function for every value from 1 to N.
    Axl+=dxl					# incrementing Axl
    Ayl+=dyl					# incrementing Ayl
    Axl1+=dxl1					# incrementing Axl1
    Ayl1+=dyl1					# incrementing Ayl1
# Question 8
# Now compute B along the z-axis. Use Eq. 2; remember to vectorize.
Bz=(Ayl[1,2,:]-Ayl[1,0,:]-(Axl[2,1,:]-Axl[0,1,:]))/4# computing the Bz values by vectorized operation given in question.
Bz1=(Ayl1[1,2,:]-Ayl1[1,0,:]-(Axl1[2,1,:]-Axl1[0,1,:]))/4# computing the Bz1 values by vectorized operation given in question.
# Question 9
# Plot the magnetic field Bz(z). Use a log-log plot.
py.figure(2)					# creating and naming the figure window
py.loglog(z,np.abs(Bz),label= 'Magnetic Field Bz')# plotting Bz vs z in loglog plot
py.xlabel('z $\longrightarrow$ ')		# naming x-label to the plot
py.ylabel('Bz $\longrightarrow$ ')		# naming y-label to the plot
py.title('Magnetic Field Variation w.r.to z')	# giving title to the plot
py.grid('True')					# enabling grid in the axes
py.legend()					# describing the elements of the plot
py.show()					# displaying the output plot
py.figure(3)					# creating and naming the figure window
py.loglog(z,np.abs(Bz1),label= 'Magnetic Field Bz')# plotting Bz1 vs z in loglog plot
py.xlabel('z $\longrightarrow$ ')		# naming x-label to the plot
py.ylabel('Bz $\longrightarrow$ ')		# naming y-label to the plot
py.title('Magnetic Field Variation w.r.to z')	# giving title to the plot
py.grid('True')					# enabling grid in the axes
py.legend()					# describing the elements of the plot
py.show()					# displaying the output plot
# Question 10
# Fit the field to a fit of the type Bz≈cz^b
def estimate(data):				# defining the estimate function to find the best fit values of c,b
    M=np.c_[np.ones(len(data)),np.log(np.arange(1001-len(data),1001,1))]# assigning the values to the matrix.
    est=np.linalg.lstsq(M,np.log(data),rcond=None)[0]#using np.linal.lstsq for obtaining best fit values
    return np.exp(est[0]),est[1]		# returning the required quantities c,b
c,b = estimate(np.abs(Bz))			# calling the estimate function.
print('best fit value of c :',c)		# printing the best fit value of c when current values are taken to compute Bz.
print('best fit value of b :',b)		# printing the best fit value of b when current values are taken to compute Bz.
c_abs,b_abs = estimate(np.abs(Bz1))		# calling the estimate function
print('best fit value of c1 :',c_abs)		# printing the best fit value of c when absolute values of current are taken to compute Bz.
print('best fit value of b1 :',b_abs)		# printing the best fit value of b when absolute values of current are taken to compute Bz.
# Question 11 is discussed in the report.'''
