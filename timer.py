import schedule
import time
import subprocess

def job(t):
	#TAKE A LOOK AT THIS LATER
	#https://www.tutorialspoint.com/python/python_command_line_arguments.htm
	#USE THIS TO CREATE A RANDOM PLAYLIST
	#http://stackoverflow.com/questions/12831210/embedding-youtube-playlist-but-starting-from-random-video
	#Create a similar draftOrder page to create a random start and maybe embed the playlist on the page
	#then create a new bat script that calls that 
	#and finally have this python script call that bat script

	filepath="C:/batches/playlist.bat"
	p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)
	stdout, stderr = p.communicate()

schedule.every().day.at("07:10").do(job,'It is 01:00')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
	#The sleep is to slow down the while loop