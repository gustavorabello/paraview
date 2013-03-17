try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

airwater_0000000_vtk = GetActiveSource()
Contour6 = Contour( PointMergeMethod="Uniform Binning" )

Contour6.PointMergeMethod = "Uniform Binning"
Contour6.ContourBy = ['POINTS', 'P']
Contour6.Isosurfaces = [0.0]

Contour6.ContourBy = ['POINTS', 'PHI']

RenderView1 = GetRenderView()
DataRepresentation8 = GetDisplayProperties(airwater_0000000_vtk)
DataRepresentation12 = Show()
DataRepresentation12.ScaleFactor = 9.999999747378752e-06
DataRepresentation12.SelectionPointFieldDataArrayName = 'P'
DataRepresentation12.EdgeColor = [0.0, 0.0, 0.5000076295109483]

a1_P_PVLookupTable = GetLookupTableForArray( "P", 1 )

DataRepresentation12.ColorArrayName = 'P'
DataRepresentation12.LookupTable = a1_P_PVLookupTable

Render()
