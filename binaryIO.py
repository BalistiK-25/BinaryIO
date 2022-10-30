class MCP:
    def __init__(self, ports=0):
        self.ports = ports

    @staticmethod
    def __port_to_binary(port):
        return 1 << port

    def get_state(self, port):
        return (self.ports & MCP.__port_to_binary(port)) >> port

    def set_state(self, state, port):
        self.ports = self.ports | MCP.__port_to_binary(port) if state == 1 else self.ports & ~MCP.__port_to_binary(port)

    def set_state_of_ports(self, state, port_array):
        for p in port_array:
            self.set_state(state, p)
