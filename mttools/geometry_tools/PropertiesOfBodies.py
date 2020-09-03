from math import pi
from typing import Tuple, Dict

from mttools.utils.types import RealNumber


def rect_bar(depth: RealNumber, thickness: RealNumber) -> Dict[str, float]:
    """
    Calculates the Centroid, Area, Moment of Inetia, and Section Modulus  of a rectangular bar.
        The assumed orientation is with the depth along the y axis so that
        Ixx is strong axis and Iyy is weak axis.

    >>> rect_bar(3, 0.5)
    {'Centroid X': 0.25, 'Centroid Y': 1.5, 'Area': 1.5,
     'Ixx': 1.125, 'Iyy': 0.03125, 'Sx': 0.75, 'Sy': 0.125}

    """
    if any((depth <= 0, thickness <= 0)):
        raise ValueError("All dimensions must be greater than 0")

    y = depth / 2
    x = thickness / 2
    area = depth * thickness
    Ixx = depth ** 3 * thickness / 12
    Iyy = thickness ** 3 * depth / 12
    return {
        "Centroid X": x,
        "Centroid Y": y,
        "Area": area,
        "Ixx": Ixx,
        "Iyy": Iyy,
        "Sx": Ixx / y,
        "Sy": Iyy / x,
    }


def round_bar(
    outside_diameter: RealNumber, inside_diameter: RealNumber = None
) -> Dict[str, float]:
    """
    Calculates the Centroid, Area, Moment of Inetia, and Section Modulus  of a round bar.
        The assumed orientation is with the depth along the y axis so that
        Ixx is strong axis and Iyy is weak axis.

    >>> round_bar(18, 15)
    {'Centroid': 9.0, 'Area': 77.75441817634739,
     'Ixx': 2667.9484736759196, 'Sxx': 296.4387192973244}

    >>> round_bar(13, 0)
    {'Centroid': 6.5, 'Area': 132.73228961416876,
     'Ixx': 1401.9848090496575, 'Sxx': 215.68997062302424}

    >>> round_bar(8)
    {'Centroid': 4.0, 'Area': 50.26548245743669,
     'Ixx': 201.06192982974676, 'Sxx': 50.26548245743669}
    """
    if not inside_diameter:
        inside_diameter = 0

    if any((outside_diameter <= 0, inside_diameter < 0)):
        raise ValueError("All dimensions must be greater than 0")

    y = outside_diameter / 2
    area = pi * (outside_diameter ** 2 - inside_diameter ** 2) / 4
    Ixx = pi * (outside_diameter ** 4 - inside_diameter ** 4) / 64
    return {
        "Centroid": y,
        "Area": area,
        "Ixx": Ixx,
        "Sxx": Ixx / y,
    }


def Tbeam(
    depth: RealNumber,
    web_thickness: RealNumber,
    flange_width: RealNumber,
    flange_thickness: RealNumber,
) -> Dict[str, float]:
    """
    Calculates the Centroid, Area, Moment of Inetia, and Section Modulus  of a T beam.
        The assumed orientation is with the depth along the y axis and the flange on top
        so that Ixx is strong axis and Iyy is weak axis.

        The web is assumed to be centered on the flange.

        depth is the total depth of the web (stem) and flange

    >>> Tbeam(4, 0.5, 4, 0.5)
    {'Centroid X': 2.0, 'Centroid Y': 2.8166666666666664, 'Area': 3.75,
     'Ixx': 5.5614583333333325, 'Iyy': 2.703125,
     'Sx': 1.9744822485207099, 'Sy': 1.3515625}
    """
    if any((depth <= 0, web_thickness <= 0, flange_width <= 0, flange_thickness <= 0)):
        raise ValueError("All dimensions must be greater than 0")

    web_height = depth - web_thickness
    y = depth - (
        (
            depth ** 2 * web_thickness
            + flange_thickness ** 2 * (flange_width - web_thickness)
        )
        / (2 * (flange_width * flange_thickness + web_height * web_thickness))
    )
    x = flange_width / 2
    area = flange_width * flange_thickness + web_height * web_thickness
    Ixx = (
        1
        / 3
        * (
            web_thickness * y ** 3
            + flange_width * (depth - y) ** 3
            - (flange_width - web_thickness) * (depth - y - flange_thickness) ** 3
        )
    )
    Iyy = (
        web_thickness ** 3 * web_height / 12 + flange_width ** 3 * flange_thickness / 12
    )
    return {
        "Centroid X": x,
        "Centroid Y": y,
        "Area": area,
        "Ixx": Ixx,
        "Iyy": Iyy,
        "Sx": Ixx / y,
        "Sy": Iyy / x,
    }


