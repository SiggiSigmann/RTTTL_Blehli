# RTTTL_Blehli
Convert RTTTL to Blheli_32 fromat

This python script converts music in RTTTL fromat into BLHeli fromat. So it can be used as a Startupsounf for your esc.
A lot of songs can be found here [http://esctunes.com/](http://esctunes.com/)


## Use
To convert you have to execute the scipr with the RTTTL as an Argument. e.g:

```
python converter.py "Pacman:o=5,d=4,b=112:32b5,32p5,32b6,32p5,32f#6,32p5,32d#6,32p5,32b6,32f#6,16p5,16d#6,16p5,32c6,32p5,32c7,32p5,32g6,32p5,32e6,32p5,32c7,32g6,16p5,16e6,16p5,32b5,32p5,32b6,32p5,32f#6,32p5,32d#6,32p5,32b6,32f#6,16p5,16d#6,16p5,32d#6,32e6,32f6,32p5,32f6,32f#6,32g6,32p5,32g6,32g#6,32a6,32p5,32b6."
```

If the music is to fast you can try to adust it with the Gen. Length setting. Also you can set a Speed Multiplayer as an argument. e.g. 2 => half speed.
```
python converter.py 2 "Pacman:o=5,d=4,b=112:32b5,32p5,32b6,32p5,32f#6,32p5,32d#6,32p5,32b6,32f#6,16p5,16d#6,16p5,32c6,32p5,32c7,32p5,32g6,32p5,32e6,32p5,32c7,32g6,16p5,16e6,16p5,32b5,32p5,32b6,32p5,32f#6,32p5,32d#6,32p5,32b6,32f#6,16p5,16d#6,16p5,32d#6,32e6,32f6,32p5,32f6,32f#6,32g6,32p5,32g6,32g#6,32a6,32p5,32b6."
```

## Hints
- If there are is a Pause after each Tone: To save sam Tones the Pause can be manual deleted and the Gen. Interval option can be uset to replace it
- Long Notes will also be scaled up be adding them multiple times. If more tones are needed these duplicats can be delete or adjustet manualy.
- It is better if the song don't contains 1/16 or 1/32 tones. To keep them the song will be automatically be scaled and this can cause dublicate notes.