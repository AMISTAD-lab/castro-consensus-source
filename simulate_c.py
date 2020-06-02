import ctypes
import numpy as np

clib = ctypes.cdll.LoadLibrary('./simulate.so')

f = clib.f
f.restype = ctypes.c_double

g = clib.g
g.restype = ctypes.c_double

get_agent_choice = clib.get_agent_choice
get_agent_choice.restype = ctypes.c_char

def sim_basic(theta, agent_count, initial_yes=1, initial_total=2):
    buf = np.array([0]*agent_count, dtype=np.byte)
    clib.sim_basic(ctypes.c_char_p(buf.ctypes.data), ctypes.c_double(theta), ctypes.c_int(agent_count), ctypes.c_int(initial_yes), ctypes.c_int(initial_total))
    return buf

def many_simulate_basic(theta, agent_count, num_sims, initial_yes=1, initial_total=2):
    """Run many iterations of the complex simulation (including Recent
    Majority Vote and External Pressure) and return them as a list.

    `num_sims` is the number of times to run it. See the documentation
    of `sim_complex` for the other arguments.
    """
    return [sim_basic(theta, agent_count, initial_yes, initial_total) for _ in range(num_sims)]

g_complex = clib.g_complex
g_complex.restype = ctypes.c_double

get_agent_choice_complex = clib.get_agent_choice_complex
get_agent_choice_complex.restype = ctypes.c_char

def sim_complex(theta, r, alpha, beta, agent_count, initial_m=0.5):
    buf = np.array([0]*agent_count, dtype=np.byte)
    clib.sim_complex(ctypes.c_char_p(buf.ctypes.data), ctypes.c_double(theta), ctypes.c_double(alpha), ctypes.c_double(beta), ctypes.c_double(r), ctypes.c_int(agent_count), ctypes.c_double(initial_m))
    return buf

def many_simulate_complex(theta, r, alpha, beta, agent_count, num_sims, initial_m=0.5):
    """Run many iterations of the complex simulation (including Recent
    Majority Vote and External Pressure) and return them as a list.

    `num_sims` is the number of times to run it. See the documentation
    of `sim_complex` for the other arguments.
    """
    return [sim_complex(theta, r, alpha, beta, agent_count, initial_m) for _ in range(num_sims)]