import time
import board
import busio
import adafruit_midi
import usb_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.program_change import ProgramChange


uart = busio.UART(board.GP0, board.GP1, baudrate=31250, timeout=0.001)  # init UART
midi_in_channel = 2
midi_out_channel = 1
midi0 = adafruit_midi.MIDI(
    midi_in=uart,
    midi_out=uart,
    in_channel=(midi_in_channel - 1),
    out_channel=(midi_out_channel - 1),
    debug=False,
    )

midi1 = adafruit_midi.MIDI(midi_out=usb_midi.ports[1],midi_in=usb_midi.ports[0], out_channel=0, in_channel=1)
midi = midi1
def setupMidi(mode):
    print(usb_midi)
    if mode == "MIDI":
        midi = midi0
    elif mode == "USB":
        midi = midi1

def sendCC(program, value):
    midi.send(ControlChange(program, value))

def sendPC(program):
    midi.send(ProgramChange(program))

def checkSong(CurrentSong):
    midiIn = midi.receive()
    try:
        songNo = midiIn.note
    except Exception as e:
        error = e
        songNo = CurrentSong
    return songNo