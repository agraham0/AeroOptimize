import openvsp as vsp

vsp.VSPCheckSetup()

analysis_name = "VSPAEROSweep"

vsp.SetAnalysisInputDefaults("VSPAEROSweep")
inputs = vsp.GetAnalysisInputNames("VSPAEROSweep")

param_type = {}

RES_DATA_TYPE = {-1:"INVALID_TYPE", 0:"INT_DATA", 1:"DOUBLE_DATA", 2:"STRING_DATA", 3:"VEC3D_DATA", 4:"DOUBLE_MATRIX_DATA"}

for param in inputs:
    param_type[param] = RES_DATA_TYPE[vsp.GetAnalysisInputType(analysis_name, param)]

print(param_type)


