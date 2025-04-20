def test_ufl():
    import ufl
    r = ufl.FiniteElement("R", cell=ufl.triangle)
    assert r.sobolev_space() is ufl.L2
