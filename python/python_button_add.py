import nuke

# Add current frame to dataset knob as a keyframe
dataset_knob = nuke.thisNode()['dataset']
dataset_knob.setAnimated()
dataset_knob.setValue(nuke.frame())

# Extract and sort frame numbers from dataset knob keyframes
dataset_curve = dataset_knob.animations()[0]
keyframes = sorted([key.x for key in dataset_curve.keys()])

# Count total keyframes
numberframes = len(keyframes)

# Define dataset sequence first and last frames
first = int(nuke.Root()['first_frame'].value())
last = first + numberframes

# Set dataset sequence last frame
dataset_range = nuke.toNode('set_range')['last_frame']
dataset_range.setExpression('')
dataset_range.clearAnimated()
dataset_range.setValue(last - 1)

# Prepare dataset sequence
append_knob = nuke.toNode('append_set')['firstFrame']
append_knob.setExpression('')
append_knob.clearAnimated()
append_knob.setAnimated()

# Set dataset sequence
for i, src_frame in enumerate(keyframes):
    target_frame = first + i
    append_knob.setValueAt(src_frame, target_frame)

# Update dataset total frames label
autolabel_string = f"nuke.thisNode().name() + ' ({numberframes})'"
nuke.thisNode()['autolabel'].setValue(autolabel_string)