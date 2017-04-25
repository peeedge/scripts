import winsound
import time

# the notes
P = 0   # pause
C = 1
CS = 2  # C sharp
D = 3
DS = 4
E = 5
F = 6
FS = 7
G = 8
GS = 9
A = 10
AS = 11
B = 12

EN = 100  # eighth note
QN = 200  # quarter note
HN = 400  # half note
FN = 800  # full note

def play(octave, note, duration):
    """play note (C=1 to B=12), in octave (1-8), and duration (msec)"""
    if note == 0:    # a pause
        time.sleep(duration/1000)
        return
    frequency = 32.7032           # C1
    for k in range(0, octave):    # compute C in given octave
        frequency *= 2

    for k in range(0, note):      # compute frequency of given note
        frequency *= 1.059463094  # 1.059463094 = 12th root of 2
    #~ time.sleep(0.0010)             # delay between keys 

    winsound.Beep(int(frequency), duration)

def part0():
    play(3,C,FN)
    play(3,E,HN)
    play(3,G,FN)
    play(3,D,FN)

def part1():
    play(3,A,HN)
    play(3,C,FN)
    play(3,E,HN)
    play(3,D,FN)

def part2():    
    play(4,F,QN)
    play(4,G,QN)
    play(4,G,QN)
    play(4,G,QN)
    play(4,G,QN)
    play(4,F,QN)
    play(4,E,EN)
    play(4,F,QN)
    play(4,G,QN)

def part3():  
    play(4,E,EN)
    play(4,F,QN)
    play(4,G,FN)
    play(4,F,QN)
    play(4,E,EN)
    play(4,F,QN)

    play(4,E,EN)
    play(4,D,EN)
    play(4,E,EN)

    play(4,D,FN)
    play(4,C,FN)
    play(4,D,FN)

    play(4,E,HN)
    play(4,C,FN)

def good():
    play(3,A,HN)
    play(4,C,FN)
    
def ugly():
    play(4,F,QN)
    play(4,G,FN)
    play(4,G,FN)
    play(4,G,FN)
    play(4,G,FN)
    play(4,F,QN)
    play(4,F,QN)
    play(4,G,FN)

def main():
    #good()
    part0()
    part1()
    part2()
    part2()
    play(4,E,HN)
    part2()
    part3()
   # ugly()


