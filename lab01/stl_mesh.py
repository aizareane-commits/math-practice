import gmsh

gmsh.initialize()
gmsh.model.add("stl_model")

gmsh.merge("GeometryRemeshed.STL")

surfaces = gmsh.model.getEntities(2)
sl = [tag for dim, tag in surfaces]

loop = gmsh.model.geo.addSurfaceLoop(sl)
gmsh.model.geo.addVolume([loop])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

gmsh.write("stl_model.msh")
gmsh.fltk.run()

gmsh.finalize()