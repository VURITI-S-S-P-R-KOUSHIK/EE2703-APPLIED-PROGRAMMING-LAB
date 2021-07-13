#import modules for the code.
from pylab import *									#importing pylab
from scipy import integrate								#importing scipy.integrate as integrate
from numpy import transpose								#importing numpy.transpose as transpose

#Creating the functions for the code.

def F(x):										#defining the function F(x).
	return exp(x)									#Returning the value to exp(x)

def G(x):										#defining the function G(x).
	return cos(cos(x))								#Returning the value to coscos(x)
	
def u_exp(x,k):									#defining the function u_exp(x,k).									
	return F(x)*cos(k*x)								#Returning the value to F(x)*cos(k*x)

def v_exp(x,k):									#defining the function v_exp(x,k).
	return F(x)*sin(k*x)								#Returning the value to F(x)*sin(k*x)

def u_coscos(x,k):									#defining the function u_coscos(x,k)
	return G(x)*cos(k*x)								#Returning the value to G(x)*cos(k*x)
	
def v_coscos(x,k):									#defining the function v_coscos(x,k)
	return G(x)*sin(k*x)								#Returning the value to G(x)*sin(k*x)

x=linspace(-2*pi,4*pi,1200)								#assignes 1200values in between -2*pi to 4*pi
xt = linspace(0,2*pi,400)								#assigning values for xt from 0 to 2*pi,400 values
t = tile(xt,3)										#Using tile function

#Finding the coefficients of fourier series by integration and assigning to matrix.
											
C_exp = zeros((51,1))									#initialising C_exp array for fourier coefficients of exp(x)
C_exp[0][0] = (1/(2*pi))*(integrate.quad(F,0,2*pi))[0]				#giving value for C_exp[0][0]				
for k in range(1,26):									#k values from 1 to 25
	C_exp[2*k-1][0] = (1/pi)*(integrate.quad(u_exp,0,2*pi,args=(k)))[0]		#assigning an coefficients for odd terms of matrix
	C_exp[2*k][0] = (1/pi)*(integrate.quad(v_exp,0,2*pi,args=(k)))[0]		#assigning bn coefficients for even terms of matrix

C_coscos = zeros((51,1))								#initialising C_coscos array for fourier coefficients of cos(cos(x))
C_coscos[0][0] = (1/(2*pi))*(integrate.quad(G,0,2*pi))[0]				#giving value for C_coscos[0][0]
for k in range(1,26):									#k values from 1 to 25									
	C_coscos[2*k-1][0] = (1/pi)*(integrate.quad(u_coscos,0,2*pi,args=(k)))[0]	#assigning an coefficients for odd terms of matrix
	C_coscos[2*k][0] = (1/pi)*(integrate.quad(v_coscos,0,2*pi,args=(k)))[0]	#assigning bn coefficients for even terms of matrix

#creating the matrix A.

n = arange(1,52)									#Using arange function 
xl=linspace(0,2*pi,401)								#assigning values for xl from 0 to 2*pi,401 values
xl=xl[:-1]										#excluding the last value i.e 4*pi
B_exp = F(xl)										#assigning the F(x) values where x are equal to xl
B_coscos = G(xl)									#assigning the G(x) values where x equals xl									
A = zeros((400,51))									#initialising the matrix A of size 400*51.
A[:,0] = 1										#column1 in matrixA are all ones
for k in range(1,26):									#k values from 1 to 25
	A[:,2*k-1] = cos(k*xl)								#odd coloums are assigned with cos(kx)
	A[:,2*k] = sin(k*xl)								#even coloums are assigned with sin(kx)
c_exp = lstsq(A,B_exp,rcond=None)[0]							#estimating fourier coefficients of exp(x) by lstsq function 
c_coscos = lstsq(A,B_coscos,rcond=None)[0]						#estimating fourier coefficients of cos(cos(x)) by lstsq function
ct_exp = transpose(C_exp)								#transpose of C_exp matrix
ct_coscos = transpose(C_coscos)							#transpose of C_coscos matrix

#Finding the absolute difference between calculated and estimated fourier coefficients and finding the largest deviation.

Absdiff_exp = abs(c_exp - ct_exp)							#absolute difference between calculated and estimated fourier coefficients of exp(x)
Absdiff_coscos = abs(c_coscos - ct_coscos)						#absolute difference between calculated and estimated fourier coefficients of cos(cosx)

lar_dev_exp = max(Absdiff_exp[0])							#largest deviation in fourier coefficients of exp(x)
lar_dev_coscos = max(Absdiff_coscos[0])						#largest deviation in fourier coefficients of cos(cos(x))

