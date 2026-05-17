"""Main menu program for the Semiconductor Formula Calculator."""

import formulas
from utils import ask_continue, print_formula, print_header, safe_float_input, safe_int_input, show_result


def display_menu():
    """Show the main menu."""
    print()
    print_header()
    print("1. Conductivity")
    print("2. Resistivity")
    print("3. Intrinsic Carrier Concentration Relation")
    print("4. Majority Carrier Concentration")
    print("5. Minority Carrier Concentration")
    print("6. Band Gap Energy")
    print("7. Photon Energy")
    print("8. Thermal Voltage")
    print("9. Diode Current")
    print("10. Cut-in Voltage Info")
    print("11. Drift Current")
    print("12. Drift Velocity")
    print("13. Electric Field")
    print("14. Current Density")
    print("15. Hall Coefficient")
    print("16. Hall Voltage")
    print("17. Fermi Level Explanation")
    print("18. Semiconductor Type Detector")
    print("19. Exit")


def handle_conductivity():
    """Calculate semiconductor conductivity."""
    print_formula(
        "Conductivity",
        [
            "Formula: sigma = q(n*mu_n + p*mu_p)",
            f"Constant used: q = {formulas.q:.3e} C",
        ],
    )
    electron_concentration = safe_float_input("Enter electron concentration n (per m^3): ", allow_negative=False)
    hole_concentration = safe_float_input("Enter hole concentration p (per m^3): ", allow_negative=False)
    electron_mobility = safe_float_input("Enter electron mobility mu_n (m^2/V.s): ", allow_negative=False)
    hole_mobility = safe_float_input("Enter hole mobility mu_p (m^2/V.s): ", allow_negative=False)

    conductivity = formulas.calculate_conductivity(
        electron_concentration,
        hole_concentration,
        electron_mobility,
        hole_mobility,
    )
    show_result("Conductivity", conductivity, "S/m")


def handle_resistivity():
    """Calculate resistivity from conductivity."""
    print_formula(
        "Resistivity",
        [
            "Formula: rho = 1 / sigma",
            "Conductivity sigma must be non-zero.",
        ],
    )
    conductivity = safe_float_input("Enter conductivity sigma (S/m): ", allow_zero=False, allow_negative=False)
    resistivity = formulas.calculate_resistivity(conductivity)
    show_result("Resistivity", resistivity, "ohm-m")


def handle_intrinsic_relation():
    """Handle all forms of np = ni^2."""
    print_formula(
        "Intrinsic Carrier Concentration Relation",
        [
            "Formula: np = ni^2",
            "1. Calculate ni = sqrt(n*p)",
            "2. Calculate n = ni^2 / p",
            "3. Calculate p = ni^2 / n",
        ],
    )
    choice = safe_int_input("Choose an option (1-3): ", minimum=1, maximum=3)

    if choice == 1:
        electron_concentration = safe_float_input("Enter electron concentration n (per m^3): ", allow_negative=False)
        hole_concentration = safe_float_input("Enter hole concentration p (per m^3): ", allow_negative=False)
        intrinsic_concentration = formulas.calculate_ni_from_n_and_p(
            electron_concentration,
            hole_concentration,
        )
        show_result("Intrinsic carrier concentration ni", intrinsic_concentration, "per m^3")
    elif choice == 2:
        intrinsic_concentration = safe_float_input("Enter intrinsic concentration ni (per m^3): ", allow_negative=False)
        hole_concentration = safe_float_input("Enter hole concentration p (per m^3): ", allow_zero=False, allow_negative=False)
        electron_concentration = formulas.calculate_n_from_ni_and_p(
            intrinsic_concentration,
            hole_concentration,
        )
        show_result("Electron concentration n", electron_concentration, "per m^3")
    else:
        intrinsic_concentration = safe_float_input("Enter intrinsic concentration ni (per m^3): ", allow_negative=False)
        electron_concentration = safe_float_input("Enter electron concentration n (per m^3): ", allow_zero=False, allow_negative=False)
        hole_concentration = formulas.calculate_p_from_ni_and_n(
            intrinsic_concentration,
            electron_concentration,
        )
        show_result("Hole concentration p", hole_concentration, "per m^3")


