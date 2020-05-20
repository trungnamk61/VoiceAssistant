import speech_recognition as sr
import os
import time
def parent_child(pid): 
    n = os.fork() 
  
    # n greater than 0  means parent process 
    if n > 0: 
        pid = os.getpid()
def length_file() :
	File = open("/home/trungnam/Documents/OS_project/VoiceCommandProject/command.txt","a+")
	Counter = 0
	# Reading from file 
	Content = File.read() 
	CoList = Content.split("\n")
	for i in CoList :
		Counter+=1;
    	#print(Counter-1);
	File.close
	return(Counter-1) 
def main():
	length_command = length_file()/2;
	x = 0;
	y = 0;
	i = 0;
	command = []
	execute = []
	count = -6;
	count2 = 0;
	error = 0;
	file = open("/home/trungnam/Documents/OS_project/VoiceCommandProject/command.txt","a+")
	for x in range(length_command) :
		command.append(str(file.readline()).replace("\n",""))
		execute.append(file.readline().replace("\n",""))
	#print(command)
	#print(execute)
	r = sr.Recognizer()
	while True :
		with sr.Microphone() as source :
			r.adjust_for_ambient_noise(source) 
			#print("                       start : ",time.localtime(time.time()))
			print ("Say something")
			audio = r.listen(source)
			print("Time over,thanks")
			#print("                       end : " ,time.localtime(time.time()))
		try : 
			print("text : " + r.recognize_google(audio));
		except KeyboardInterrupt :
			print("exit !!!");
			quit()
		except :
			print("Don't recognition your voice !!! Please talking again !")
		else :
			text = r.recognize_google(audio)
			if (text == "hey") :
				print("Xin chao !!!")
			for y in range(length_command) :
				count = count+1
				#print (command[count])
				if (text == command[count]) :
					print('a')
					os.system(execute[count])

				else :
					error +=1
				if error == length_command :
					print("Don't execute your command voice!")
			count = -6;
			y=0;
			error = 0;
	file.close
	del f,file,r,audio,command,execute,count,length_command,error
if __name__ == "__main__":
    main()