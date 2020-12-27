class Laptop:
    def __init__(self):
        RAM1 = RAM('8 GB')
        RAM2 = RAM('8 GB')
        RAM3 = RAM('16 GB')
        self.accessible_memory = [RAM1, RAM2, RAM3]

    def _sum_ram(self):
        ram_sum = 0
        for ram in self.accessible_memory:
            values = ram.memory.split(" ")
            gb = int(values[0])
            ram_sum += gb
        return f"{ram_sum} GB"

    def print_ram(self):
        for i, ram in enumerate(self.accessible_memory):
            print(f"RAM{i+1} has", ram.memory)
        print("All accessible RAM: ", self._sum_ram())


class RAM:
    def __init__(self, memory):
        self.memory = memory


if __name__ == '__main__':
    acer_predator = Laptop()
    acer_predator.print_ram()