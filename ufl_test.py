def test_ufl():  # noqa D100
    import ufl
    r = ufl.FiniteElement("R", cell=ufl.triangle)
    assert r.sobolev_space() is ufl.L2
