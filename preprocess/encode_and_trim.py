import base64
from dataclasses import dataclass
from data_meta.data_meta import DataMeta
from util.reader import Reader
from util.writer import Writer


@dataclass
class EncodeAndTrim:
    def __post_init__(self):
        data_meta = DataMeta()

        input_data: bytes = Reader().read_data(input_path=data_meta.input_path)
        encoded: bytes = self.encode_data(input_data)
        trimmed = self.trim_data(encoded)
        Writer().save_data(trimmed, data_meta.output_path)

    def encode_data(self, data: bytes) -> bytes:
        return base64.b64encode(data)

    def trim_data(self, data: bytes) -> str:
        return str(data)[2:][:-1]