def handle_majority_carrier():
    """Calculate majority carrier concentration."""
    print_formula(
        "Majority Carrier Concentration",
        [
            "1. For n-type semiconductor: n ~= Nd",
            "2. For p-type semiconductor: p ~= Na",
        ],
    )
    choice = safe_int_input("Choose an option (1-2): ", minimum=1, maximum=2)

    if choice == 1:
        donor_concentration = safe_float_input("Enter donor concentration Nd (per m^3): ", allow_negative=False)
        electron_concentration = formulas.calculate_n_type_majority_carrier(donor_concentration)
        show_result("Electron concentration n", electron_concentration, "per m^3")
    else:
        acceptor_concentration = safe_float_input("Enter acceptor concentration Na (per m^3): ", allow_negative=False)
        hole_concentration = formulas.calculate_p_type_majority_carrier(acceptor_concentration)
        show_result("Hole concentration p", hole_concentration, "per m^3")


def handle_minority_carrier():
    """Calculate minority carrier concentration."""
    print_formula(
        "Minority Carrier Concentration",
        [
            "1. In n-type semiconductor: p = ni^2 / Nd",
            "2. In p-type semiconductor: n = ni^2 / Na",
        ],
    )
    choice = safe_int_input("Choose an option (1-2): ", minimum=1, maximum=2)

    intrinsic_concentration = safe_float_input("Enter intrinsic concentration ni (per m^3): ", allow_negative=False)

    if choice == 1:
        donor_concentration = safe_float_input("Enter donor concentration Nd (per m^3): ", allow_zero=False, allow_negative=False)
        hole_concentration = formulas.calculate_n_type_minority_holes(
            intrinsic_concentration,
            donor_concentration,
        )
        show_result("Minority hole concentration p", hole_concentration, "per m^3")
    else:
        acceptor_concentration = safe_float_input("Enter acceptor concentration Na (per m^3): ", allow_zero=False, allow_negative=False)
        electron_concentration = formulas.calculate_p_type_minority_electrons(
            intrinsic_concentration,
            acceptor_concentration,
        )
        show_result("Minority electron concentration n", electron_concentration, "per m^3")


def handle_band_gap_energy():
    """Calculate band gap energy from wavelength."""
    print_formula(
        "Band Gap Energy",
        [
            "Formula: Eg = 1240 / lambda",
            "Eg is in eV when wavelength lambda is in nm.",
        ],
    )
    wavelength_nm = safe_float_input("Enter wavelength lambda (nm): ", allow_zero=False, allow_negative=False)
    band_gap_energy = formulas.calculate_band_gap_energy(wavelength_nm)
    show_result("Band gap energy Eg", band_gap_energy, "eV")


def handle_photon_energy():
    """Calculate photon energy in joule and electron-volt."""
    print_formula(
        "Photon Energy",
        [
            "Formula: E = hc / lambda",
            "Simplified form: E(eV) = 1240 / lambda(nm)",
            f"Constants used: h = {formulas.h:.3e} J.s, c = {formulas.c:.3e} m/s",
        ],
    )
    wavelength_nm = safe_float_input("Enter wavelength lambda (nm): ", allow_zero=False, allow_negative=False)
    photon_energy_joule = formulas.calculate_photon_energy_joule(wavelength_nm)
    photon_energy_ev = formulas.calculate_photon_energy_ev(wavelength_nm)
    show_result("Photon energy E", photon_energy_joule, "J")
    show_result("Photon energy E", photon_energy_ev, "eV")


def handle_thermal_voltage():
    """Calculate thermal voltage."""
    print_formula(
        "Thermal Voltage",
        [
            "Formula: VT = kT / q",
            f"Constants used: k = {formulas.k:.3e} J/K, q = {formulas.q:.3e} C",
        ],
    )
    temperature_kelvin = safe_float_input("Enter temperature T (K): ", allow_zero=False, allow_negative=False)
    thermal_voltage = formulas.calculate_thermal_voltage(temperature_kelvin)
    show_result("Thermal voltage VT", thermal_voltage, "V")


