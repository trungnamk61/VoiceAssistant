import speech_recognition as sr
import os
import time


class speech :
	start = 0
	end = 0
	text = "1"
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
			text = "abbbbb"
		else :
			self.text = r.recognize_google(audio)
			if (self.text == "hey Siri" or self.end == 1) :
				self.start = 1
				print("Xin chao !!!")
			if (self.text == "goodbye") :
				print("Goodbye !!!")
				self.start = 0
				self.end = 1
		return (self.start,self.text)
def main():
	x = 0
	y = 1
	i = 0
	begin = 2
	_text = "a"
	command = []
	execute = []
	count2 = 0
	error = 0
	Text = speech()
	length_command = int(Text.length_file()/2)
	count = -9
	#print(count)
	file = open("command.txt","a+")
	for x in range(length_command) :
		command.append(str(file.readline()).replace("\n",""))
		execute.append(str(file.readline().replace("\n","")))
	#print(command)
	#print(execute)
	
	while True :
		begin,_text = Text.speech2text()
		#print("aaas")
		#print (type(_text))
		#print (begin)
		#print("trungnam")
		if begin == 1 :
		#	print("begin")
			for y in range(length_command) :
		#		print("xxx")
				#print (command[count])
				if str(_text) == command[count] :
		#			print("aaaaaaaa")
		#			print("a")
					print('Executing...')
					os.system(execute[count])
					#print(parent_child)
					print("Done !")
				else :
					error +=1
				count =count +1
				if error == length_command and str(_text) != "hey Siri" and str(_text) != command[0]:
					print("Don't execute your command voice!")
					count = -9
					y=0
					error = 0
		if Text.end == 1 :
			quit()
	file.close
main()
start = 0
end = 0
text = "trungnam"
del f,file,r,audio,command,execute,count,length_command,error,source,start,end,text