import nuke

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