try: paraview.simple
except: from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

sim = GetActiveSource()
PlotOverLine3 = PlotOverLine( Source="High Resolution Line Source" )

PlotOverLine3.Source.Point2 = [3.0, 3.0, 0.0]

RenderView1 = GetRenderView()
AnimationScene1 = GetAnimationScene()
XYChartView3 = CreateXYPlotView()
XYChartView3.ViewTime = 0.0

DataRepresentation34 = Show()
DataRepresentation34.XArrayName = 'arc_length'
DataRepresentation34.SeriesVisibility = ['ALE_velocity (0)', '0', 
                                         'ALE_velocity (1)', '0', 
										 'ALE_velocity (2)', '0', 'mesh_velocity (0)', '0', 'mesh_velocity (1)', '0', 'mesh_velocity (2)', '0', 'SL_velocity (0)', '0', 'SL_velocity (1)', '0', 'SL_velocity (2)', '0', 'gravity (0)', '0', 'gravity (1)', '0', 'gravity (2)', '0', 'velocity (0)', '0', 'velocity (1)', '0', 'velocity (2)', '0', 'vtkValidPointMask', '0', 'arc_length', '0', 'Points (0)', '0', 'Points (1)', '0', 'Points (2)', '0', 'Points (Magnitude)', '0', 'vtkOriginalIndices', '0']
DataRepresentation34.UseIndexForXAxis = 0

PlotOverLine3.Source.Point1 = [1.5, 0.0, 0.0]
PlotOverLine3.Source.Point2 = [1.5, 3.0, 0.0]

RenderView1.CameraClippingRange = [8.005829753817663, 8.455499064513596]

AnimationScene1.ViewModules = [ RenderView1, XYChartView3 ]

RenderView1.CameraClippingRange = [8.114190898479565, 8.319094709047231]

DataRepresentation34.SeriesColor = ['heaviside', '0', '0', '0', 'ALE_velocity (0)', '0.894118', '0.101961', '0.109804', 'ALE_velocity (1)', '0.215686', '0.494118', '0.721569', 'ALE_velocity (2)', '0.301961', '0.686275', '0.290196', 'ALE_velocity (Magnitude)', '0.596078', '0.305882', '0.639216', 'viscosity', '1', '0.498039', '0', 'density', '0.65098', '0.337255', '0.156863', 'vertID', '0.47451', '0.0901961', '0.0901961', 'kappa', '0.709804', '0.00392157', '0.00392157', 'distance', '0.937255', '0.278431', '0.0980392', 'edgeSize', '0.976471', '0.513725', '0.141176', 'heatFlux', '1', '0.705882', '0', 'mesh_velocity (0)', '1', '0.898039', '0.0235294', 'mesh_velocity (1)', '0.458824', '0.694118', '0.00392157', 'mesh_velocity (2)', '0.345098', '0.501961', '0.160784', 'mesh_velocity (Magnitude)', '0.313725', '0.843137', '0.74902', 'SL_velocity (0)', '0.109804', '0.584314', '0.803922', 'SL_velocity (1)', '0.231373', '0.407843', '0.670588', 'SL_velocity (2)', '0.603922', '0.407843', '1', 'SL_velocity (Magnitude)', '0.372549', '0.2', '0.501961', 'gravity (0)', '0.231373', '0.407843', '0.670588', 'gravity (1)', '0.109804', '0.584314', '0.803922', 'gravity (2)', '0.305882', '0.85098', '0.917647', 'gravity (Magnitude)', '0.45098', '0.603922', '0.835294', 'pressure', '0.258824', '0.239216', '0.662745', 'concentration', '0.313725', '0.329412', '0.529412', 'velocity (0)', '0.0627451', '0.164706', '0.321569', 'velocity (1)', '0.109804', '0.584314', '0.803922', 'velocity (2)', '0.231373', '0.407843', '0.670588', 'velocity (Magnitude)', '0.4', '0.243137', '0.717647', 'elemId', '0.635294', '0.329412', '0.811765', 'vtkValidPointMask', '0.870588', '0.380392', '0.807843', 'arc_length', '0.862745', '0.380392', '0.584314', 'Points (0)', '0.239216', '0.0627451', '0.321569', 'Points (1)', '0.396078', '0.486275', '0.215686', 'Points (2)', '0.458824', '0.694118', '0.00392157', 'Points (Magnitude)', '0.698039', '0.729412', '0.188235', 'vtkOriginalIndices', '1', '0.898039', '0.0235294']
DataRepresentation34.SeriesVisibility = ['ALE_velocity (0)', '0', 'ALE_velocity (1)', '0', 'ALE_velocity (2)', '0', 'mesh_velocity (0)', '0', 'mesh_velocity (1)', '0', 'mesh_velocity (2)', '0', 'SL_velocity (0)', '0', 'SL_velocity (1)', '0', 'SL_velocity (2)', '0', 'gravity (0)', '0', 'gravity (1)', '0', 'gravity (2)', '0', 'velocity (0)', '0', 'velocity (1)', '0', 'velocity (2)', '0', 'vtkValidPointMask', '0', 'arc_length', '0', 'Points (0)', '0', 'Points (1)', '0', 'Points (2)', '0', 'Points (Magnitude)', '0', 'vtkOriginalIndices', '0', 'heaviside', '0', 'ALE_velocity (Magnitude)', '0', 'viscosity', '0', 'density', '0', 'vertID', '0', 'kappa', '0', 'distance', '0', 'edgeSize', '0', 'heatFlux', '0', 'mesh_velocity (Magnitude)', '0', 'SL_velocity (Magnitude)', '0', 'gravity (Magnitude)', '0', 'pressure', '1', 'concentration', '0', 'velocity (Magnitude)', '0', 'elemId', '0']

Render()
