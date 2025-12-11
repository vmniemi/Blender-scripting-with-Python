import bpy
# "bpy" is Blender's Python module.
# It is used to so that Python can interact with Blender
# It's required for any Blender Python script.




bpy.ops.object.select_all(action='SELECT')
# This selects all objects in the scene Clear the scene (select everything and delete) ---
# existing objects so the script creates a predictable, clean scene.


bpy.ops.object.delete(use_global=False)
# This part removes all objects that are currently selected 
# These two work in object mode, if this is run in other modes it may not work properly 



for i in range(5):
    # Creates 5 spheres efficiently 
    # The loop index 'i' is used to space the spheres along the X axis and to name them.

    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(i * 2, 0, 0))
    # - radius=0.5 sets the sphere's radius.
    # - location=(i * 2, 0, 0) positions the sphere at X = i * 2, Y = 0, Z = 0.
    #   Using i * 2 spaces the spheres 2 Blender units apart along the X axis.
    

    sphere = bpy.context.active_object
    # the sphere we just created (operators set the newly made object as active by default).
    # Why assigned: storing a reference to the newly created object allows the script to
    # modify its properties (like the name, transforms, materials) directly.

    sphere.name = f"Sphere_{i}"
    # This renames the newly created object as determined by the for like such as "Sphere_0", "Sphere_1", etc.
    # Naming things are useful for managing them later
