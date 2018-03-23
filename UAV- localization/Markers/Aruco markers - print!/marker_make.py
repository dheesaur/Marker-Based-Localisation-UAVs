import sys 
import os 


n = int(raw_input('Enter the number of markers to make:(1-1023)'))

for i in range(1,n+1,1):
	
	#create the command string
	cmd_string = 'aruco_create_marker {} outfile{}.png'.format(i,i)
	#run the cmd_string in a subshell
	status = os.system(cmd_string)
	if status is not 0:
		print 'Unable to create {} marker'.format(i)
	else:
		print 'Marker {} created succesfully'.format(i)

#terminating program
sys.exit(0)
