# Importing the necessary modules
from sympy import *
from pylab import *

# Calculating the DFT of sin(5t)
x=linspace(0,2*pi,129);x=x[:-1]
y=sin(5*x)
Y0=fftshift(fft(y))/128.0
w0=linspace(-64,63,128)
figure(0)
subplot(2,1,1)
plot(w0,abs(Y0),lw=2)
xlim([-10,10])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\sin(5t)$")
grid(True)
subplot(2,1,2)
plot(w0,angle(Y0),'ro',lw=2)
ii=where(abs(Y0)>1e-3)
plot(w0[ii],angle(Y0[ii]),'go',lw=2)
xlim([-10,10])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$k$",size=16)
grid(True)
show()

# Calculating the DFT of (1 + 0.1cos(t))cos(10t)
t1=linspace(-4*pi,4*pi,513);t1=t1[:-1]
y1=(1+0.1*cos(t1))*cos(10*t1)
Y1=fftshift(fft(y1))/512.0
w1=linspace(-64,64,513);w1=w1[:-1]
figure(1)
subplot(2,1,1)
plot(w1,abs(Y1),lw=2)
xlim([-15,15])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $\left(1+0.1\cos\left(t\right)\right)\cos\left(10t\right)$")
grid(True)
subplot(2,1,2)
plot(w1,angle(Y1),'ro',lw=2)
xlim([-15,15])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()

# Calculating the DFT of cos^3(t)
t2=linspace(-4*pi,4*pi,513);t2=t2[:-1]
y2=(cos(t2))**3
Y2=fftshift(fft(y2))/512.0
w2=linspace(-64,64,513);w2=w2[:-1]
figure(2)
subplot(2,1,1)
plot(w2,abs(Y2),lw=2)
xlim([-15,15])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos^{3}(t)$")
grid(True)
subplot(2,1,2)
plot(w2,angle(Y2),'ro',lw=2)
xlim([-15,15])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()

# Calculating the DFT of sin^3(t)
t3=linspace(-4*pi,4*pi,513);t3=t3[:-1]
y3=(sin(t3))**3
Y3=fftshift(fft(y3))/512.0
w3=linspace(-64,64,513);w3=w3[:-1]
figure(3)
subplot(2,1,1)
plot(w3,abs(Y3),lw=2)
xlim([-15,15])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $sin^{3}(t)$")
grid(True)
subplot(2,1,2)
plot(w3,angle(Y3),'ro',lw=2)
xlim([-15,15])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()

# Calculating the DFT of cos(20t + 5cos(t)) where magnitude is greater than 1e-3.
t4=linspace(-4*pi,4*pi,513);t4=t4[:-1]
y4=cos(20*t4 + 5*cos(t4))
Y4=fftshift(fft(y4))/512.0
w4=linspace(-64,64,513);w4=w4[:-1]
figure(1)
subplot(2,1,1)
plot(w4,abs(Y4),lw=2)
xlim([-30,30])
ylabel(r"$|Y|$",size=16)
title(r"Spectrum of $cos(20t + 5cos(t))$")
grid(True)
subplot(2,1,2)
ii=where(abs(Y4)>1e-3)
plot(w4[ii],angle(Y4[ii]),'go',lw=2)
xlim([-30,30])
ylabel(r"Phase of $Y$",size=16)
xlabel(r"$\omega$",size=16)
grid(True)
show()

# Defining the Functions.
def gauss(x):
    return exp(-0.5*x**2)

def expectedgauss(w):
    return 1/sqrt(2*pi) * exp(-w**2/2)

def estdft(tolerance=1e-6,samples=128,func = gauss,expectedfn = expectedgauss,wlim = 5):
    T = 8*pi
    N = samples
    Yold=0
    err=tolerance+1
    iters = 0
    #iterative loop to find window size
    while err>tolerance:  
        x=linspace(-T/2,T/2,N+1)[:-1]
        w = linspace(-N*pi/T,N*pi/T,N+1)[:-1]
        y = gauss(x)
        Y=fftshift(fft(ifftshift(y)))*T/(2*pi*N)
        err = sum(abs(Y[::2]-Yold))
        Yold = Y
        iters+=1
        T*=2
        N*=2
        

    # Calculating error
    true_error = sum(abs(Y-expectedfn(w)))
    print("True error: ",true_error)
    print("samples = "+str(N)+" time period = pi*"+str(T/pi))

    mag = abs(Y)
    phi = angle(Y)
    phi[where(mag<tolerance)]=0
    
    # plotting estimate output
    figure()
    subplot(2,1,1)
    plot(w,abs(Y),lw=2)
    xlim([-wlim,wlim])
    ylabel('Magnitude',size=16)
    title("Estimate fft of gaussian")
    grid(True)
    subplot(2,1,2)
    plot(w,angle(Y),'ro',lw=2)
    ii=where(abs(Y)>1e-3)
    plot(w[ii],angle(Y[ii]),'go',lw=2)
    xlim([-wlim,wlim])
    ylabel("Phase",size=16)
    xlabel("w",size=16)
    grid(True)
    show()

    #plotting expected output    
    Y_ = expectedfn(w)
    
    mag = abs(Y_)
    phi = angle(Y_)
    phi[where(mag<tolerance)]=0
    
    figure()
    subplot(2,1,1)
    plot(w,abs(Y),lw=2)
    xlim([-wlim,wlim])
    ylabel('Magnitude',size=16)
    title("True fft of gaussian")
    grid(True)
    subplot(2,1,2)
    plot(w,angle(Y),'ro',lw=2)
    ii=where(abs(Y)>1e-3)
    plot(w[ii],angle(Y[ii]),'go',lw=2)
    xlim([-wlim,wlim])
    ylabel("Phase",size=16)
    xlabel("w",size=16)
    grid(True)
    show()

    return


estdft()
