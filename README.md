# DB Dataset

A compact and efficient Nuke tool (Gizmo) designed to automate frame extraction for a **CopyCat** training. It eliminates the need for tedious manual setups involving multiple FrameHold and AppendClip nodes, allowing you to choose and compile frames in a single click.

---

## Core Features

* **One-Click Selection:** Add or remove frames for your dataset on the fly while scrubbing the timeline.
* **Automated Assembly:** Selected frames are instantly compiled into a new sequence.
* **Keyframe Management:** Easily modify your frame pool using intuitive control buttons.
* **Preserve Original Image:** Option to preserve the original image in a separate layer via a single checkbox.

---

## Interface & Controls

The gizmo provides a clean and minimal control panel:

* **Add** — Sets a keyframe on the current frame, adding it to the dataset.
* **Remove** — Deletes the keyframe on the current frame, removing it from the dataset.
* **Reset** — Completely clears all keyframes and wipes the dataset.
* **Frame Counter** — Displays the total number of selected frames right next to the name.
* **"Save Original" Checkbox** — Preserve the source image into a separate layer.

---

## 📦 Installation

1. Copy the gizmo file into your `.nuke` directory or any custom plugin path defined in your `init.py`.
2. Add the command to `menu.py` file:

```python
import nuke

toolbar = nuke.toolbar('Nodes')
dbtoolset = toolbar.addMenu('DB Toolset')
dbtoolset.addCommand("DB_Dataset", "nuke.createNode('DB_Dataset')")
```

---

## Compatibility
- Supported Versions: **Nuke 13, 14, 15, and 16+**.
- OS Compatibility: Windows, Linux, macOS.
