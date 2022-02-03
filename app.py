import numpy as np
from preprocess.encode_and_trim import EncodeAndTrim
from data_meta.data_meta import DataMeta
from commands.commands import Commands


def read_base64data(input_path: str) -> str:
    with open(input_path, "r") as f:
        return f.read()


def base64_txt_to_array(data: str, array_number):
    print(array_number)
    n = 255
    ll = [data[index: index + n] for index in range(0, len(data), n)]
    arr = np.array(ll)
    return (arr[int(array_number)])


if __name__ == '__main__':
    token_name = "someTokenName1"
    sending_address = "someAddress1"
    serial_number = "someSerialNumber1"
    token_url = "someTokenUrl"


    EncodeAndTrim()
    commands = Commands()


    # from here onwards is just tmp code to test it works ...
    # this needs to be refactored

    data = read_base64data(DataMeta.output_path)
    array_number = 0
    while array_number < 57: # IndexError: index 57 is out of bounds for axis 0 with size 57
        data_packet = base64_txt_to_array(data, array_number)
        commands.create_omni_command_d1(sending_address, data_packet)
        array_number += 1
        data_packet = base64_txt_to_array(data, array_number)
        commands.create_omni_command_d2(data_packet)
        array_number += 1
        data_packet = base64_txt_to_array(data, array_number)
        commands.create_omni_command_d3(token_name, serial_number, token_url, data_packet)
        array_number += 1

