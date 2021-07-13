#import modules for the code.
from pylab import *
import scipy.special as ss

#Creating the function.

def g(t,A,B):								#defining the function.
	return A*ss.jn(2,t) + B*t					#let the function return to value.

	
	
data = loadtxt("fitting.dat")						#load data from a fitting.dat for better reading the file.

t = data[:,0]								#Assigning the first coloum of data as t(that actually refers to time).
d = data[:,1]								#Assigning the second coloum of data as d(that actually is value of f(t))

#Calling of the function with A and B values are 1.05 and -0.105 respectively

ft = g(t,1.05,-0.105)							#By taking the values from data's first coloum, find the values of the function and assign to ft.
stdev = logspace(-1,-3,9)						#Assigning the the standard deviations as given in questions.

#plotting the actual plot with 9 other noisy plots.

figure(0)								#naming as figure(0).
for i in range(1,10):							# i from 1 to 9		
	plot(t,data[:,i],label="σ=%.4f"%stdev[i-1])			#This is plotting of 9 noisy plots and to show the σ value corresponding to that plot.
plot(t,ft,label="True Value",color='black',linewidth=2)		#This is plotting of actual function by labelling true value with color black and linewidth 2 units.	
title("Q4:Data to be fitted to theory",size=20)			#The plot heading is given with size of 20 units.	
xlabel(r'$t\rightarrow$',size=20)					#The x-axis is labeled.
ylabel(r'$f(t)+n(t)\rightarrow$',size=20)				#The y-axis is labeled.
grid(True)								#To add grid lines to the plot.
legend()								#Describing the elements of the graph.

#plotting the error plot in the first set of data as compared to the actual plot.

stdev0 = 0.10								# Assigning the first standard deviation value to stdev0.
figure(1)								#naming as figure(1).
plot(t,ft,label="True Value",color='black',linewidth=2)		#This is plotting of actual function by labelling true value with color black and linewidth 2 units.
errorbar(t[::5],d[::5],stdev0,fmt='ro',label='Noise')		#Plotting errorbar for every 5th data item with colour of red and with point, labeled it as noise.
title("Q5:Data with Error Bars and exact function",size=20)		#The plot title is given with 20 units size.	
xlabel(r'$t\rightarrow$',size=20)					#The x-axis is labeled.
ylabel(r'$f(t)+n\rightarrow$',size=20)				#The y-axis is labeled.
grid(True)								#To add the grid lines to the plot.
legend()								#Describing the elements of the graph.

#Calculating the matrix M, finding matrix Q i.e M*p, checking whether is equal to g(t,A0,B0) asked in Q6.

n,m= data.shape							#Finding the rows and coloums of the data and assigning it to n,m.
M = empty((n,2))							#Initialising the Matrix M with dimensions as rows of data *2.
for i in range(n):							#i from 1 to n.
	M[i] = (ss.jn(2,t[i]),t[i])					#Filling the matrix.

P = array([1.05,-0.105])						#as A=1.05 and B=-0.105 make an array.
Q = dot(M,P)								#multiplication of matrix M and P.

if array_equal(Q,ft):							#If arrays Q and ft are equal  
	print("The two vectors are equal.")				#print as equal.
else:									#else print as not equal.
	print("The two vectors are not equal.")
	
#calculating the mean squared error for different values of A and B.
	
A = array([0.1*i for i in range(21)])					#Assigning the array A as A=0,0.1, . . . ,2.
B = array([-0.2+0.01*i for i in range(21)])				#Assigning the array B as B=−0.2,−0.19, . . . ,0.
E = zeros((21,21))							#Initialising the Matrix E with dimensions of 21*21 with all zeroes.
for i in range(21):							#i from 1 to 20.
	for j in range(21):						#j from 1 to 20.
		for k in range (n):					#k from 1 to n.
			E[i][j] += ((d[k] - g(t[k],A[i],B[j]))**2/n)	#εij= (∑k=0(fk−g(tk,Ai,Bj))**2)/n are assigned accordingly to corresponding Eij
			
K,L = meshgrid(A,B)							#Creating a rectangular grid out of two given one-dimensional arrays A and B representing the Matrix indexing to K,L.

#plotting the contour of mean squared error for different values of A and B.

figure(2)								#naming as figure(2)
Ct=contour(K,L,E,20)							#Plotting the contour plot.
clabel(Ct,Ct.levels[:5],inline=1,fontsize=10)				#labeling,fontsize and levels are assigned.
title("Q8:Contour Plot of εij",size=20)				#The plot title is given with 20 units size.					
xlabel(r'$A\rightarrow$',size=20)					#The x-axis is labeled.
ylabel(r'$B\rightarrow$',size=20)					#The y-axis is labeled.

#Calculating the error in the estimate of A and B.

Ea = empty((9,1))							#Initialising the Matrix Ea with dimensions 9*1.
Eb = empty((9,1))							#Initialising the Matrix Eb with dimensions 9*1.
for i in range(9):							#i from 1 to 8
	
	F = linalg.lstsq(M,data[:,i+1],rcond=None)			#By lstsq finding P vector for some data value out of 9.
	Ea[i] = abs(F[0][0]-P[0])					#Finding the absolute value of difference of that P vector's 1st value value with 1.05.
	Eb[i] = abs(F[0][1]-P[1])					#Finding the absolute value of difference of that P vector's 2nd value value with -0.105.

#Plotting the variation of error in the estimate of A and B with respect to noise.
	
figure(3)								#naming as figure(3)
plot(stdev,Ea,label='Aerr',marker='o',linestyle='dashed')		#Plotting Ea vs stdev with point and dashed lines. 
plot(stdev,Eb,label='Berr',marker='o',linestyle='dashed')		#Plotting Eb vs stdev with point and dashed lines.
title("Q10:Variation of Error with Noise",size=20)			#The plot title is given with 20 units size.	
xlabel(r'$Noise standard deviation\rightarrow$',size=20)		#The x-axis is labeled.
ylabel(r'$MS error\rightarrow$',size=20)				#The y-axis is labeled.
grid(True)								#To add the grid lines to the plot.
legend()								#Describing the elements of the graph.

#plotting the variation of error in the estimate of A and B with respect to noise in log scale.

figure(4)								#naming as figure(4)
loglog(stdev,Ea,'ro',label='Aerr',)					#Plotting the loglog plot of Ea vs stdev and label with 'Aerr'
errorbar(logspace(-1, -3, 9), Ea, std(Ea), fmt='ro')			#Plotting errorbar with red colour.
loglog(stdev,Eb,'go',label='Berr')					#Plotting the loglog plot of Eb vs stdev and label with 'Berr'
errorbar(logspace(-1, -3, 9), Eb, std(Eb), fmt='go')			#Plotting errorbar with green colour.
title("Q11:Variation of Error with Noise",size=20)			#The plot title is given with 20 units size.	
xlabel(r'$σn\rightarrow$',size=20)					#The x-axis is labeled.
ylabel(r'$MS error\rightarrow$',size=20)				#The y-axis is labeled.
grid(True)								#To add the grid lines to the plot.
legend()								#Describing the elements of the graph.
show()									#To dispaly all the graph in above.


	
	






 


