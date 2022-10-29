ports = 0


def __port_to_binary(port):
    return 1 << (port - 1)


def get_state(port):
    return (ports & __port_to_binary(port)) >> (port - 1)


def set_state(state, port):
    global ports
    ports = ports | __port_to_binary(port) if state == 1 else ports & ~__port_to_binary(port)


def set_state_of_ports(state, port_array):
    for p in port_array:
        set_state(state, p)
