import btrack
from skimage.io import imread
from btrack import datasets
from btrack.io import export_CSV
# load your segmentation data
segmentation = imread('/Users/lian/Desktop/Tracking/BTrack/segmented.tif')

# create btrack objects (with properties) from the segmentation data
# (you can also calculate properties, based on scikit-image regionprops)
objects = btrack.utils.segmentation_to_objects(
  segmentation, properties=('area', )
)
CONFIG_FILE = datasets.cell_config()
# initialise a tracker session using a context manager
with btrack.BayesianTracker() as tracker:

  # configure the tracker using a config file
  tracker.configure(CONFIG_FILE)

  # append the objects to be tracked
  tracker.append(objects)

  # set the volume (Z axis volume limits default to [-1e5, 1e5] for 2D data)
  tracker.volume = ((0, 1200), (0, 1600))

  # track them (in interactive mode)
  tracker.track_interactive(step_size=100)

  # generate hypotheses and run the global optimizer
  tracker.optimize()

#   # store the data in an HDF5 file
#   tracker.export('/path/to/tracks.h5', obj_type='obj_type_1')

  # get the tracks as a python list
  tracks = tracker.tracks

  # optional: get the data in a format for napari
  data, properties, graph = tracker.to_napari()

export_CSV("/Users/lian/Desktop/Tracking/BTrack/output.csv",tracks)
# get the first track
track_zero = tracks[0]

# print the length of the track
print(len(track_zero))

# print all of the xyzt positions in the track
print(track_zero.x)
print(track_zero.y)
print(track_zero.z)
print(track_zero.t)

# print the fate of the track
print(track_zero.fate)

# print the track ID, root node, parent node, children and generational depth
print(track_zero.ID)
print(track_zero.root)
print(track_zero.parent)
print(track_zero.children)
print(track_zero.generation)