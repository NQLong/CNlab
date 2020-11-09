from time import time
import sys
HEADER_SIZE = 12
def encode(self=0, version =0, padding =0, extension=0, cc=0, seqnum=0, marker=0, pt=0, ssrc=0, payload=0):
    """Encode the RTP packet with header fields and payload."""
    timestamp = int(time())
    print(timestamp)
    header = bytearray(HEADER_SIZE)
    header[0] = (
        header[0] 
        |   version << 6 
        |   padding << 5 
        |   extension << 4
        |   cc
    )

    header[1] = (
        header[1]
        |   marker << 7
        |   pt 
    )

    header[2:3]=[seqnum >> 8,seqnum & 255]
    header[4:8]=[
        (timestamp >> i) & 255 for i in [24,16,8,0]
    ]
    header[8:16]=[
        (timestamp >> i) & 255 for i in [24,16,8,0]
    ]
    # header[4:8]= [
    #     0xFF & timestamp
    # ]
    #--------------
    # TO COMPLETE
    #--------------
    # Fill the header bytearray with RTP header fields
    
    # header[0] = ...
    # ...
    
    # Get the payload from the argument
    # self.payload = ...
    for i in range (12): 
        print(hex(header[i]),end = ' ')
    print()
encode(version = 2,seqnum= 0x9865, pt =26,ssrc=89)
