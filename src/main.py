# Author: Dathan Ho
# Description: Runs calculations based on component values for my first pedal design.
# This pedal design consists of a fixed-biased single stage common-emitter amplifier and
# an assymetrical anti-parallel diode configuration for clipping.

# Common-Emitter Amplifier

import bjt_math
from components import transistors

print ("\n--- Calculations for Pedal Design #1 ---")

# Supply Voltage
vcc = 9

# Getting transistor specs
transistor1 = "2N3904"
hfe_2N3904 = transistors[transistor1]["hfe"]
vbe_2N3904 = transistors[transistor1]["vbe"]
vce_sat_2N3904 = transistors[transistor1]["vce_sat"]

# Common-emitter amplifier stage

print("\n1. Amplifier Stage Collector Voltage")
ce_vc, ce_target_vc = bjt_math.calculate_common_emitter(
    vcc = vcc,
    r_upper = 2.2e6,
    r_lower = 470e3,
    r_base = 470,
    r_emitter = 470,
    r_collector = 10e3,
    hfe = hfe_2N3904,
    vbe = vbe_2N3904,
    vce_sat = vce_sat_2N3904
)

print ("The collector voltage for CE amplifier is:", round(ce_vc, 2))
print ("Max headroom is available when collector voltage is:", round(ce_target_vc, 2))
print()

# Emitter-follower buffer stage

print("\n2. Buffer Stage")
ef_ve, ef_target_ve = bjt_math.calculate_emitter_follower(
    vcc = vcc,
    r_upper = 1e6,
    r_lower = 2.67e6,
    r_base = 100,
    r_emitter = 10e3,
    hfe = hfe_2N3904,
    vbe = vbe_2N3904,
    vce_sat = vce_sat_2N3904
)

print ("The emitter voltage for Emitter Follower buffer is:", round(ef_ve, 2))
print ("Max headroom is available when emitter voltage is:", round(ef_target_ve, 2))
print()