# Author: Dathan Ho
# Description: This file includes functions that includes
# fundamental calculations for BJT circuit topologies.


from components import transistors

def calculate_common_emitter(vcc, r_upper, r_lower, r_base,
                             r_emitter, r_collector, hfe, vbe, vce_sat):
    """Calculates collector voltage for common emitter amplifier
    and target voltage for maximum headroom"""

    # 1. Base network thevenin equivalent and base current
    vth = vcc * (r_lower/(r_upper + r_lower))
    rth = ((r_lower*r_upper)/(r_lower + r_upper)) + r_base
    ib = (vth - vbe) / (rth + ((hfe + 1)*r_emitter))

    # 1. Use current gain and base current to find collector current
    ic = hfe * ib

    # 2. Calculating collector bias voltage (vc)
    vc = vcc - ic*r_collector # RETURN VALUE I

    # 3. Calculating emitter voltage at saturation
    ic_sat = (vcc - vce_sat) / (r_collector + r_emitter)
    ve_sat = ic_sat * r_emitter

    # 4. Calculating collector bias voltage for max headroom
    target_vc = (vcc + vce_sat + ve_sat) / 2 # RETURN VALUE II

    return vc, target_vc


def calculate_emitter_follower(vcc, r_upper, r_lower, r_base,
                               r_emitter, hfe, vbe, vce_sat):
    """Calculates loaded emitter voltage for emitter follower buffer
    and target voltage for maximum headroom"""
    
    # 1. Base network thevenin equivalent and base current
    vth = vcc * (r_lower/(r_upper + r_lower))
    rth = ((r_lower*r_upper)/(r_lower + r_upper)) + r_base
    ib = (vth - vbe) / (rth + ((hfe + 1)*r_emitter))

    # 2. Use base current to find loaded base voltage
    vb = vth - (ib * rth)

    # 3. Calculate emitter voltage using base-emitter drop
    ve = vb - vbe # RETURN VALUE I

    # 4. Find max headroom target
    target_ve = (vcc - vce_sat) / 2 # RETURM VALUE II

    return ve, target_ve