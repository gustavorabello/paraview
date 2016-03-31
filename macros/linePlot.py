#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
sim10vtk = FindSource('sim-10.vtk')

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(Input=sim10vtk,
    Source='High Resolution Line Source')

# init the 'High Resolution Line Source' selected for 'Source'
plotOverLine1.Source.Point1 = [-1.5, 0.0, 0.0]
plotOverLine1.Source.Point2 = [1.5, 1.5, 0.0]

# Properties modified on plotOverLine1
plotOverLine1.Tolerance = 2.22044604925031e-16

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [862, 628]

# get layout
viewLayout1 = GetLayout()

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [426, 628]

# place view in the layout
viewLayout1.AssignView(2, lineChartView1)

# show data in view
plotOverLine1Display = Show(plotOverLine1, lineChartView1)
# trace defaults for the display properties.
plotOverLine1Display.CompositeDataSetIndex = [0]
plotOverLine1Display.UseIndexForXAxis = 0
plotOverLine1Display.XArrayName = 'arc_length'
plotOverLine1Display.SeriesVisibility = ['ALE_velocity_Magnitude', 'concentration', 'density', 'distance', 'edgeSize', 'elemId', 'gravity_Magnitude', 'heatFlux', 'heaviside', 'kappa', 'mesh_velocity_Magnitude', 'pressure', 'SL_velocity_Magnitude', 'velocity_Magnitude', 'vertID', 'viscosity']
plotOverLine1Display.SeriesLabel = ['ALE_velocity_X', 'ALE_velocity_X', 'ALE_velocity_Y', 'ALE_velocity_Y', 'ALE_velocity_Z', 'ALE_velocity_Z', 'ALE_velocity_Magnitude', 'ALE_velocity_Magnitude', 'arc_length', 'arc_length', 'concentration', 'concentration', 'density', 'density', 'distance', 'distance', 'edgeSize', 'edgeSize', 'elemId', 'elemId', 'gravity_X', 'gravity_X', 'gravity_Y', 'gravity_Y', 'gravity_Z', 'gravity_Z', 'gravity_Magnitude', 'gravity_Magnitude', 'heatFlux', 'heatFlux', 'heaviside', 'heaviside', 'kappa', 'kappa', 'mesh_velocity_X', 'mesh_velocity_X', 'mesh_velocity_Y', 'mesh_velocity_Y', 'mesh_velocity_Z', 'mesh_velocity_Z', 'mesh_velocity_Magnitude', 'mesh_velocity_Magnitude', 'pressure', 'pressure', 'SL_velocity_X', 'SL_velocity_X', 'SL_velocity_Y', 'SL_velocity_Y', 'SL_velocity_Z', 'SL_velocity_Z', 'SL_velocity_Magnitude', 'SL_velocity_Magnitude', 'velocity_X', 'velocity_X', 'velocity_Y', 'velocity_Y', 'velocity_Z', 'velocity_Z', 'velocity_Magnitude', 'velocity_Magnitude', 'vertID', 'vertID', 'viscosity', 'viscosity', 'vtkValidPointMask', 'vtkValidPointMask', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
plotOverLine1Display.SeriesColor = ['ALE_velocity_X', '0', '0', '0', 'ALE_velocity_Y', '0.89', '0.1', '0.11', 'ALE_velocity_Z', '0.22', '0.49', '0.72', 'ALE_velocity_Magnitude', '0.3', '0.69', '0.29', 'arc_length', '0.6', '0.31', '0.64', 'concentration', '1', '0.5', '0', 'density', '0.65', '0.34', '0.16', 'distance', '0', '0', '0', 'edgeSize', '0.89', '0.1', '0.11', 'elemId', '0.22', '0.49', '0.72', 'gravity_X', '0.3', '0.69', '0.29', 'gravity_Y', '0.6', '0.31', '0.64', 'gravity_Z', '1', '0.5', '0', 'gravity_Magnitude', '0.65', '0.34', '0.16', 'heatFlux', '0', '0', '0', 'heaviside', '0.89', '0.1', '0.11', 'kappa', '0.22', '0.49', '0.72', 'mesh_velocity_X', '0.3', '0.69', '0.29', 'mesh_velocity_Y', '0.6', '0.31', '0.64', 'mesh_velocity_Z', '1', '0.5', '0', 'mesh_velocity_Magnitude', '0.65', '0.34', '0.16', 'pressure', '0', '0', '0', 'SL_velocity_X', '0.89', '0.1', '0.11', 'SL_velocity_Y', '0.22', '0.49', '0.72', 'SL_velocity_Z', '0.3', '0.69', '0.29', 'SL_velocity_Magnitude', '0.6', '0.31', '0.64', 'velocity_X', '1', '0.5', '0', 'velocity_Y', '0.65', '0.34', '0.16', 'velocity_Z', '0', '0', '0', 'velocity_Magnitude', '0.89', '0.1', '0.11', 'vertID', '0.22', '0.49', '0.72', 'viscosity', '0.3', '0.69', '0.29', 'vtkValidPointMask', '0.6', '0.31', '0.64', 'Points_X', '1', '0.5', '0', 'Points_Y', '0.65', '0.34', '0.16', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.89', '0.1', '0.11']
plotOverLine1Display.SeriesPlotCorner = ['ALE_velocity_X', '0', 'ALE_velocity_Y', '0', 'ALE_velocity_Z', '0', 'ALE_velocity_Magnitude', '0', 'arc_length', '0', 'concentration', '0', 'density', '0', 'distance', '0', 'edgeSize', '0', 'elemId', '0', 'gravity_X', '0', 'gravity_Y', '0', 'gravity_Z', '0', 'gravity_Magnitude', '0', 'heatFlux', '0', 'heaviside', '0', 'kappa', '0', 'mesh_velocity_X', '0', 'mesh_velocity_Y', '0', 'mesh_velocity_Z', '0', 'mesh_velocity_Magnitude', '0', 'pressure', '0', 'SL_velocity_X', '0', 'SL_velocity_Y', '0', 'SL_velocity_Z', '0', 'SL_velocity_Magnitude', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'velocity_Magnitude', '0', 'vertID', '0', 'viscosity', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']
plotOverLine1Display.SeriesLineStyle = ['ALE_velocity_X', '1', 'ALE_velocity_Y', '1', 'ALE_velocity_Z', '1', 'ALE_velocity_Magnitude', '1', 'arc_length', '1', 'concentration', '1', 'density', '1', 'distance', '1', 'edgeSize', '1', 'elemId', '1', 'gravity_X', '1', 'gravity_Y', '1', 'gravity_Z', '1', 'gravity_Magnitude', '1', 'heatFlux', '1', 'heaviside', '1', 'kappa', '1', 'mesh_velocity_X', '1', 'mesh_velocity_Y', '1', 'mesh_velocity_Z', '1', 'mesh_velocity_Magnitude', '1', 'pressure', '1', 'SL_velocity_X', '1', 'SL_velocity_Y', '1', 'SL_velocity_Z', '1', 'SL_velocity_Magnitude', '1', 'velocity_X', '1', 'velocity_Y', '1', 'velocity_Z', '1', 'velocity_Magnitude', '1', 'vertID', '1', 'viscosity', '1', 'vtkValidPointMask', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Points_Magnitude', '1']
plotOverLine1Display.SeriesLineThickness = ['ALE_velocity_X', '2', 'ALE_velocity_Y', '2', 'ALE_velocity_Z', '2', 'ALE_velocity_Magnitude', '2', 'arc_length', '2', 'concentration', '2', 'density', '2', 'distance', '2', 'edgeSize', '2', 'elemId', '2', 'gravity_X', '2', 'gravity_Y', '2', 'gravity_Z', '2', 'gravity_Magnitude', '2', 'heatFlux', '2', 'heaviside', '2', 'kappa', '2', 'mesh_velocity_X', '2', 'mesh_velocity_Y', '2', 'mesh_velocity_Z', '2', 'mesh_velocity_Magnitude', '2', 'pressure', '2', 'SL_velocity_X', '2', 'SL_velocity_Y', '2', 'SL_velocity_Z', '2', 'SL_velocity_Magnitude', '2', 'velocity_X', '2', 'velocity_Y', '2', 'velocity_Z', '2', 'velocity_Magnitude', '2', 'vertID', '2', 'viscosity', '2', 'vtkValidPointMask', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Points_Magnitude', '2']
plotOverLine1Display.SeriesMarkerStyle = ['ALE_velocity_X', '0', 'ALE_velocity_Y', '0', 'ALE_velocity_Z', '0', 'ALE_velocity_Magnitude', '0', 'arc_length', '0', 'concentration', '0', 'density', '0', 'distance', '0', 'edgeSize', '0', 'elemId', '0', 'gravity_X', '0', 'gravity_Y', '0', 'gravity_Z', '0', 'gravity_Magnitude', '0', 'heatFlux', '0', 'heaviside', '0', 'kappa', '0', 'mesh_velocity_X', '0', 'mesh_velocity_Y', '0', 'mesh_velocity_Z', '0', 'mesh_velocity_Magnitude', '0', 'pressure', '0', 'SL_velocity_X', '0', 'SL_velocity_Y', '0', 'SL_velocity_Z', '0', 'SL_velocity_Magnitude', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'velocity_Magnitude', '0', 'vertID', '0', 'viscosity', '0', 'vtkValidPointMask', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Points_Magnitude', '0']

# set active view
SetActiveView(renderView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=plotOverLine1)

# Properties modified on plotOverLine1.Source
plotOverLine1.Source.Point1 = [0.0, 0.0, 0.0]
plotOverLine1.Source.Point2 = [0.0, 1.5, 0.0]

# set active view
SetActiveView(lineChartView1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=plotOverLine1)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=plotOverLine1)

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = []
plotOverLine1Display.SeriesColor = ['ALE_velocity_X', '0', '0', '0', 'ALE_velocity_Y', '0.889998', '0.100008', '0.110002', 'ALE_velocity_Z', '0.220005', '0.489998', '0.719997', 'ALE_velocity_Magnitude', '0.300008', '0.689998', '0.289998', 'arc_length', '0.6', '0.310002', '0.639994', 'concentration', '1', '0.500008', '0', 'density', '0.650004', '0.340002', '0.160006', 'distance', '0', '0', '0', 'edgeSize', '0.889998', '0.100008', '0.110002', 'elemId', '0.220005', '0.489998', '0.719997', 'gravity_X', '0.300008', '0.689998', '0.289998', 'gravity_Y', '0.6', '0.310002', '0.639994', 'gravity_Z', '1', '0.500008', '0', 'gravity_Magnitude', '0.650004', '0.340002', '0.160006', 'heatFlux', '0', '0', '0', 'heaviside', '0.889998', '0.100008', '0.110002', 'kappa', '0.220005', '0.489998', '0.719997', 'mesh_velocity_X', '0.300008', '0.689998', '0.289998', 'mesh_velocity_Y', '0.6', '0.310002', '0.639994', 'mesh_velocity_Z', '1', '0.500008', '0', 'mesh_velocity_Magnitude', '0.650004', '0.340002', '0.160006', 'pressure', '0', '0', '0', 'SL_velocity_X', '0.889998', '0.100008', '0.110002', 'SL_velocity_Y', '0.220005', '0.489998', '0.719997', 'SL_velocity_Z', '0.300008', '0.689998', '0.289998', 'SL_velocity_Magnitude', '0.6', '0.310002', '0.639994', 'velocity_X', '1', '0.500008', '0', 'velocity_Y', '0.650004', '0.340002', '0.160006', 'velocity_Z', '0', '0', '0', 'velocity_Magnitude', '0.889998', '0.100008', '0.110002', 'vertID', '0.220005', '0.489998', '0.719997', 'viscosity', '0.300008', '0.689998', '0.289998', 'vtkValidPointMask', '0.6', '0.310002', '0.639994', 'Points_X', '1', '0.500008', '0', 'Points_Y', '0.650004', '0.340002', '0.160006', 'Points_Z', '0', '0', '0', 'Points_Magnitude', '0.889998', '0.100008', '0.110002']
plotOverLine1Display.SeriesPlotCorner = ['ALE_velocity_Magnitude', '0', 'ALE_velocity_X', '0', 'ALE_velocity_Y', '0', 'ALE_velocity_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SL_velocity_Magnitude', '0', 'SL_velocity_X', '0', 'SL_velocity_Y', '0', 'SL_velocity_Z', '0', 'arc_length', '0', 'concentration', '0', 'density', '0', 'distance', '0', 'edgeSize', '0', 'elemId', '0', 'gravity_Magnitude', '0', 'gravity_X', '0', 'gravity_Y', '0', 'gravity_Z', '0', 'heatFlux', '0', 'heaviside', '0', 'kappa', '0', 'mesh_velocity_Magnitude', '0', 'mesh_velocity_X', '0', 'mesh_velocity_Y', '0', 'mesh_velocity_Z', '0', 'pressure', '0', 'velocity_Magnitude', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'vertID', '0', 'viscosity', '0', 'vtkValidPointMask', '0']
plotOverLine1Display.SeriesLineStyle = ['ALE_velocity_Magnitude', '1', 'ALE_velocity_X', '1', 'ALE_velocity_Y', '1', 'ALE_velocity_Z', '1', 'Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'SL_velocity_Magnitude', '1', 'SL_velocity_X', '1', 'SL_velocity_Y', '1', 'SL_velocity_Z', '1', 'arc_length', '1', 'concentration', '1', 'density', '1', 'distance', '1', 'edgeSize', '1', 'elemId', '1', 'gravity_Magnitude', '1', 'gravity_X', '1', 'gravity_Y', '1', 'gravity_Z', '1', 'heatFlux', '1', 'heaviside', '1', 'kappa', '1', 'mesh_velocity_Magnitude', '1', 'mesh_velocity_X', '1', 'mesh_velocity_Y', '1', 'mesh_velocity_Z', '1', 'pressure', '1', 'velocity_Magnitude', '1', 'velocity_X', '1', 'velocity_Y', '1', 'velocity_Z', '1', 'vertID', '1', 'viscosity', '1', 'vtkValidPointMask', '1']
plotOverLine1Display.SeriesLineThickness = ['ALE_velocity_Magnitude', '2', 'ALE_velocity_X', '2', 'ALE_velocity_Y', '2', 'ALE_velocity_Z', '2', 'Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'SL_velocity_Magnitude', '2', 'SL_velocity_X', '2', 'SL_velocity_Y', '2', 'SL_velocity_Z', '2', 'arc_length', '2', 'concentration', '2', 'density', '2', 'distance', '2', 'edgeSize', '2', 'elemId', '2', 'gravity_Magnitude', '2', 'gravity_X', '2', 'gravity_Y', '2', 'gravity_Z', '2', 'heatFlux', '2', 'heaviside', '2', 'kappa', '2', 'mesh_velocity_Magnitude', '2', 'mesh_velocity_X', '2', 'mesh_velocity_Y', '2', 'mesh_velocity_Z', '2', 'pressure', '2', 'velocity_Magnitude', '2', 'velocity_X', '2', 'velocity_Y', '2', 'velocity_Z', '2', 'vertID', '2', 'viscosity', '2', 'vtkValidPointMask', '2']
plotOverLine1Display.SeriesMarkerStyle = ['ALE_velocity_Magnitude', '0', 'ALE_velocity_X', '0', 'ALE_velocity_Y', '0', 'ALE_velocity_Z', '0', 'Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'SL_velocity_Magnitude', '0', 'SL_velocity_X', '0', 'SL_velocity_Y', '0', 'SL_velocity_Z', '0', 'arc_length', '0', 'concentration', '0', 'density', '0', 'distance', '0', 'edgeSize', '0', 'elemId', '0', 'gravity_Magnitude', '0', 'gravity_X', '0', 'gravity_Y', '0', 'gravity_Z', '0', 'heatFlux', '0', 'heaviside', '0', 'kappa', '0', 'mesh_velocity_Magnitude', '0', 'mesh_velocity_X', '0', 'mesh_velocity_Y', '0', 'mesh_velocity_Z', '0', 'pressure', '0', 'velocity_Magnitude', '0', 'velocity_X', '0', 'velocity_Y', '0', 'velocity_Z', '0', 'vertID', '0', 'viscosity', '0', 'vtkValidPointMask', '0']

# Properties modified on plotOverLine1Display
plotOverLine1Display.SeriesVisibility = ['pressure']

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.0, 0.75, 10000.0]
renderView1.CameraFocalPoint = [0.0, 0.75, 0.0]
renderView1.CameraParallelScale = 1.6770509831248424

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).