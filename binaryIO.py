class Binary:
    def __init__(self, byte=0):
        self.byte = byte

    @staticmethod
    def __bit_position_to_binary(port):
        return 1 << port

    def get_state(self, bit):
        return (self.byte & Binary.__bit_position_to_binary(bit)) >> bit

    def set_state(self, state, bit):
        self.byte = self.byte | Binary.__bit_position_to_binary(bit) \
            if state == 1 \
            else self.byte & ~Binary.__bit_position_to_binary(bit)

    def set_state_of_bits(self, state, bit_positions):
        for p in bit_positions:
            self.set_state(state, p)
