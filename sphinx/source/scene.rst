.. _scene:

Scene Setup
==============

This panel provides a centralized place to configure **timeline**, **rigid body world**,  
and **baking** settings required for a stable physics simulation workflow.

It is especially useful when working with linked files, library overrides,  
or complex rigs that rely on multiple rigid bodies and constraints.

.. image:: images/addon_scene_panel.png
    :alt: Scene Setup panel
    :align: center
    :width: 50%

Timeline
-------------

The **Timeline** section displays and edits basic animation frame settings:

* **Current Frame**  
  Shows the current frame of the scene timeline.

* **Start / End**  
  Defines the playback range used for previewing and baking physics simulations.

These values are shared with Blender's global timeline and directly affect  
rigid body simulation and cache baking.

Rigid Body World
-----------------------

Blender's rigid body system relies on a scene-level container called the  
**Rigid Body World**, which manages:

* Global simulation settings (solver iterations, substeps, gravity)
* Collections that store all rigid bodies
* Collections that store all rigid body constraints

Bone Physics automatically manages these settings to ensure consistency.

.. _update-rigid-world:

Update Rigid World
^^^^^^^^^^^^^^^^^^

Click **Update Rigid World** to synchronize the scene with the rigid body system.

.. image:: images/addon_update_rigid_world.gif
        :align: center

|

This operation will:

* Ensure a valid **Rigid Body World** exists in the scene
* Create and assign required collections if missing
* Add all Bone Physics rigid bodies to the world collection
* Add all rigid body constraints to the constraint collection
* Fix broken references caused by:
  
  * Linked files
  * Library Overrides
  * Collection Instances

This step is **required** after:

* Linking a rig from another file
* Creating or updating library overrides
* Duplicating or instancing rigs
* Encountering missing or invalid physics behavior

.. note::
   If the button displays an error icon, it indicates that the rigid body world
   settings differ from the recommended defaults and should be updated.

Simulation Quality Settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following parameters control simulation accuracy and stability:

* **Substeps**  
  Number of physics substeps per frame.  
  Higher values improve stability for fast or lightweight objects.

* **Iterations**  
  Solver iteration count per substep.  
  Higher values result in more accurate constraint solving at the cost of performance.

The add-on sets conservative default values that balance stability and performance  
for character-based physics.

Bake
----

Rigid body simulations can be cached (baked) for stable playback and rendering.

* **Bake**  
  Bakes the rigid body simulation into the point cache for the current frame range.

* **Delete Bake**  
  Clears the baked cache and restores the simulation to real-time evaluation.

When a bake exists:

* Timeline playback no longer recalculates physics
* Simulation results are deterministic
* Performance during animation playback improves

.. note::
   Baking is recommended before final animation polish or rendering.
   If you need to adjust rigid bodies or constraints, delete the bake first.

Workflow Notes
--------------

* Always run **Update Rigid World** after structural changes to the rig.
* Bake only after confirming the simulation behaves as expected.
* When working in a multi-file pipeline, update the rigid body world
  after linking or overriding assets to avoid broken constraints.
