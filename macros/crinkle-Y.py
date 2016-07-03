#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
sim = GetActiveSource()

# delete key visibility of source file
simDisplay = GetDisplayProperties(sim, view=renderView1)
simDisplay.SetScalarBarVisibility(renderView1, False)

# create a new 'Slice'
slice1 = Slice(Input=sim)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
slice1Display = Show(slice1, renderView1)

# hide data in view
Hide(sim, renderView1)

# Properties modified on slice1.SliceType - Y
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1
slice1.Crinkleslice = 1

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'elemId'))

# remove 'show plane'
Hide3DWidgets(proxy=slice1.SliceType)

