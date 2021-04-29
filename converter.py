from fractions import Fraction

#rtttl string
rtttl = "Theme - Indiana Jones:o=5,d=4,b=250:32p5,e5,8p5,8f5,8g5,8p5,1c6,8p5,d5,8p5,8e5,1f5,p5,g5,8p5,8a5,8b5,8p5,1f6,p5,a5,8p5,8b5,2c6,2d6,2e6,e5,8p5,8f5,8g5,8p5,1c6,p5,d6,8p5,8e6,1f7"

#extract name
split1 = rtttl.split(":")
print("name:" + split1[0])

#extract options
split2 = split1[1].split(",")
d=-1
o=-1
b=-1
for i in split2:
    if i[0] == "d":
        d=int(i[2:])
    if i[0] == "o":
        o=int(i[2:])
    if i[0] == "b":
        b=int(i[2:])
print("d:"+str(d)+" o:"+str(o)+" b: "+str(b))

#extract tones
valideNotes = ["a", "b", "c", "d", "e", "f", "g", "p"]
melody = []

notes = split1[2].split(",")
for n in notes:
    #check if half tone longer
    halflonger = 0
    if n[-1] == ".":
        halflonger=1
        n = n[:-1]
        #print(".")

    duration = -1
    tone = ""
    #check if duration is set
    if n[0] in valideNotes:
        #use default duration
        duration = d
        #octav is defined
        if(len(n)==1):
            if(n[1] == "#"):
                tone = n+str(o)
            else:
                tone = n
        elif(len(n)>1):
            tone = n
        else:
            tone = n+str(o)
    else:
        #duration is no set:
        #find index where tone starts
        start = 0
        for i in range(len(n)):
            if n[i] in valideNotes:
                start = i

        #extract duartion
        if start > 0:
            duration = int(n[:start])
        else:
            duration = 1
    
        #extract tone
        tone = n[start:]
        #check if octav is set
        if (tone[-1] in valideNotes) or ( tone[-1] == "#"):
            tone = tone + str(o)

    #check if tone is pause
    if tone[0] == "p":
        tone = tone[0]

    #convert to new vormate (uppercase)
    tone = tone.upper()

    #handel halftone longer and add to array
    if halflonger == 1:
        melody.append([tone,1.0/duration])
        melody.append([tone,1.0/(duration*2)])
    else:
        duration = 1.0/duration
        melody.append([tone,duration])
#print(melody)

#get longest and shortes duration
max_duration = 1/16
smalles_duration = 1
for m in melody:
    if(m[1] < smalles_duration):
        smalles_duration = m[1]
    if(m[1] > max_duration):
        max_duration = m[1]
#print(Fraction(smalles_duration))
#print(Fraction(max_duration))

#calc multiplayer to fit duratins into range (1/1 - 1/8)
multipy = 1.0
while((smalles_duration*multipy<(1/8)) and (not(max_duration*multipy)>=1)):
    multipy += multipy
#print(multipy)

#create string to put in blheli
str_melody = ""
str_melody_48 = ""
count = 0
clipped = 0
clippedNotes = ""
for m in melody:
    #check if durations fits in range (non fitting will be cut off)
    if(m[1]>=(1/8) and m[1]<=(1)):
        str_melody += m[0] +" "+str(Fraction(m[1]*multipy))+" "
        count += 1
        #check if max length is reached
        if count == 48:
            str_melody_48 = str_melody
    else:
        clipped = 1
        clippedNotes += m[0] +" "+str(Fraction(m[1]*multipy))+" "

if clipped == 1:
    print("melody had to be clipped")
    print("\t"+clippedNotes)

print(" ")
print(str_melody)
if count>48:
    print(" ")
    print("cutted to 48 Notes:")
    print(str_melody_48)