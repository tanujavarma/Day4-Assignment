file=open('myfile.txt','w')
file.write(" I Love LetsUpgrade.")
file.close()

file=open('myfile.txt','r')
content=file.read()
file.close()

file=open('myfile.txt','a')
file.write("I want to learn python.")
file.close()



