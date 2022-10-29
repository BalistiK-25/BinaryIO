# BinaryIO

This is a little helper tool to manipulate an integer number with bitwise manipulation.
The following lists the function provided:

    # Acess the number stored by the tool.
    binaryIO.ports

    # Sets the state (0-1) of a port (bit) of a byte.
    binaryIO.set_state(state, port)
    example:
    binaryIO.set_state(1, 2)
    
    # Sets the state (0-1) of multiple ports (bits) of a byte with a single call.
    binaryIO.set_state_of_ports(state, ports)
    example:
    binaryIO.set_state_of_ports(1, [2, 3, 5, 8])
    
    # Returns the state of a specific port
    binaryIO.get_state(port)
    example:
    binaryIO.getState(3)



