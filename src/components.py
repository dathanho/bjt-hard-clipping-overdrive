# Description: Includes all the components and important specifications

# Available resistor values in kit
resistors = {10, 47, 100, 220, 330, 470, 1000, 1500, 2200, 2700, 3900, 
             4700, 5600, 8200, 10000, 15000, 22000, 33000, 47000, 68000,
             100000, 150000, 220000, 330000, 470000, 1000000, 2200000}

# Available capacitors
capacitors = {30e-12, 47e-12, 100e-12, 470e-12, 1e-9, 2.2e-9, 
              4.7e-9, 10e-9, 22e-9, 47e-9, 100e-9, 220e-9, 1e-6}

# Available diodes - specs are typical values (not exact)
diodes = {
    "BAT41": {"type": "Schottky", "vf": 0.4},
    "1N4148": {"type": "Silicon Switching", "vf": 0.7 }
}

# Available transistors - specs are typical values (not exact)
transistors = {
    "2N3904": {"type": "NPN", "hfe": 200, "vbe": 0.65, "vce_sat": 0.2}
}

