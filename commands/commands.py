

class Commands:
    def __init__(self):
        pass

    def create_omni_command_d1(self, sending_address, data_packet) -> str:
        return f'omni_sendissuancefixed "{sending_address}" 1 1 0 "{data_packet}'

    def create_omni_command_d2(self, data_packet):
        return f'" "{data_packet}'

    def create_omni_command_d3(self, token_name, serial_number, token_url, data_packet) -> str:
        return f'" "{token_name}{str(serial_number)[1:]}" "{token_url}" "{data_packet}" "1"'
