#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
sim = GetActiveSource()

# create a new 'Slice'
slice1 = Slice(Input=sim)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
slice1Display = Show(slice1, renderView1)

# hide data in view
Hide(sim, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, False)

# Properties modified on slice1.SliceType
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# Properties modified on slice1
slice1.Triangulatetheslice = 0

# Properties modified on slice1
slice1.Crinkleslice = 1

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'elemId'))

# remove 'show plane'
Hide3DWidgets(proxy=slice1.SliceType)

