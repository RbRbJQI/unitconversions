from __future__ import division, unicode_literals, print_function, absolute_import

from .UnitConversionBase import *

class AOMAMP(UnitConversion):
    # This must be defined outside of init, and must match the default hardware unit specified within the BLACS tab
    base_unit = 'V'
    # derived_units = ['Vs']

    # You can pass a dictionary at class instantiation with some parameters to use in your unit converstion.
    # You can also place a list of "order of magnitude" prefixes (eg, k, m, M, u, p) you also want available
    # and the UnitConversion class will automatically generate the conversion function based on the functions
    # you specify for the "derived units". This list should be stored in the 'magnitudes' key of the parameters
    # dictionary

    def __init__(self,calibration_parameters = None):
        self.parameters = calibration_parameters

        self.derived_units = ['Vs']

        # Set default parameters if they are not speficied in calibration_parameters
        # self.parameters.setdefault('m',25*10**6)
        self.parameters.setdefault('shift',0)

        UnitConversion.__init__(self,self.parameters)

    def Vs_to_base(self,Vs):
        #here is the calibration code that may use self.parameters
        volts = Vs-self.parameters['shift']
        return volts
    def Vs_from_base(self,volts):
        #here is the calibration code that may use self.parameters
        Vs = volts  + self.parameters['shift']
        return Vs