print("The largest deviation between coefficients for exp() is ",lar_dev_exp)	#printing largest deviation value for fourier coefficients of exp(x)
print("The largest deviation between coefficients for coscos() is ",lar_dev_coscos)	#printing largest deviation value for fourier coefficients of cos(cos(x))	


cl_exp = dot(A,c_exp)									#Estimated exp(x) function
cl_coscos = dot(A,c_coscos)								#Estimated cos(cosx) function					


figure(1)										#naming as figure(1)
semilogy(x,F(x),'r',label='true value')						#plotting semilog for exp(x) function
semilogy(x,F(t),'-b',label='Periodic extension')					#plotting semilog for periodic extension of exp(x) function
semilogy(xt,cl_exp,'go',label='estimated value')					#plotting semilog for estimated exp(x) function
title("Semilog plot of $e^{x}$ function")									#The plot is titled
xlabel(r'$x\rightarrow$',size=15)							#labelling x-axis
ylabel(r'$e^x\rightarrow$',size=15)							#labelling y-axis
grid(True)										#To add the grid lines to the plot
legend()										#Describing the elements of the graph


	
figure(2)										#naming as figure(2)
plot(x,G(x),'r',label='true value')							#plotting cos(cos(x)) function
plot(x,G(t),'-b',label='Periodic extension')						#plotting fourier function of cos(cos(x)) function
plot(xt,cl_coscos,'go',label='estimated value')					#plotting estimated cos(cos(x)) function
title("plot of cos(cos(x)) function")									#The plot is titled
xlabel(r'$x\rightarrow$',size=15)							#labelling x-axis
ylabel(r'$cos(cos(x))\rightarrow$',size=15)						#labelling y-axis
grid(True)										#To add the grid lines to the plot
legend()										#Describing the elements of the graph

figure(3)										#naming as figure(3)
semilogy(n,abs(C_exp),'ro',label='direct integration')				#semilog plot of magnitude of integrated fourier coefficients for exp(x)
semilogy(n,abs(c_exp),'go',label='Least Squares approach')				#semilog plot of magnitude of estimated fourier coefficients for exp(x)
title("Semilog Plot of coefficients for $e^{x}$")					#the plot is titled
xlabel(r'$n\rightarrow$',size=15)							#labelling x-axis
ylabel('Magnitude of coefficients for $e^{x}$ ',size=15)				#labelling y-axis
grid(True)										#To add the grid lines to the plot
legend()										#Describing the elements of the graph

figure(4)										#naming as figure(4)
loglog(n,abs(C_exp),'ro',label='direct integration')					#loglog plot of magnitude of integrated fourier coefficients for exp(x)
loglog(n,abs(c_exp),'go',label='Least Squares approach')				#loglog plot of magnitude of estimated fourier coefficients for exp(x)
title("Loglog Plot of coefficients of $e^{x}$")					#the plot is titled
xlabel(r'$n\rightarrow$',size=15)							#labelling x-axis
ylabel('Magnitude of coefficients for $e^{x}$',size=15)				#labelling y-axis
grid(True)										#To add the grid lines to the plot
legend()										#Describing the elements of the graph

figure(5)										#naming as figure(5)
semilogy(n,abs(C_coscos),'ro',label='direct integration')				#semilog plot of magnitude of integrated fourier coefficients for cos(cos(x))
semilogy(n,abs(c_coscos),'go',label='Least Squares approach')			#semilog plot of magnitude of estimated fourier coefficients for cos(cos(x))
title("Semilog Plot of coefficients for cos(cos(x))")				#the plot is titled
xlabel(r'$n\rightarrow$',size=15)							#labelling x-axis
ylabel('Magnitude of coefficients for cos(cos(x)) ',size=15)				#labelling y-axis
grid(True)										#To add the grid lines to the plot
legend()										#Describing the elements of the graph

figure(6)										#naming as figure(6)
loglog(n,abs(C_coscos),'ro',label='direct integration')				#loglog plot of magnitude of integrated fourier coefficients for cos(cos(x))
loglog(n,abs(c_coscos),'go',label='Least Squares approach')				#loglog plot of magnitude of estimated fourier coefficients for cos(cos(x))
title("Loglog Plot of coefficients of cos(cos(x))")					#the plot is titled
xlabel(r'$n\rightarrow$',size=15)							#labelling x-axis
ylabel('Magnitude of coefficients for cos(cos(x))',size=15)				#labelling y-axis
grid(True)										#To add the grid lines to the plot
legend()										#Describing the elements of the graph
show()											#To dispaly all the graph in above
