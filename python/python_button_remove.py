import nuke

# Check if animation and keyframe exist
dataset_knob = nuke.thisNode()['dataset']
if dataset_knob.isAnimated(0):
    if dataset_knob.isKey(0):

        # Remove keyframe from dataset knob on current frame
        dataset_knob.removeKey(0)

        # Extract and sort frame numbers from dataset knob keyframes
        dataset_curve = dataset_knob.animations()[0]
        keyframes = sorted([key.x for key in dataset_curve.keys()])

        # Count total keyframes
        numberframes = len(keyframes)

        # Check if any keyframes remain
        if numberframes > 0:
            
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
        
        else:
            
            # Reset dataset knob
            node = nuke.thisNode()
            node['dataset'].clearAnimated()
            node['dataset'].setExpression('frame')
            node['label'].setValue('')

            # Reset sequence
            nuke.toNode('append_set')['firstFrame'].clearAnimated()
            nuke.toNode('append_set')['firstFrame'].setExpression('frame')

            # Reset sequence range
            root_last = int(nuke.Root()['last_frame'].value())
            nuke.toNode('set_range')['last_frame'].clearAnimated()
            nuke.toNode('set_range')['last_frame'].setValue(root_last)

            # Clear dataset total frames label
            nuke.thisNode()['autolabel'].setValue("nuke.thisNode().name()")