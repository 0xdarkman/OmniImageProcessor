from dataclasses import dataclass


@dataclass
class Reader:
    def read_data(self, input_path: str) -> bytes:
        with open(input_path, "rb") as f:
            return f.read()
