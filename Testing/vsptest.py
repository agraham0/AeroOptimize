import openvsp as vsp
import numpy as np

fname = "HERC3.vsp3"

#####

vsp.VSPCheckSetup()

vsp.ReadVSPFile(fname)

ids = vsp.FindGeoms()

wing_id = ids[1]
print(vsp.GetGeomName(wing_id))

wing_area_id = vsp.GetParm(wing_id, "TotalArea", "WingGeom")

vsp.SetParmVal(wing_area_id, 3200)

vsp.WriteVSPFile("Check.vsp3")

# Constant values

wing_area = 3200

# Values to iterate through
'''
dihedral = np.linspace(-10, 0, 11)

sweep = np.linspace(0, 36, 19)

aspect_ratio = np.linspace(8, 12, 5)

twist = np.linspace(-10, 10, 21)
print(sweep)
'''
# create _DegenGeom.csv file input for VLM
analysis_name = "VSPAEROComputeGeometry"
vsp.SetAnalysisInputDefaults(analysis_name)
method = list(vsp.GetIntAnalysisInput(analysis_name, "AnalysisMethod"))
method[0] = vsp.VORTEX_LATTICE
vsp.SetIntAnalysisInput(analysis_name, "AnalysisMethod", method)
vsp.PrintAnalysisInputs(analysis_name)
resp = vsp.ExecAnalysis(analysis_name)
vsp.PrintResults(resp)
