try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

sim = GetActiveSource()
bubble = Threshold()

bubble.Scalars = ['POINTS', 'heaviside']
bubble.ThresholdRange = [0.1, 1.0]
RenameSource("bubble")

RenderView1 = GetRenderView()

a1_pressure_PVLookupTable = GetLookupTableForArray( "pressure", 1 )
DataRepresentation25 = GetDisplayProperties(sim)
a1_pressure_PVLookupTable = GetLookupTableForArray( "pressure", 1 )

DataRepresentation27 = Show()
DataRepresentation27.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation27.ScalarOpacityFunction = []
DataRepresentation27.ColorArrayName = 'pressure'
DataRepresentation27.ScalarOpacityUnitDistance = 0.08332388424304965
DataRepresentation27.LookupTable = a1_pressure_PVLookupTable

DataRepresentation25.Visibility = 0

Render()

