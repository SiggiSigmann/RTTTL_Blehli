from fractions import Fraction

rtttl = "Theme - Harry Potter:o=5,d=16,b=125:8b5,8e6.,g6,8f#6,4e6,8b6,4a6.,4f#6.,8e6.,g6,8f#6,4d6,8f6,2b5,8p5,8b5,8e6.,g6,8f#6,4e6,8b6,4d7,8c#7,4c7,8g#6,8c7.,b6,8a#6,4f#6,8g6,2e6,8p5,8g6,4b6,8g6,4b6,8g5,4c7,8b6,4a#6,8f#6,8g6.,b6,8a#6,4a#5,8b5,2b6,8p5"
split1 = rtttl.split(":")

print("name:" + split1[0])
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

valideNotes = ["a", "b", "c", "d", "e", "f", "g", "p"]
notes = split1[2].split(",")
smalles_duration = 99
melody = []
for n in notes:
    halflonger = 0
    if n[-1] == ".":
        halflonger=1
        n = n[:-1]
        #print(".")

    duration = -1
    tone = ""
    if n[0] in valideNotes:
        duration = d
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
        start = 0
        for i in range(len(n)):
            if n[i] in valideNotes:
                start = i

        if start > 0:
            duration = int(n[:start])
        else:
            duration = 1
    
        tone = n[start:]
        if (tone[-1] in valideNotes) or ( tone[-1] == "#"):
            tone = tone + str(o)

    if tone[0] == "p":
        tone = tone[0]
    tone = tone.upper()

    if halflonger == 1:
        melody.append([tone,1.0/duration])
        melody.append([tone,1.0/(duration*2)])
    else:
        duration = 1.0/duration
        melody.append([tone,duration])


for m in melody:
    if(m[1] < smalles_duration):
        smalles_duration = m[1]
        
    
print(Fraction(smalles_duration))
#print(melody)

multipy = 1.0
while(smalles_duration*multipy<(1/8)):
    multipy += multipy
print(multipy)

str_melody = ""
count = 0
for m in melody:
    str_melody += m[0] +" "+str(Fraction(m[1]*multipy))+" "
    count += 1
    if count == 48:
        print(str_melody)
        print(" ")
        print(" ")

print(str_melody)
