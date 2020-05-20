import speech_recognition as sr
import os
import time


class speech :
	start = 0
	end = 0
	text = " "
	def length_file(self) :
		File = open("command.txt","a+")
		Counter = 0
		# Reading from file 
		Content = File.read() 
		CoList = Content.split("\n")
		for i in CoList :
			Counter+=1;
    		#print(Counter-1);
		File.close
		return(Counter-1) 
	def speech2text(self) :
		end = 0
		r = sr.Recognizer()
		#while True :
		with sr.Microphone() as source :
			r.adjust_for_ambient_noise(source) 	 #Adjusts the energy threshold dynamically
			#print("                       start : ",time.localtime(time.time()))
			print ("I'm listening")
			audio = r.listen(source)			 #Records a single phrase from ``source`` (an ``AudioSource`` instance) into an ``AudioData`` instance
			print("Time over,thanks")
			#print("                       end : " ,time.localtime(time.time()))
		try : 
			print("text : " + r.recognize_google(audio));
		except KeyboardInterrupt :
			print("exit !!!")
			quit()
		except : 
			print("Don't recognition your voice !!! Please talking again !")
		else :
			text = r.recognize_google(audio)
			if (text == "hey Siri" or end == 1) :
				start = 1
				print("Xin chao !!!")
			if (text == "goodbye") :
				print("Goodbye !!!")
				start = 0
				end = 1
		
def main():
	x = 0
	y = 0
	i = 0
	command = []
	execute = []
	count = -6
	count2 = 0
	error = 0
	Text = speech()
	length_command = Text.length_file()/2

	file = open("command.txt","a+")
	for x in range(length_command) :
		command.append(str(file.readline()).replace("\n",""))
		execute.append(str(file.readline().replace("\n","")))
	#print(command)
	#print(execute)
	
	while True :
		Text.speech2text()
		print (Text.text)
		if Text.start == 1 :
			for y in range(length_command) :
				count = count+1
				#print (command[count])
				if Text.text == command[count] :
					print("a")
					print('Executing...')
					os.system(execute[count])
					#print(parent_child)
					print("Done !")
				else :
					error +=1
				if error == length_command :
					print("Don't execute your command voice!")
				count = -6
				y=0;
				error = 0
		if Text.end == 1 :
			quit()
	file.close
main()
start = 0
end = 0
text = "trungnam"
del f,file,r,audio,command,execute,count,length_command,error,source,start,end,text