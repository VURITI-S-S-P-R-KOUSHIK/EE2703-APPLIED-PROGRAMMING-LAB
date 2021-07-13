# importing modules.
from pylab import *
import scipy.signal as sp

# The time response of the spring with decay 0.5 and the its plot.

H1 = poly1d([1,0.5])
F1 = polymul([1,1,2.5],[1,0,2.25])
X1 = sp.lti(H1,F1)
t1,x1 = sp.impulse(X1,None,linspace(0,50,1000))


figure(0)
plot(t1,x1)
title(" X(t) for decay of 0.5")
xlabel(r'$t\rightarrow$')
ylabel(r'$x(t)\rightarrow$')
grid(True)

# The time response of the spring with decay 0.05 and the its plot.

H2 = poly1d([1,0.05])
F2 = polymul([1,0.1,2.2525],[1,0,2.25])
X2 = sp.lti(H2,F2)
t2,x2 = sp.impulse(X2,None,linspace(0,50,1000))


figure(1)
plot(t2,x2)
title("X(t) for smaller decay of 0.05")
xlabel(r'$t\rightarrow$')
ylabel(r'$x(t)\rightarrow$')
grid(True)

# find system Transfer function and find responses for by varing frequency from 1.4 to 1.6 and the plots.

H = sp.lti([1],[1,0,2.25])
for omega in arange(1.4,1.6,0.05):
	t3 = linspace(0,50,1000)
	f = cos(omega*t3)*exp(-0.05*t3)
	t,x,svec = sp.lsim(H,f,t3)


	figure(2)
	plot(t,x,label='omega = ' + str(omega))
	title("x(t) for different frequencies( omega range from 1.4 to 1.6)")
	xlabel(r'$t\rightarrow$')
	ylabel(r'$X(t)\rightarrow$')
	legend(loc = 'upper left')
	grid(True)
	show()

#To solve coupled spring equation and to find reponse, then inverse laplace tranform by sp.impulse to find the time response.

t4 = linspace(0,20,1000)
H4_x = sp.lti(np.poly1d([1,0,2]),poly1d([1,0,3,0]))
X4 = sp.impulse(H4_x,T=t4)
H4_y = sp.lti(np.poly1d([2]),poly1d([1,0,3,0]))
Y4 = sp.impulse(H4_y,T=t4)
# The plots of time responses X(t) and Y(t).
figure(3)
plot(X4[0],X4[1],label='x(t)')
plot(Y4[0],Y4[1],label='y(t)')
title("X(t) and Y(t)")
xlabel(r'$t\rightarrow$')
ylabel(r'$functions X(t) and Y(t)\rightarrow$')
legend(loc = 'upper right')
grid(True)

#To find the Transfer Equation of two port network  and plotting bode plots of magnitude and phase.
w=1.5
zeta=0
R = 100
L = 1e-6
C = 1e-6

w = 1/sqrt(L*C) 
Q = 1/R * sqrt(L/C)
zeta = 1/(2*Q)

num = poly1d([w**2])
den = poly1d([1,2*w*zeta,w**2])

H = sp.lti(num,den)

w,S,phi=H.bode()

figure(4)
semilogx(w,S)
title("Magnitude Bode plot")
xlabel(r'$\omega\rightarrow$')
ylabel(r'$20\log|H(j\omega)|\rightarrow$')
grid(True)

figure(5)
semilogx(w,phi)
title("Phase Bode plot")
xlabel(r'$\omega\rightarrow$')
ylabel(r'$\angle H(j\omega)\rightarrow$')
grid(True)

t6 = arange(0,30e-6,1e-8)
vi = cos(1e3*t6) - cos(1e6*t6)
t6,vo,svec = sp.lsim(H,vi,t6)

#To Find the output voltage from transfer function and input voltage for short term and long term time intervals.The plots of output voltages.
	
figure(6)
plot(t6,vo)
title("The Output Voltage for short time interval")
xlabel(r'$t\rightarrow$')
ylabel(r'$V_o(t)\rightarrow$')
grid(True)

t7 = arange(0,10e-3,1e-8)
vi = cos(1e3*t7) - cos(1e6*t7)
t7,v_o,svec = sp.lsim(H,vi,t7)

figure(7)
plot(t7,v_o)
title("The Output Voltage for long time interval")
xlabel(r'$t\rightarrow$')
ylabel(r'$V_o(t)\rightarrow$')
grid(True)
show()	
