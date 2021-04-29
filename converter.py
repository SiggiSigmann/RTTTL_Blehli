
d=4
melody = "2a#5,2f5,p5,8a#5,8a#5,8c6,8d6,8d#6,2f6,2p5,f6,f6,8f#6,8g#6,2a#6,2p5,a#6,8a#6,8p5,8g#6,8f#6,g#6.,8f#6,2f6,2p5,2f6,d#6,8d#6,8f6,2f#6,2p5,f6,d#6,c#6,8c#6,8d#6,2f6,2p5,d#6,c6,c6,8c6,8d6,2e6,2p5,2g6,1f6"

notes = melody.split(",")

new_notes = []
stringout = ""

numbers = ["1","2","3","4","5","6","7","8","9"]
for n in notes:
	#check for duration is set
	if n[0] in numbers:
		new = str(int(int(n[0])/2))
		if new == "0":
			new = "1"					
		if n[1] == "p":
			stringout += "P 1/" + new +" "
		else:
			if n[-1] == ".":
				stringout += (n[1].upper()+n[2:-1]+" 1/"+ new +" ")
			else:
				stringout += (n[1].upper()+n[2:]+" 1/"+ new +" ")
	else:
		d = str(2)
		if d == "0":
			d = "1"
		if n[0] == "p":
			stringout += "P 1/"+ d +" "
		else:
			if n[-1] == ".":
				stringout += (n[0].upper()+n[1:-1]+" 1/"+ d +" ")
			else:
				stringout += (n[0].upper()+n[1:]+" 1/"+ d +" ")
print(stringout)