def handle_diode_current():
    """Calculate diode current from the Shockley diode equation."""
    print_formula(
        "Diode Current",
        [
            "Formula: I = I0(e^(V / (eta*VT)) - 1)",
            "I0 = reverse saturation current, V = applied voltage",
            "eta = ideality factor, VT = thermal voltage",
        ],
    )
    reverse_saturation_current = safe_float_input("Enter reverse saturation current I0 (A): ", allow_negative=False)
    applied_voltage = safe_float_input("Enter applied voltage V (V): ", allow_negative=True)
    ideality_factor = safe_float_input("Enter ideality factor eta: ", allow_zero=False, allow_negative=False)
    thermal_voltage = safe_float_input("Enter thermal voltage VT (V): ", allow_zero=False, allow_negative=False)

    diode_current = formulas.calculate_diode_current(
        reverse_saturation_current,
        applied_voltage,
        ideality_factor,
        thermal_voltage,
    )
    show_result("Diode current I", diode_current, "A")


def handle_cut_in_voltage():
    """Display cut-in voltage information."""
    print_formula(
        "Cut-in Voltage Information",
        [
            "Approximate cut-in voltage values for common diodes:",
        ],
    )
    cut_in_values = formulas.get_cut_in_voltage_info()
    for diode_name, voltage in cut_in_values.items():
        print(f"{diode_name}: {voltage} V")


def handle_drift_current():
    """Calculate drift current."""
    print_formula(
        "Drift Current",
        [
            "Formula: Idrift = n*q*A*vd",
            f"Constant used: q = {formulas.q:.3e} C",
        ],
    )
    carrier_concentration = safe_float_input("Enter carrier concentration n (per m^3): ", allow_negative=False)
    area = safe_float_input("Enter cross-sectional area A (m^2): ", allow_negative=False)
    drift_velocity = safe_float_input("Enter drift velocity vd (m/s): ", allow_negative=False)
    drift_current = formulas.calculate_drift_current(carrier_concentration, area, drift_velocity)
    show_result("Drift current Idrift", drift_current, "A")


def handle_drift_velocity():
    """Calculate drift velocity."""
    print_formula(
        "Drift Velocity",
        [
            "Formula: vd = mu*E",
        ],
    )
    mobility = safe_float_input("Enter mobility mu (m^2/V.s): ", allow_negative=False)
    electric_field = safe_float_input("Enter electric field E (V/m): ", allow_negative=False)
    drift_velocity = formulas.calculate_drift_velocity(mobility, electric_field)
    show_result("Drift velocity vd", drift_velocity, "m/s")


def handle_electric_field():
    """Calculate electric field."""
    print_formula(
        "Electric Field",
        [
            "Formula: E = V / L",
        ],
    )
    voltage = safe_float_input("Enter voltage V (V): ", allow_negative=True)
    length = safe_float_input("Enter length L (m): ", allow_zero=False, allow_negative=False)
    electric_field = formulas.calculate_electric_field(voltage, length)
    show_result("Electric field E", electric_field, "V/m")


def handle_current_density():
    """Calculate current density."""
    print_formula(
        "Current Density",
        [
            "Formula: J = sigma*E",
        ],
    )
    conductivity = safe_float_input("Enter conductivity sigma (S/m): ", allow_negative=False)
    electric_field = safe_float_input("Enter electric field E (V/m): ", allow_negative=False)
    current_density = formulas.calculate_current_density(conductivity, electric_field)
    show_result("Current density J", current_density, "A/m^2")


