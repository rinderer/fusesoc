from fusesoc.simulator.icarus import SimulatorIcarus
from fusesoc.simulator.modelsim import Modelsim
from fusesoc.simulator.verilator import Verilator
from fusesoc.simulator.isim import Isim
def SimulatorFactory(sim,system):
    if sim == 'icarus':
        return SimulatorIcarus(system)
    elif sim == 'modelsim':
        return Modelsim(system)
    elif sim == 'verilator':
        return Verilator(system)
    elif sim == 'isim':
        return Isim(system)
    else:
        raise RuntimeError("Unknown simulator '"+sim+"'")
