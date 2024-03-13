import openvsp as vsp
import itertools
import numpy as np
import json

# Declare Constants

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

# Check OpenVSP
vsp.VSPCheckSetup()

def unpack_des_vars(des_var_dict:dict):
    for i in des_var_dict.keys():
        list_vals = des_var_dict[i]
        des_var_dict[i] = np.linspace(list_vals[0], list_vals[1], list_vals[2])
    keys, values = zip(*des_var_dict.items())
    permutations = [dict(zip(keys, v)) for v in itertools.product(*values)]
    return permutations

def aero_sweep_analysis(vsp_fpath:str, des_vars:dict, sim_params:dict, wing_id:str):

    # Checking that vsp is working

    # Read in file
    vsp.ReadVSPFile(vsp_fpath) 

    # Loading des_vars
    for param in des_vars.keys():
        group, param_name = param.split()
        param_id = vsp.GetParm(wing_id, param_name, group)
        vsp.SetParmVal(param_id, des_vars[param])
    vsp.Update()
  
    # Degen Geometry
    analysis_name = "VSPAEROComputeGeometry"
    vsp.SetAnalysisInputDefaults(analysis_name)
    method = list(vsp.GetIntAnalysisInput(analysis_name, "AnalysisMethod"))
    method[0] = vsp.VORTEX_LATTICE
    vsp.SetIntAnalysisInput(analysis_name, "AnalysisMethod", method)
    vsp.ExecAnalysis(analysis_name)

    # VSPAEROSweep
    analysis_name = "VSPAEROSweep"
    vsp.SetAnalysisInputDefaults(analysis_name)
    
    
    vsp.SetStringAnalysisInput(analysis_name, "WingID", wing_id, 0)

    # Update the inputs
    for key in sweep_inputs.keys():
        if AEROSWEEP_PARAM_TYPES[key] == "INT_DATA":
            vsp.SetIntAnalysisInput(analysis_name, key, (int(sweep_inputs[key]),), 0)
        if AEROSWEEP_PARAM_TYPES[key] == "DOUBLE_DATA":
            vsp.SetDoubleAnalysisInput(analysis_name, key, (float(sweep_inputs[key]),), 0)
    vsp.Update()

    # Execute the analysis
    vsp.ExecAnalysis(analysis_name)
    resp = vsp.FindLatestResultsID("VSPAERO_History")
    CL = vsp.GetDoubleResults(resp, "CL")
    print(CL)
    return CL

def analyze(vsp_fpath:str, des_var_json_path, sim_params, wing_id):
    
    des_var_json = json.load(des_var_json_path)
    des_var_sets = unpack_des_vars(des_var_json)
    for var_set in des_var_sets:
        vsp.WriteResultsCSVFile


if __name__ == "__main__":
    WingName = "WingGeom"
    
    sweep_inputs = {
        "AlphaStart": 2.0,
        "AlphaNpts": 1,
        "MachStart": 0.0,
        "MachNpts": 1
    }

    des_vars = {
        "Dihedral WingGeom": [-10, 0, 3],
        "Sweep WingGeom": [-35, -1, 3],
        "Aspect WingGeom": [8, 12, 3]
    }
    aero_sweep_analysis("Deploy/Files/Check.vsp3", des_vars, sweep_inputs, WingName)
