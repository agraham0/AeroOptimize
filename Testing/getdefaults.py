import openvsp as vsp

AEROSWEEP_PARAM_TYPES =  {
    "2DFEMFlag": "INT_DATA",
    "ActuatorDiskFlag": "INT_DATA",
    "AlphaEnd": "DOUBLE_DATA",
    "AlphaNpts": "INT_DATA",
    "AlphaStart": "DOUBLE_DATA",
    "AlternateInputFormatFlag": "INT_DATA",
    "AnalysisMethod": "INT_DATA",
    "AutoTimeNumRevs": "INT_DATA",
    "AutoTimeStepFlag": "INT_DATA",
    "BetaEnd": "DOUBLE_DATA",
    "BetaNpts": "INT_DATA",
    "BetaStart": "DOUBLE_DATA",
    "CGGeomSet": "INT_DATA",
    "Clmax": "DOUBLE_DATA",
    "ClmaxToggle": "INT_DATA",
    "FarDist": "DOUBLE_DATA",
    "FarDistToggle": "INT_DATA",
    "FixedWakeFlag": "INT_DATA",
    "FromSteadyState": "INT_DATA",
    "GeomSet": "INT_DATA",
    "GroundEffect": "DOUBLE_DATA",
    "GroundEffectToggle": "INT_DATA",
    "HoverRamp": "DOUBLE_DATA",
    "HoverRampFlag": "INT_DATA",
    "KTCorrection": "INT_DATA",
    "MachEnd": "DOUBLE_DATA",
    "MachNpts": "INT_DATA",
    "MachStart": "DOUBLE_DATA",
    "Machref": "DOUBLE_DATA",
    "ManualVrefFlag": "INT_DATA",
    "MassSliceDir": "INT_DATA",
    "MaxTurnAngle": "DOUBLE_DATA",
    "MaxTurnToggle": "INT_DATA",
    "NCPU": "INT_DATA",
    "NoiseCalcFlag": "INT_DATA",
    "NoiseCalcType": "INT_DATA",
    "NoiseUnits": "INT_DATA",
    "NumMassSlice": "INT_DATA",
    "NumTimeSteps": "INT_DATA",
    "NumWakeNodes": "INT_DATA",
    "Precondition": "INT_DATA",
    "ReCref": "DOUBLE_DATA",
    "ReCrefEnd": "DOUBLE_DATA",
    "ReCrefNpts": "INT_DATA",
    "RedirectFile": "STRING_DATA",
    "RefFlag": "INT_DATA",
    "Rho": "DOUBLE_DATA",
    "RotateBladesFlag": "INT_DATA",
    "Sref": "DOUBLE_DATA",
    "Symmetry": "INT_DATA",
    "TimeStepSize": "DOUBLE_DATA",
    "UnsteadyType": "INT_DATA",
    "Vinf": "DOUBLE_DATA",
    "Vref": "DOUBLE_DATA",
    "WakeNumIter": "INT_DATA",
    "WingID": "STRING_DATA",
    "Xcg": "DOUBLE_DATA",
    "Ycg": "DOUBLE_DATA",
    "Zcg": "DOUBLE_DATA",
    "bref": "DOUBLE_DATA",
    "cref": "DOUBLE_DATA"
  }

vsp.VSPCheckSetup()

analysis_name = "VSPAEROSweep"
vsp.SetAnalysisInputDefaults(analysis_name)

defs = {}

for key in AEROSWEEP_PARAM_TYPES.keys():
    if AEROSWEEP_PARAM_TYPES[key] == "INT_DATA":
        defs[key] = list(vsp.GetIntAnalysisInput(analysis_name, key))
    if AEROSWEEP_PARAM_TYPES[key] == "DOUBLE_DATA":
        defs[key] = list(vsp.GetDoubleAnalysisInput(analysis_name, key))
    if AEROSWEEP_PARAM_TYPES[key] == "STRING_DATA":
        defs[key] = list(vsp.GetStringAnalysisInput(analysis_name, key))
print(defs)
