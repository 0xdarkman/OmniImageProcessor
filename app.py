import numpy as np
from preprocess.encode_and_trim import EncodeAndTrim
from data_meta.data_meta import DataMeta
from commands.commands import Commands


def read_base64data(input_path: str) -> str:
    with open(input_path, "r") as f:
        return f.read()


def base64_txt_to_array(base64data: str, array_number):
    print(array_number)
    n = 255
    ll = [base64data[index: index + n] for index in range(0, len(base64data), n)]
    array = np.array(ll)
    return (array[int(array_number)])


if __name__ == '__main__':
    EncodeAndTrim()

    commands = Commands()

    # from here onwards is just tmp code to test it works ...
    data = read_base64data(DataMeta.output_path)

    array_number = 0

    while array_number <= 9000:
        data_packet = base64_txt_to_array(data, array_number)
        array_number += 1

        # I got an error here
