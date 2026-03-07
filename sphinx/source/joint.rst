.. _joint:

Joint
==============

Add Joint
--------------

Add Joint Between Two Rigid Bodies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Switch to *Object Mode*.  
2. Select the two rigid bodies to which you want to add a constraint.
3. Click the :menuselection:`+` button.
4. Configure the joint properties, then press :menuselection:`OK` to comfirm.

.. image:: images/addon_add_joint.gif
   :align: center

|

.. note::
   * You can find detailed explanations of all joint parameters in :ref:`Joint Properties <joint_properties>`.
   * ``Use Bone Rotation``: 
     
     When enabled, the joint's orientation will be aligned with the orientation of the associated bone.

     Disabling this option keeps the default joint orientation instead of matching the bone.

   * ``Is Lateral Joint``: 
     
     Indicates that the joint connects two rigid bodies belonging to different bone chains (for example, neighboring skirt chains).
     
     When this option is enabled, the add-on places the joint at the midpoint between the two rigid bodies and computes an averaged
     orientation to produce a stable constraint.

   * While it is technically possible to create multiple joints between the same pair of rigid bodies, do so with caution.  
     
     If you accidentally create duplicates when only one joint is needed, the simulation may behave unexpectedly.  
     
     You can verify duplicates in the :ref:`Joint List <joint_list>` and `Outliner`

     .. image:: images/addon_redundant_joints.png
        :align: center

Add Joints Along a Bone Chain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Switch to *Object Mode*
2. Select all rigid bodies along the same bone chain that require constraints.  
3. Click the :menuselection:`+` button.  
4. Configure the joint properties, then press :menuselection:`OK` to comfirm.

.. image:: images/addon_add_joints.gif
   :align: center

|

.. warning::
    When both bone-chain rigid bodies (e.g. A, B, C) and unrelated rigid bodies (e.g. D, E) are selected,
    the add-on will only create joints between the bone-chain rigid bodies (A, B, C).  
    The others (D, E) will be ignored.

.. note::
   Rigid bodies from different bone chains must be connected one pair at a time —  
   batch operations are **Not** supported in this case.  
     
   For example, when adding joints between rigid bodies belonging to different skirt bone chains, you must add them individually.  
     
   This limitation exists because each model has unique structures and assumptions, we prioritize flexibility and compatibility over full automation.  

   

Save Presets
^^^^^^^^^^^^^^
See also: :ref:`Rigid Body Save Presets <save_presets>`

.. _joint_properties:

Joint Properties
----------------------

- **name**: The name of the joint.  

- **limit_lin_x_upper**: Upper limit of linear motion along the **X** axis.  
- **limit_lin_y_upper**: Upper limit of linear motion along the **Y** axis.  
- **limit_lin_z_upper**: Upper limit of linear motion along the **Z** axis.  
- **limit_lin_x_lower**: Lower limit of linear motion along the **X** axis.  
- **limit_lin_y_lower**: Lower limit of linear motion along the **Y** axis.  
- **limit_lin_z_lower**: Lower limit of linear motion along the **Z** axis.  

- **limit_ang_x_upper**: Upper angular limit around the **X** axis (*in degrees*).  
- **limit_ang_y_upper**: Upper angular limit around the **Y** axis (*in degrees*).  
- **limit_ang_z_upper**: Upper angular limit around the **Z** axis (*in degrees*).  
- **limit_ang_x_lower**: Lower angular limit around the **X** axis (*in degrees*).  
- **limit_ang_y_lower**: Lower angular limit around the **Y** axis (*in degrees*).  
- **limit_ang_z_lower**: Lower angular limit around the **Z** axis (*in degrees*).  

- **spring_linear**: The spring stiffness that controls linear motion (Higher values produce stronger resistance when the joint is displaced).  
- **spring_angular**: The spring stiffness that controls angular motion (Higher values produce stronger torque resistance when the joint is rotated).

.. note::
   The parameters above correspond to Blender's built-in *Rigid Body Constraint* properties.  

.. _joint_properties_panel:

Joint Properties Panel
----------------------------

The *Joint Properties Panel* is where you can view and edit all joint-related attributes.  

It can be found under the *Physics Tab* in Blender.  

.. image:: images/addon_joint_properties_panel.gif
   :align: center

|

.. _joint_list:

Joint List
----------------

The *Joint List* displays all joints (*Rigid Body Constraint*) in the current scene.  

By default, it filters by :menuselection:`Active Model`, displaying only the joints of the currently selected model.  

To view joints from all models, change the filter to :menuselection:`All Models`.

.. image:: images/addon_joint_list.gif
   :align: center

|

Reordering List Items
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can reorder list items using the :menuselection:`⬆` and :menuselection:`⬇` buttons, 
or through the right-side dropdown menu options: :menuselection:`Move To Top` and :menuselection:`Move To Bottom`.

.. image:: images/addon_joint_move.gif
   :align: center

|

Error Icon Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Missing Joint
~~~~~~~~~~~~~~~~
A *"Missing Joint Error"* icon appears when the list entry has no valid *Rigid Body Constraint* data.  

This usually occurs when the joint was deleted from Blender's constraint system but still exists in the add-on's list.  

To fix this, recreate the joint using the :menuselection:`Add Rigid Body Constraint` button in the :ref:`Joint Properties Panel <joint_properties_panel>`.

.. image:: images/addon_joint_missing_joint.gif
   :align: center

|

Missing Linked Objects
~~~~~~~~~~~~~~~~~~~~~~~
A *"Missing Linked Objects Error"* icon appears when one or both of the rigid bodies linked by the joint are missing. 

For example, if ``Object1`` or ``Object2`` is not assigned, the joint cannot function properly.  

You can reassign the missing objects in the :ref:`Joint Properties Panel <joint_properties_panel>`.

.. image:: images/addon_joint_missing_object.gif
   :align: center

|

.. tip::
   It is generally recommended to assign the **static** or **bone-driven** rigid body as ``Object1``, and the **simulated** rigid body as ``Object2``.  
   
   This setup ensures a more stable and predictable constraint behavior, because Blender internally treats ``Object1`` as the reference frame for the joint's position and rotation limits.

Invalid Joint Pair
~~~~~~~~~~~~~~~~~~~~
An *"Invalid Joint Pair Error"* icon appears when both linked objects (``Object1`` and ``Object2``) refer to the same rigid body object.  

This setup is invalid because a joint requires two distinct rigid bodies.

Recreate the joint with two different rigid bodies to resolve this issue.

.. image:: images/addon_joint_invalid_pair.gif
   :align: center

|

Remove Joint
-------------------

1. Select a joint in the *3D viewport*, the *Joint List*, or the *Outliner*
2. Click the :menuselection:`-` button to remove it.

See also: :ref:`Remove Rigid Body <remove_rigid_body>`.
