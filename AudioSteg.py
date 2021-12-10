import wave

def audio_encode(file, text):
    audio = wave.open(file, mode='rb')

    #get the frames of the audio file and convert to bytes
    frames = bytearray(list(audio.readframes(audio.getnframes())))

    #append data to fill the rest of the bytes not taken up by the text
    final_string = text + int((len(frames)-(len(text)*8*8))/8) * '#'
    #text to bit array
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') 
        for i in final_string])))
    
    #put the bits from the bit array into the LSB of each byte in the audio
    for i, bit in enumerate(bits):
        frames[i] = (frames[i] & 254) | bit

    final_frames = bytes(frames)

    #write to file
    with wave.open('EncodedAudio.wav', 'wb') as fd:
        fd.setparams(audio.getparams())
        fd.writeframes(final_frames)
    audio.close()


def audio_decode(file):
    audio = wave.open(file, mode='rb')

    #audio to byte array
    frames = bytearray(list(audio.readframes(audio.getnframes())))

    extract = [frames[i] & 1 for i in range(len(frames))]

    #convert the bytes back into string
    string = "".join(chr(int("".join(map(str,extract[i:i+8])),2)) 
        for i in range(0,len(extract),8))

    final_string = string.split("###")[0]
    audio.close()
    return final_string