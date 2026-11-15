# DB Dataset

A compact and efficient gizmo for Foundry Nuke designed to automate frame extraction for a CopyCat training. It eliminates the need for tedious manual setups involving multiple FrameHold and AppendClip nodes, allowing you to choose frames in a single click.

<p align="center"><img width="2000" height="852" alt="db_dataset_preview" src="https://github.com/user-attachments/assets/6f327aee-e088-4ee7-9813-3859675a73f4" /></p>

---

## Core Features

* **One-Click Selection:** Add or remove frames for your dataset on the fly while scrubbing the timeline.
* **Automated Assembly:** Selected frames are instantly compiled into a new sequence.
* **Keyframe Management:** Easily modify your frame pool using intuitive control buttons.
* **Preserve Original Image:** Option to preserve the original image in a separate layer via a single checkbox.

---

## Installation

1. Download the latest version from the **[Releases page](https://github.com/baramov/DB_Dataset/releases)**.
2. Copy `DB_Dataset.gizmo` file into `.nuke` directory or any custom plugin path defined in `init.py`.
3. Add the command to `menu.py` file:

```python
import nuke

toolbar = nuke.toolbar('Nodes')
dbtoolset = toolbar.addMenu('DB Toolset')
dbtoolset.addCommand("DB_Dataset", "nuke.createNode('DB_Dataset')")
```

---

## Controls

The gizmo provides a clean and minimal control panel:

* **Add** — Sets a keyframe on the current frame, adding it to the dataset.
* **Remove** — Deletes the keyframe on the current frame, removing it from the dataset.
* **Reset** — Completely clears all keyframes and wipes the dataset.
* **Preserve Source RGBA** — Preserve the source image into a separate layer.
* **Frame Counter** — Displays the total number of selected frames right next to the name.

---

## Compatibility
- Supported Versions: **Nuke 13.0 or later**.
- OS Compatibility: Windows, Linux, macOS.
