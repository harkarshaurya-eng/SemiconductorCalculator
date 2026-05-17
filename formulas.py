"""Formula functions for the Semiconductor Formula Calculator."""

import math

# Physical constants used throughout the project.
q = 1.602e-19
k = 1.381e-23
h = 6.626e-34
c = 3e8


def calculate_conductivity(electron_concentration, hole_concentration, electron_mobility, hole_mobility):
    """Return semiconductor conductivity in siemens per meter (S/m)."""
    return q * (
        (electron_concentration * electron_mobility)
        + (hole_concentration * hole_mobility)
    )


def calculate_resistivity(conductivity):
    """Return resistivity in ohm-meter."""
    if conductivity == 0:
        raise ValueError("Conductivity must not be zero.")
    return 1 / conductivity


def calculate_ni_from_n_and_p(electron_concentration, hole_concentration):
    """Return intrinsic carrier concentration ni from n and p."""
    return math.sqrt(electron_concentration * hole_concentration)


def calculate_n_from_ni_and_p(intrinsic_concentration, hole_concentration):
    """Return electron concentration n from ni and p."""
    if hole_concentration == 0:
        raise ValueError("Hole concentration p must not be zero.")
    return (intrinsic_concentration ** 2) / hole_concentration


def calculate_p_from_ni_and_n(intrinsic_concentration, electron_concentration):
    """Return hole concentration p from ni and n."""
    if electron_concentration == 0:
        raise ValueError("Electron concentration n must not be zero.")
    return (intrinsic_concentration ** 2) / electron_concentration


def calculate_n_type_majority_carrier(donor_concentration):
    """In n-type semiconductor, majority electron concentration is approximately Nd."""
    return donor_concentration


def calculate_p_type_majority_carrier(acceptor_concentration):
    """In p-type semiconductor, majority hole concentration is approximately Na."""
    return acceptor_concentration


def calculate_n_type_minority_holes(intrinsic_concentration, donor_concentration):
    """Return minority hole concentration in an n-type semiconductor."""
    if donor_concentration == 0:
        raise ValueError("Donor concentration Nd must not be zero.")
    return (intrinsic_concentration ** 2) / donor_concentration


def calculate_p_type_minority_electrons(intrinsic_concentration, acceptor_concentration):
    """Return minority electron concentration in a p-type semiconductor."""
    if acceptor_concentration == 0:
        raise ValueError("Acceptor concentration Na must not be zero.")
    return (intrinsic_concentration ** 2) / acceptor_concentration


def calculate_band_gap_energy(wavelength_nm):
    """Return band gap energy in electron-volt (eV)."""
    if wavelength_nm <= 0:
        raise ValueError("Wavelength must be greater than zero.")
    return 1240 / wavelength_nm


def calculate_photon_energy_joule(wavelength_nm):
    """Return photon energy in joule."""
    if wavelength_nm <= 0:
        raise ValueError("Wavelength must be greater than zero.")
    wavelength_m = wavelength_nm * 1e-9
    return (h * c) / wavelength_m


def calculate_photon_energy_ev(wavelength_nm):
    """Return photon energy in electron-volt (eV)."""
    if wavelength_nm <= 0:
        raise ValueError("Wavelength must be greater than zero.")
    return 1240 / wavelength_nm


def calculate_thermal_voltage(temperature_kelvin):
    """Return thermal voltage VT in volt."""
    if temperature_kelvin <= 0:
        raise ValueError("Temperature must be greater than zero Kelvin.")
    return (k * temperature_kelvin) / q


def calculate_diode_current(reverse_saturation_current, applied_voltage, ideality_factor, thermal_voltage):
    """Return diode current from the Shockley diode equation."""
    if reverse_saturation_current < 0:
        raise ValueError("Reverse saturation current I0 cannot be negative.")
    if ideality_factor <= 0:
        raise ValueError("Ideality factor eta must be greater than zero.")
    if thermal_voltage <= 0:
        raise ValueError("Thermal voltage VT must be greater than zero.")

    exponent_value = applied_voltage / (ideality_factor * thermal_voltage)

    # math.exp overflows for very large positive numbers, so we stop early.
    if exponent_value > 700:
        raise ValueError("The entered values are too large for the diode current calculation.")

    return reverse_saturation_current * (math.exp(exponent_value) - 1)


def get_cut_in_voltage_info():
    """Return approximate cut-in voltage values."""
    return {
        "Silicon diode": 0.7,
        "Germanium diode": 0.3,
    }


def calculate_drift_current(carrier_concentration, area, drift_velocity):
    """Return drift current in ampere."""
    return carrier_concentration * q * area * drift_velocity


def calculate_drift_velocity(mobility, electric_field):
    """Return drift velocity in meter per second."""
    return mobility * electric_field


def calculate_electric_field(voltage, length):
    """Return electric field in volt per meter."""
    if length == 0:
        raise ValueError("Length must not be zero.")
    return voltage / length


def calculate_current_density(conductivity, electric_field):
    """Return current density in ampere per square meter."""
    return conductivity * electric_field


def calculate_hall_coefficient(carrier_concentration, semiconductor_type):
    """Return Hall coefficient in m^3/C with sign based on semiconductor type."""
    if carrier_concentration == 0:
        raise ValueError("Carrier concentration must not be zero.")

    hall_coefficient = 1 / (carrier_concentration * q)
    semiconductor_type = semiconductor_type.lower()

    if semiconductor_type == "n":
        return -hall_coefficient
    if semiconductor_type == "p":
        return hall_coefficient

    raise ValueError("Semiconductor type must be 'n' or 'p'.")


def calculate_hall_voltage(hall_coefficient, current, magnetic_field, thickness):
    """Return Hall voltage in volt."""
    if thickness == 0:
        raise ValueError("Thickness must not be zero.")
    return (hall_coefficient * current * magnetic_field) / thickness


def get_fermi_level_explanation():
    """Return a beginner-friendly explanation for the intrinsic Fermi level."""
    return (
        "For an intrinsic semiconductor, the Fermi level is approximately at the "
        "middle of the forbidden energy gap. This means electrons and holes are "
        "balanced in a pure semiconductor material."
    )


def detect_semiconductor_type(electron_concentration, hole_concentration):
    """Identify semiconductor type from electron and hole concentrations."""
    if electron_concentration > hole_concentration:
        return "N-type semiconductor"
    if hole_concentration > electron_concentration:
        return "P-type semiconductor"
    return "Intrinsic semiconductor"
