from _config.configEqCim17 import configEqCim17
from _config.configSshCim17 import configSshCim17
from _config.configAsCim17 import configAsCim17
from _config.configBaseVoltageCim17 import configBaseVoltageCim17
from _config.configGeographicalRegionCim17 import configGeographicalRegionCim17
from _config.configBmCim17 import configBmCim17
from _config.configDlCim17 import configDlCim17
from _config.configGlCim17 import configGlCim17
from _config.configOpCim17 import configOpCim17
from _config.configScCim17 import configScCim17
from _config.configAcCim17 import configAcCim17
from _config.configMeasurementValueSourceCim17 import configMeasurementValueSourceCim17
from _config.configReadingQualityTypeCim17 import configReadingQualityTypeCim17
from _config.configReadingTypeCim17 import configReadingTypeCim17
from _config.configCuCim17 import configCuCim17
from _config.configSvCim17 import configSvCim17
from _config.configTpCim17 import configTpCim17
from _config.configOrCim17 import configOrCim17

def configPicker(doctype, docTopic):
    configType = (doctype, docTopic)
    match configType:
        case ("EQ", "Equipment"):
            config = configEqCim17
        case ("SSH", "Steady State Hypothesis"):
            config = configSshCim17
        case ("AS", "Asset"):
            config = configAsCim17
        case ("RD", "Base Voltage"):
            config = configBaseVoltageCim17
        case ("RD", "Geographical Region"):
            config = configGeographicalRegionCim17
        case ("BM", "Boundry"):
            config = configBmCim17
        case ("DL", "Diagram Layout"):
            config = configDlCim17
        case ("GL", "Geographical Location"):
            config = configGlCim17
        case ("OP", "Operation"):
            config = configOpCim17
        case ("SC", "Short Circuit"):
            config = configScCim17
        case ("AC", "Asset Catalogue"):
            config = configAcCim17
        case ("RD", "Measurement Value Source"):
            config = configMeasurementValueSourceCim17
        case ("RD", "Reading Quality Type"):
            config = configReadingQualityTypeCim17
        case ("RD", "Reading Type"):
            config = configReadingTypeCim17
        case ("CU", "Customer"):
            config = configCuCim17
        case ("SV", "State Variables"):
            config = configSvCim17
        case ("TP", "Topology"):
            config = configTpCim17
        case ("OR", "Object Reference"):
            config = configOrCim17
    return config