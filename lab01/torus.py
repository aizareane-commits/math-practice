import gmsh

gmsh.initialize()
gmsh.model.add("hollow_torus")

R = 1
r1 = 0.4
r2 = 0.3
lc = 0.02

outer = gmsh.model.occ.addTorus(0, 0, 0, R, r1)
inner = gmsh.model.occ.addTorus(0, 0, 0, R, r2)

gmsh.model.occ.cut([(3, outer)], [(3, inner)])

gmsh.model.occ.synchronize()

gmsh.option.setNumber("Mesh.MeshSizeMin", lc)
gmsh.option.setNumber("Mesh.MeshSizeMax", lc)

gmsh.model.mesh.generate(3)

gmsh.write("torus.msh")
gmsh.fltk.run()

gmsh.finalize()