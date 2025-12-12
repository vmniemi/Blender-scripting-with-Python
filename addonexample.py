bl_info = {
    "name": "My Sphere Generator",
    "author": "Veikka Niemi",
    "version": (1, 0),
    "blender": (4, 2, 16),
    "location": "3D View > Sidebar > Simple Tools",
    "description": "Creates five spheres in a row",
    "category": "Object",
}
# Creates a dictionary that contains information about the add-on
# Such as minimum blender required or description
# This section is not required but recommended if sharing or publishing it


import bpy
# "bpy" is Blender's Python module
# It is used to so that Python can interact with Blender
# It's required for any Blender Python script.


class OBJECT_OT_generate_spheres(bpy.types.Operator): #Defines a new operator type
    bl_idname = "object.generate_spheres"  # Internal name used to call the operator
    bl_label = "Generate 5 Spheres"  # Displayed name in menus and UI

    def execute(self, context): # Creates a method that runs when the user activates the operator
        # The actual code that you want the add-on to run
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        for i in range(5):
            bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(i * 2, 0, 0))
        return {'FINISHED'}  # Tells Blender that the code ran successfully


class VIEW3D_PT_sphere_panel(bpy.types.Panel): # Creates a new user interface panel
    bl_label = "My Sphere Generator" # Name displayed in the sidebar
    bl_idname = "VIEW3D_PT_sphere_panel" # creates a unique identifier for add-on
    bl_space_type = 'VIEW_3D' # Location of the  panel,  appears in the 3D Viewport
    bl_region_type = 'UI' #In the right-side sidebar (N-panel)
    bl_category = 'Simple Tools'  # Tab name of panel


    
    # Adds a clickable button
    def draw(self, context):
        layout = self.layout
        layout.operator(OBJECT_OT_generate_spheres.bl_idname, icon='MESH_UVSPHERE')

# This makes the registreration run through a loop instead of running the whole thing everytime
classes = (
    OBJECT_OT_generate_spheres,
    VIEW3D_PT_sphere_panel,
)


# Blender must register operators and panels to recognize them
# This you used when you enable the add-on
def register():
    for cls in classes:  # Loop through every class
        bpy.utils.register_class(cls) # register it with Blender

# Same thing as register, this you used when you disable or reload the add-on
def unregister():
    for cls in reversed(classes):   
        bpy.utils.unregister_class(cls)

# This lets you run the add-on as a regular script in Blender’s text editor without installing it
if __name__ == "__main__":
    register()
