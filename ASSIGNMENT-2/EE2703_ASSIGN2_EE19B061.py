import sys
import numpy as np
import math

if len(sys.argv) == 2:					#If the length of the array of command lines is 2.then the loop should proceed.
	if sys.argv[1].split(".")[1] != "netlist":	#if it is not netlist show an error.
		print("ERROR:Incorrect input file type")
	else:
	# Initialiasing all the variables required.
		start = -1 
		end = -2
		GND = 0 
		NODE = 0 
		final = []	
		x=[]
		CIRCUIT = ".circuit"
		END = ".end"
		ALT = ".ac"
		ac = 0
		AC = 0
		v = 0
		y=0	
				
		with open(sys.argv[1]) as file: 	#to open the file in current directory.Initialise as file.
			lines = file.readlines()	#To read all the lines at a single go in file and then return them as each line as string element in the list.
			
			for i in range(0,len(lines)):
				if lines[i][:len(CIRCUIT)]==CIRCUIT:	#compare the string elements in line with CIRCUIT.
				   start = i				#assign the index value of the line having circuit\n to start.   					
				elif lines[i][:len(END)]==END:	#compare the string elements in line with END.
				   end = i				#assign the index value of the line having end\n to end.			   
				elif lines[i][:len(ALT)]==ALT:	#compare the string elements in line with ALT.
					ac = lines[i].split()		#Storing tokens of line with .ac respectively.
					AC+=i				#assigning the index of line containing .ac in AC.
					w=2*math.pi*float(ac[-1])	#Omega of the ac source i.e. 2*pi*frequency.

			if AC<end:					#if .ac is within the circuit then assign AC is 0.
				AC = 0
			if start >= end: 				# if the start value is greater or equal to end invalid state.
			    print("INVALID CIRCUIT IN THE INPUT FILE")
			else:
				for i in range(start+1,end):		#i varing from start+1 to end values.
					res = (lines[i].split("#")[0]).split()	#removes the comments in the code and spliting at white spaces.		
					final.append(res)
 
				for l in range(0,len(final)):
					
					
						if final[l][1] == "GND": i = 0	#Reading all the node values at one side.	
						else: i = int(final[l][1])							
						if final[l][2] == "GND": j = 0	#Reading all the node values at other side.							
						else: j = int(final[l][2]) 
						
						if NODE <= i:				#assigning NODE the max value of i i.e. from one side.
							NODE = i
						if NODE <= j:				#assigning NODE the max value of j i.e. from other side.
							NODE = j
						if final[l][0][0] == "V" : v+=1	#No. of voltage sources
						
						
				
				A = [ [ 0 for i in range(NODE+v) ] for j in range(NODE+v) ] #initiating matrix of required sizes.
				b = [ [ 0 for i in range(NODE+v) ] for j in range(1) ]      #initiating matrix of required sizes
					
				for l in range(0,len(final)):										
	#Assigning the resistor components to the matrix.	
					if final[l][0][0] == "R":
						z = float(final[l][3]) #Assigning the Impedence value to z.
						
						if final[l][1] == "GND":
							i = 0
						else:
							i = int(final[l][1])
						if final[l][2] == "GND":
							j = 0
						else:
							j = int(final[l][2])

						if i*j != 0:
							A[i-1][i-1] += 1/z
							A[i-1][j-1] += -1/z
							A[j-1][i-1] += -1/z
							A[j-1][j-1] += 1/z
						if i == 0:
							A[j-1][j-1] += 1/z
						if j == 0:
							A[i-1][i-1] +=1/z
	#Assigning the Capacitor components to the matrix.
					if final[l][0][0] == "C" and AC !=0:
						z = complex(0,-1/(w*float(final[l][3])))	#Assigning the Impedence value to z.
						
						if final[l][1] == "GND":
							i = 0
						else:
							i = int(final[l][1])
						if final[l][2] == "GND":
							j = 0
						else:
							j = int(final[l][2])

						if i*j != 0:
							A[i-1][i-1] += 1/z
							A[i-1][j-1] += -1/z
							A[j-1][i-1] += -1/z
							A[j-1][j-1] += 1/z
						if i == 0:
							A[j-1][j-1] += 1/z
						if j == 0:
							A[i-1][i-1] +=1/z

	#Assigning the Inductor components to the matrix.
					if final[l][0][0] == "L" and AC !=0:
						z = complex(0,(w*float(final[l][3])))	#Assigning the Impedence value to z.
						
						if final[l][1] == "GND":
							i = 0
						else:
							i = int(final[l][1])
						if final[l][2] == "GND":
							j = 0
						else:
							j = int(final[l][2])

						if i*j != 0:
							A[i-1][i-1] += 1/z
							A[i-1][j-1] += -1/z
							A[j-1][i-1] += -1/z
							A[j-1][j-1] += 1/z
						if i == 0:
							A[j-1][j-1] += 1/z
						if j == 0:
							A[i-1][i-1] +=1/z
	#Assigning the voltage source values and current through sources to the matrix.
		
					if final[l][0][0] == "V":
						y+=1
						if final[l][1] == "GND":
							i = 0
						else:
							i = int(final[l][1])
							A[int(NODE+y-1)][i-1] = 1
							A[i-1][int(NODE+y-1)] = -1
							if final[l][3] =="ac":								
								b[0][int(NODE+y-1)] = complex(float(final[l][-2])*math.cos(float(final[l][-1])),float(final[l][-2])*math.sin(float(final[l][-1])))
							else:								
								b[0][int(NODE+y-1)] = float(final[l][-1])
						if final[l][2] == "GND":
							j = 0
						else:
							j = int(final[l][2])
							A[int(NODE+y-1)][j-1] = -1
							A[j-1][int(NODE+y-1)] = -1
							if final[l][3] == "ac":
								b[0][NODE+y-1] = -complex(float(final[l][-2])*math.cos(float(final[l][-1])),float(final[l][-2])*math.sin(float(final[l][-1])))
							else:
								b[0][NODE+y-1] = -float(final[l][-1])				
				
				out = np.linalg.solve(A,b[0]) #solving the matrix equation Ax=B and giving output x as out(matrix).

						
						
				print("Voltages at nodes are")
				for i in range(0,NODE+v):
					if AC==0:       # for dc sources the node wise voltage and current through the voltage source.
						if i<NODE:print("Voltage at node %d is"%(i+1))
						if i>=NODE:print("Current through V%d source is"%(i-NODE+1))
						print(float("%.2f"%out[i]))
					else:		# for dc sources the node wise voltage and current through the voltage source.
						if i<NODE:print("Voltage at node %d is"%(i+1))
						if i>=NODE:print("Current through V%d source is"%(i-NODE+1))
						print(out[i])  
				
				
elif len(sys.argv) ==1 : print("Usage: %s \nError: No Input Found \nExpected:FileName.py FileName.netlist" % sys.argv[0])
else: print("Usage: %s \nError:Too Many Inputs Found \nExpected:FileName.py FileName.netlist" % sys.argv)
