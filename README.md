# BinaryIO

This is a little helper tool to manipulate an integer number with bitwise manipulation.
The following lists the function provided:

Create a new binaryIO object, optionally with a pre-specified byte

    binIO1 = binaryIO.Binary()
    binIO2 = binaryIO.Binary(0b10011011)
    
Access the byte stored inside the object:

    binIO.byte

Change a specific bit of the byte (state is either 0 or 1; if invalid state, defaults to 0)

    binIO.set_state(1, 0) #set state 1 of bit 0 = 0b1
    binIO.set_state(1, 3) #set state 1 of bit 3 = 0b1001
    binIO.set_state(0, 3) #set state 0 of bit 3 = 0b1
    
    
Change a batch of bits of a byte (state is either 0 or 1; if invalid state, defaults to 0)

    binIO.set_state_of_bits(1, [2, 3, 7]) #set state 1 of bits 2, 3 and 7    = 0b10001100
    binIO.set_state_of_bits(1, [5, 6]) #set state 1 of bits 5 and 6          = 0b11101100
    binIO.set_state_of_bits(0, [2, 6, 7]) #set state 0 of bits 2, 6 and 7    = 0b101000
    
    
Returns the state of a specific bit

    binIO = binaryIO.Binary(0b1001)
    binIO.get_state(3) #get state of bit 3 = 1
    binIO.get_state(2) #get state of bit 2 = 0
    




