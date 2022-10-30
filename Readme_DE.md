# BinaryIO

BinaryIO ist ein Hilfswerkzeug, um bestimmte bits eines bytes zumanipulieren.
Folgend gelistet sind die Funktionen, die das Werkzeug beinhaltet:

Erstellen eines neues Objektes (optional mit einem bestimmten Byte gesetzt):

    binIO1 = binaryIO.Binary()
    binIO2 = binaryIO.Binary(0b10011011)
    
Auslesen des gespeicherten Wertes:

    binIO.byte

Ändern eines bestimmten Bits des Bytes (der state ist dabei entweder 0 oder 1; ein invalider state ist standardmäßig 0):

    binIO.set_state(1, 0) #setzte state 1 von bit 0 = 0b1
    binIO.set_state(1, 3) #setzte state 1 von bit 3 = 0b1001
    binIO.set_state(0, 3) #setzte state 0 von bit 3 = 0b1
    
    
Ändere mehrere Bits des Bytes (der state ist dabei entweder 0 oder 1; ein invalider state ist standardmäßig 0):


    binIO.set_state_of_bits(1, [2, 3, 7]) #setzte state 1 von bits 2, 3 and 7   = 0b10001100
    binIO.set_state_of_bits(1, [5, 6])    #setzte state 1 von bits 5 and 6      = 0b11101100
    binIO.set_state_of_bits(0, [2, 6, 7]) #setzte state 0 von 2, 6 and 7        = 0b101000
    
    
Frage den Wert eines bits ab:

    binIO = binaryIO.Binary(0b1001)
    binIO.get_state(3) #gibt den Wert des bits 3 aus  = 1
    binIO.get_state(2) #gibt den Wert des bits 2 aus  = 0
    