def handle_hall_coefficient():
    """Calculate Hall coefficient."""
    print_formula(
        "Hall Coefficient",
        [
            "Formula: RH = 1 / (n*q)",
            "For n-type semiconductor, RH is negative.",
            "For p-type semiconductor, RH is positive.",
        ],
    )
    semiconductor_type = input("Enter semiconductor type (n/p): ").strip().lower()
    while semiconductor_type not in ("n", "p"):
        print("Please enter 'n' for n-type or 'p' for p-type.")
        semiconductor_type = input("Enter semiconductor type (n/p): ").strip().lower()

    carrier_concentration = safe_float_input("Enter carrier concentration (per m^3): ", allow_zero=False, allow_negative=False)
    hall_coefficient = formulas.calculate_hall_coefficient(carrier_concentration, semiconductor_type)
    show_result("Hall coefficient RH", hall_coefficient, "m^3/C")


def handle_hall_voltage():
    """Calculate Hall voltage."""
    print_formula(
        "Hall Voltage",
        [
            "Formula: VH = RH*I*B / t",
            "RH = Hall coefficient, I = current, B = magnetic field, t = thickness",
        ],
    )
    hall_coefficient = safe_float_input("Enter Hall coefficient RH (m^3/C): ", allow_negative=True)
    current = safe_float_input("Enter current I (A): ", allow_negative=True)
    magnetic_field = safe_float_input("Enter magnetic field B (T): ", allow_negative=True)
    thickness = safe_float_input("Enter thickness t (m): ", allow_zero=False, allow_negative=False)
    hall_voltage = formulas.calculate_hall_voltage(hall_coefficient, current, magnetic_field, thickness)
    show_result("Hall voltage VH", hall_voltage, "V")


def handle_fermi_level():
    """Display a simple Fermi level explanation."""
    print_formula(
        "Fermi Level Explanation",
        [
            "Conceptual result for an intrinsic semiconductor:",
        ],
    )
    print(formulas.get_fermi_level_explanation())


def handle_semiconductor_type_detector():
    """Detect whether the semiconductor is n-type, p-type, or intrinsic."""
    print_formula(
        "Semiconductor Type Detector",
        [
            "Rule:",
            "If n > p, the material is n-type.",
            "If p > n, the material is p-type.",
            "If n = p, the material is intrinsic.",
        ],
    )
    electron_concentration = safe_float_input("Enter electron concentration n (per m^3): ", allow_negative=False)
    hole_concentration = safe_float_input("Enter hole concentration p (per m^3): ", allow_negative=False)
    semiconductor_type = formulas.detect_semiconductor_type(electron_concentration, hole_concentration)
    print(f"\nDetected type: {semiconductor_type}")


def run_selected_option(choice):
    """Call the correct function based on the menu choice."""
    # Each menu number is connected to one clear function.
    if choice == 1:
        handle_conductivity()
    elif choice == 2:
        handle_resistivity()
    elif choice == 3:
        handle_intrinsic_relation()
    elif choice == 4:
        handle_majority_carrier()
    elif choice == 5:
        handle_minority_carrier()
    elif choice == 6:
        handle_band_gap_energy()
    elif choice == 7:
        handle_photon_energy()
    elif choice == 8:
        handle_thermal_voltage()
    elif choice == 9:
        handle_diode_current()
    elif choice == 10:
        handle_cut_in_voltage()
    elif choice == 11:
        handle_drift_current()
    elif choice == 12:
        handle_drift_velocity()
    elif choice == 13:
        handle_electric_field()
    elif choice == 14:
        handle_current_density()
    elif choice == 15:
        handle_hall_coefficient()
    elif choice == 16:
        handle_hall_voltage()
    elif choice == 17:
        handle_fermi_level()
    elif choice == 18:
        handle_semiconductor_type_detector()


def main():
    """Run the calculator until the user chooses to exit."""
    while True:
        # Show the menu again after each finished calculation.
        display_menu()
        choice = safe_int_input("\nEnter your choice (1-19): ", minimum=1, maximum=19)

        if choice == 19:
            print("\nThank you for using the Semiconductor Formula Calculator.")
            break

        try:
            run_selected_option(choice)
        except ValueError as error:
            # Friendly error messages make invalid physics values easier to understand.
            print(f"\nError: {error}")

        if not ask_continue():
            print("\nThank you for using the Semiconductor Formula Calculator.")
            break


if __name__ == "__main__":
    main()
