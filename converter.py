from fractions import Fraction

rtttl = "The Simpsons Theme - The Simpsons:o=5,d=4,b=225:8f#6.,8f#5.,8f#5.,8a#6.,8f#5.,8c7.,8f#5.,8d#7.,8c#7.,8f#5.,8f#5.,8a#6.,8f#5.,8f#6.,8f#5.,8d#6.,8c6.,8c6.,8c6.,8c#6.,8f#5.,8f#5.,8c5.,8c#5.,8c6.,8c6.,8c6.,8c#6.,8f#5.,8f#5.,c5.,8c#5.,8f#6.,8f#5.,8f#5.,8a#6.,8f#5.,8c7.,8f#5.,8d#7.,8c#7.,8f#5.,8f#5.,8a#6.,8f#5.,8f#6.,8f#5.,8d#6.,8c6.,8c6.,8c6.,8c#6.,8f#5.,8f#5.,8c5.,8c#5.,8c6.,8c6.,8c6.,8c#6.,8f#5.,8f#5.,8c5.,8c#5.,f#5."
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
for m in melody:
    str_melody += m[0] +" "+str(Fraction(m[1]*multipy))+" "

print(str_melody)
