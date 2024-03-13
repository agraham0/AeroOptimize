import openvsp as vsp

vsp.VSPCheckSetup()

vsp.ReadVSPFile("Deploy/Files/Check.vsp3")

analysis_name = "VSPAEROComputeGeometry"
vsp.SetAnalysisInputDefaults(analysis_name)
method = list(vsp.GetIntAnalysisInput(analysis_name, "AnalysisMethod"))
method[0] = vsp.VORTEX_LATTICE
vsp.SetIntAnalysisInput(analysis_name, "AnalysisMethod", method)
# vsp.PrintAnalysisInputs(analysis_name)
vsp.ExecAnalysis(analysis_name)

analysis_name = "VSPAEROSweep"
vsp.SetAnalysisInputDefaults(analysis_name)
wid = vsp.FindGeomsWithName("WingGeom")
vsp.SetStringAnalysisInput(analysis_name, "WingID", wid, 0)
vsp.SetDoubleAnalysisInput(analysis_name, "AlphaStart", (2.0,), 0)
vsp.SetIntAnalysisInput(analysis_name, "AlphaNpts", (1,), 0)
vsp.SetDoubleAnalysisInput(analysis_name, "MachStart", (0.0,), 0)
vsp.SetIntAnalysisInput(analysis_name, "MachNpts", (1,), 0)
vsp.Update()
# # vsp.PrintAnalysisInputs(analysis_name)
vsp.ExecAnalysis(analysis_name)
# vsp.PrintResults(resp)

history_res = vsp.FindLatestResultsID("VSPAERO_History")
# load_res = vsp.FindLatestResultsID("VSPAERO_Load")
dtypes = {0: "INT_DATA", 1: "DOUBLE_DATA"}
res_dtypes = {}
data_names = vsp.GetAllDataNames(history_res)
for name in range(int(len(data_names))):
    dtype = vsp.GetResultsType(history_res, data_names[name])
    res_dtypes[data_names[name]] = dtypes[dtype]
    # print(str(name) + " | " + data_names[name] + " | " + str(dtype))

print(res_dtypes)
\
