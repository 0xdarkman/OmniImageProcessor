from dataclasses import dataclass


@dataclass
class Writer:
    def save_data(self, data: str, output_path: str):
        with open(output_path, "w+") as f:
            f.write(data)