def Ibeam_equal_flange(
    depth: RealNumber,
    web_thickness: RealNumber,
    flange_width: RealNumber,
    flange_thickness: RealNumber,
) -> Dict[str, float]:
    """
    Calculates the Centroid, Area, Moment of Inetia, and Section Modulus  of an I beam.
        The assumed orientation is with the depth along the y axis so that
        Ixx is strong axis and Iyy is weak axis.

        The web is assumed to be centered on the flanges.

        depth is the total depth of the web (stem) and flange

    >>> Ibeam_equal_flange(8, 0.5, 6, 0.75)
    {'Centroid X': 3.0, 'Centroid Y': 4.0, 'Area': 12.25,
     'Ixx': 130.13020833333334, 'Iyy': 27.067708333333332,
     'Sx': 32.532552083333336, 'Sy': 9.022569444444445}
    """
    if any((depth <= 0, web_thickness <= 0, flange_width <= 0, flange_thickness <= 0)):
        raise ValueError("All dimensions must be greater than 0")

    web_height = depth - 2 * flange_thickness
    y = depth / 2
    x = flange_width / 2
    area = 2 * flange_width * flange_thickness + web_height * web_thickness
    Ixx = (
        flange_width * depth ** 3 - web_height ** 3 * (flange_width - web_thickness)
    ) / 12
    Iyy = (
        2 * (flange_width ** 3 * flange_thickness / 12)
        + web_thickness ** 3 * web_height / 12
    )
    return {
        "Centroid X": x,
        "Centroid Y": y,
        "Area": area,
        "Ixx": Ixx,
        "Iyy": Iyy,
        "Sx": Ixx / y,
        "Sy": Iyy / x,
    }


def Ibeam_unequal_flange(
    depth: RealNumber,
    web_thickness: RealNumber,
    top_flange: Tuple[RealNumber, RealNumber],
    btm_flange: Tuple[RealNumber, RealNumber],
) -> Dict[str, float]:
    """
    Calculates the Centroid, Area, Moment of Inetia, and Section Modulus  of an I beam.
        The assumed orientation is with the depth along the y axis so that
        Ixx is strong axis and Iyy is weak axis.

        The web is assumed to be centered on the flanges.

        depth is the total depth of the web (stem) and flange

        top flange / btm flange inputs are (width, thickness)

    >>> Ibeam_unequal_flange(8, 0.5, (9, 0.75), (6, 1))
    {'Centroid X': 4.5, 'Centroid Y': 4.243110236220472, 'Area': 15.875,
    'Ixx': 172.29872559875326, 'Iyy': 63.627604166666664,
    'Sx': 40.60670498917498, 'Sy': 14.139467592592592}
    """
    top_flange_width, top_flange_thickness = top_flange
    btm_flange_width, btm_flange_thickness = btm_flange
    if any(
        (
            depth <= 0,
            web_thickness <= 0,
            top_flange_width <= 0,
            top_flange_thickness <= 0,
            btm_flange_width <= 0,
            btm_flange_thickness <= 0,
        )
    ):
        raise ValueError("All dimensions must be greater than 0")

    web_height = depth - top_flange_thickness - btm_flange_thickness
    area = (
        top_flange_width * top_flange_thickness
        + web_height * web_thickness
        + btm_flange_width * btm_flange_thickness
    )
    y1 = (
        web_thickness * depth ** 2
        + btm_flange_thickness ** 2 * (btm_flange_width - web_thickness)
        + top_flange_thickness
        * (top_flange_width - web_thickness)
        * (2 * depth - top_flange_thickness)
    ) / (2 * area)
    y = max((y1, depth - y1))
    x = max((top_flange_width, btm_flange_width)) / 2
    Ixx = (
        web_thickness * depth ** 3 / 3
        + (btm_flange_width - web_thickness) * (btm_flange_thickness) ** 3 / 3
        + (top_flange_width - web_thickness)
        * (depth ** 3 - (depth - top_flange_thickness) ** 3)
        / 3
        - area * y1 ** 2
    )
    Iyy = (
        top_flange_width ** 3 * top_flange_thickness / 12
        + btm_flange_width ** 3 * btm_flange_thickness / 12
        + web_thickness ** 3 * web_height / 12
    )
    return {
        "Centroid X": x,
        "Centroid Y": y1,
        "Area": area,
        "Ixx": Ixx,
        "Iyy": Iyy,
        "Sx": Ixx / y,
        "Sy": Iyy / x,
    }
