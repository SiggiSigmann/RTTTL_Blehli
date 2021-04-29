from fractions import Fraction

rtttl = "HauntedHouse: d=4,o=5,b=108: 2a4., 2e, 2d#, 2b4, 2a4, 2c, 2d, 2a#4, 2e., e, 1f4, 1a4, 1d#, 2e., d, 2c., b4, 1a4, 1p, 2a4, 2e, 2d#, 2b4, 2a4, 2c, 2d, 2a#4, 2e., e, 1f4, 1a4, 1d#, 2e., d, 2c., b4, 1a4"
split1 = rtttl.split(": ")

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
notes = split1[2].split(", ")
melody = ""
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

    if halflonger == 1:
        oldduration = (1.0/duration)
        duration = Fraction(1.0/duration)
        duration = Fraction(oldduration + ( oldduration /2))
    else:
        duration = Fraction(1.0/duration)

    tone = tone.upper()
    melody += (tone + " " + str(duration) + " ")

print(melody)
