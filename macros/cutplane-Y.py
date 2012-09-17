try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

sim = GetActiveSource()
Threshold1 = Threshold()
RenameSource('cutplane-Y')

Threshold1.Scalars = ['CELLS', 'concentration']

Threshold1.Scalars = ['POINTS', 'cutPlaneY']
Threshold1.ThresholdRange = [1.23, 3.0]

# no Visibility to vtk file
RenderView1 = GetRenderView()
DataRepresentation1 = GetDisplayProperties(sim)
DataRepresentation1.Visibility = 0
a1_pressure_PVLookupTable = GetLookupTableForArray( "pressure", 1 )

# show cut plane 
DataRepresentation2 = Show()
DataRepresentation2.EdgeColor = [0.0, 0.0, 0.5000076295109483]
DataRepresentation2.ScalarOpacityFunction = []
DataRepresentation2.ColorArrayName = 'pressure'
DataRepresentation2.ScalarOpacityUnitDistance = 0.6817266399853545
DataRepresentation2.LookupTable = a1_pressure_PVLookupTable
DataRepresentation2.Representation = 'Surface With Edges'

Render()
