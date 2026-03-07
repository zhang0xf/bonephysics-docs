.. Bone Physics Docs documentation master file, created by
   sphinx-quickstart on Fri Sep 19 16:51:38 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the Bone Physics documentation!
===========================================

**Bone Physics** is a Blender add-on designed for skeletal-based physics simulation in stylized character animation.
It is particularly useful for dynamic elements such as hair, ribbons, tails, and other secondary motion parts.

This add-on is developed on top of |blender_mmd_tools|.
Its purpose is to port the MMD physics system into Blender as a standalone module,  
while providing full compatibility with Blender's built-in **Rigify** armature and other common rigging systems.

This add-on is open-source on |github| and distributed under the GPL-3.0 license.

If you would like to support its development, you may also purchase it on |superhivemarket|, |gumroad|, and |bilibili_shop|.

Since the system is based on |blender_mmd_tools|,  
you can reference the physics setups found in many existing **MMD models** when configuring your own characters.

Video tutorials and complete workflow demonstrations are available on |youtube_link| and |bilibili_link|.

.. |github| raw:: html
         
   <a href="https://github.com/zhang0xf/bonephysics" target="_blank">github</a>

.. |superhivemarket| raw:: html
         
   <a href="https://superhivemarket.com" target="_blank">superhivemarket</a>

.. |gumroad| raw:: html

   <a href="https://gumroad.com" target="_blank">gumroad</a>

.. |bilibili_shop| raw:: html

   <a href="https://shop.bilibili.com" target="_blank">bilibili_shop</a>

.. |blender_mmd_tools| raw:: html
         
   <a href="https://github.com/MMD-Blender/blender_mmd_tools" target="_blank">blender_mmd_tools</a>

.. |youtube_link| raw:: html

   <a href="https://www.youtube.com" target="_blank">YouTube</a>

.. |bilibili_link| raw:: html

   <a href="https://www.bilibili.com" target="_blank">Bilibili</a>

.. toctree::
   :maxdepth: 2

   installation
   setup
   rigidbody
   joint
   scene
   link
   QA