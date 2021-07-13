import sys 


if len(sys.argv) == 2:     #If the length of the array of command lines is 2.then the loop should proceed.
	fileName = sys.argv[1] #initialise the filename as 2nd of array of command lines.
	CIRCUIT = ".circuit"  #Assigning CIRCUIT as circuit\n.
	END = ".end"          #Assigning End as end\n.
	start = -1            #initialising start eqaul to -1.
	end = -2              #initialising end is eqaul to -2.
	final = []            #initialise an empty list.
	from_node=[]
	to_node=[]
	value=[]
	element=[]
						
	
	with open(fileName) as f:  #to open the file in current directory.Initialise as file.
		lines = f.readlines() #To read all the lines at a single go in file and then return them as each line as string element in the list.
		for line in lines:   # for every line in lines to be 
			if CIRCUIT == line[:len(CIRCUIT)]:  #compare the string elements in line with CIRCUIT.
			   start = lines.index(line) #assign the index value of the line having circuit\n to start.
			elif END == line[:len(END)]:  #compare the string elements in line with END.
			   end = lines.index(line)  #assign the index value of the line having end\n to end.
			   break
		if start >= end:  # if the start value is greater or equal to end invalid state.
		    print("INVALID") 
		    exit(0)	   
		
		for line in reversed(lines[start+1:end]):
			element=line.split('#')[0].split()[0]
			from_node=line.split('#')[0].split()[1]
			to_node=line.split('#')[0].split()[2]
			value=line.split('#')[0].split()[3]
			print(value,to_node,from_node,element)
			
	
		
			
elif len(sys.argv) ==1 : print("Error: No Input Found") #if the length of sys.argv is 1 because there is no input.
else: print("Error:Too Many Inputs Found")  #anything other than that the inputs are more inputs.
