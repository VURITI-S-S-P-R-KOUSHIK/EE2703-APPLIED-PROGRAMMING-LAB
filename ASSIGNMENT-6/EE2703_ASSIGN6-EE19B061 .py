#importing the modulues
from sys import argv
import numpy as np
import matplotlib.pyplot as plt

n=100  # spatial grid size
M=5    # no. of electrons injected per turn
nk=500 # no. of turns to simulate
u0=5   # threshold velocity
p=0.25 # probability that ionization will occur
Msig=1 # Standard deviation

try:
	len(argv)==1 and len(argv)==6
except ioerror:
	print('Invalid:')
	exit(0)
	
if len(argv)==6:
	n=int(argv[1])		# spatial grid size given by user	
	M=int(argv[2])		# no. of electrons injected per turn given by user	
	nk=int(argv[3])	# no. of turns to simulate given by user
	u0=float(argv[4])	# threshold velocity given by user
	p=float(argv[5])	# probability that ionization will occur given by user
	Msig=float(argv[6])	# Standard deviation given by user

# Initialize position, velocity, change of distance vectors of electrons at a given time instant
xx = np.zeros(n*M)	# position
u = np.zeros(n*M)	# velocity
dx = np.zeros(n*M)	# displacement

# Initialize intensity, velocity, position lists containing values of all elctrons at all instants of time
I=[]	# intensity
V=[]	# position
X=[]	# velocity


for k in range(nk):			#identifying the indices where elctron is available/ejected
# adding new electrons
    m=int(np.random.rand()*Msig+M)	# number of new elctrons by normal distribuition of mean and sigma specified, only integer part is taken
    jj=np.where(xx==0)[0]		# finding position of zero for filling new electrons
    xx[jj[:m]]=1			# updating the position array(xx) to 1 where electrons are injected
# To find the electron indices    
    ii=np.where(xx>0)[0]		# identifying the electrons which reaches anode		
# Updating the positions and speed
    dx[ii]=u[ii]+0.5			# updating displacemet of elctrons which are in tubelight			
    xx[ii]=xx[ii]+dx[ii]		# updating position of each electron
    u[ii]=u[ii]+1			# increasing velocity of electrons which are in tubelight
#adding to the history lists
    X.extend(xx[ii].tolist())		# extending the X list		
    V.extend(u[ii].tolist())		# extending the V list
# Anode checking
    zz=np.where(xx>=n)[0]		# identifying the electrons which reaches anode				
    xx[zz]=0				# position updated to zero,as they are not available
    u[zz]=0				# velocity will be zero
# checking ionization
    kk=np.where(u>=u0)[0]		# finding electrons which has velocity greater than threshold		
    ll=np.where(np.random.rand(len(kk))<=p)# getting indices of available elctron postions which can be collided
    kl=kk[ll]				# finding elctron indices which are collided
    
    xx[kl]+= -1*(dx[kl]*np.random.rand(n*M)[kl]) # can also use xx[kl]=xx[kl]-dx[kl]+((u[kl]-1)*dt+0.5*dt*dt), where dt is a random number in between 0 and 1
    u[kl]=0				# updating the collided elctron velcity to zero

    I.extend(xx[kl].tolist())		# adding the information of collidee elctrons using extend function


plt.figure()
plt.hist(X,bins=np.arange(1,n),rwidth=0.9,ec='black')
plt.title("Electron density")
plt.xlabel(r"$x\rightarrow$")
plt.ylabel(r"Number of electrons$\rightarrow$")

plt.figure()
ints,bins,trash = plt.hist(I,bins=np.arange(1,n),rwidth=0.9,ec='black')
plt.title('Emission Intensity')
plt.xlabel(r'$x\rightarrow$')
plt.ylabel(r"Intensity$\rightarrow$")

plt.figure()
plt.scatter(X,V,marker='x')
plt.title("Electron Phase Space")
plt.xlabel(r"$x\rightarrow$")
plt.ylabel(r"$v\rightarrow$")
plt.show()

xpos=0.5*(bins[0:-1]+bins[1:])	# performing average value
print('Intensity Data:')
print('xpos','count')
for i in range(len(xpos)):		# for i in range from 0 to xpos
    print(xpos[i],ints[i])

