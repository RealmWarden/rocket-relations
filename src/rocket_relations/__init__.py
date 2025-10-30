"""
Ideal rocket propulsion relations package.
This package contains functions for calculating characteristic velocity and thrust coefficient.
"""

from .ideal import cStar, thrustCoeff
__all__ = ["cStar", "thrustCoeff"]