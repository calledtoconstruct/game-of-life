import pytest

from life import evolve
from life import is_alive

@pytest.mark.test_id(1)
def test_given_a_live_cell_with_no_neighbors_when_evolving_cell_dies():
    universe = [False, False, False, False, True, False, False, False, False]
    universe = evolve(universe, 3, 3)
    assert False == is_alive(universe, 3, 1, 1)

@pytest.mark.test_id(2)
def test_given_a_live_cell_with_one_neighbor_when_evolving_cell_dies():
    universe = [False, True, False, False, True, False, False, False, False]
    universe = evolve(universe, 3, 3)
    assert False == is_alive(universe, 3, 1, 1)

@pytest.mark.test_id(3)
def test_given_a_live_cell_with_four_neighbors_when_evolving_cell_dies():
    universe = [True, True, False, False, True, False, False, True, True]
    universe = evolve(universe, 3, 3)
    assert False == is_alive(universe, 3, 1, 1)

@pytest.mark.test_id(4)
def test_given_a_live_cell_with_three_neighbors_when_evolving_cell_continues_to_live():
    universe = [True, False, False, False, True, False, False, True, True]
    universe = evolve(universe, 3, 3)
    assert True == is_alive(universe, 3, 1, 1)

@pytest.mark.test_id(5)
def test_given_a_live_cell_with_two_neighbors_when_evolving_cell_continues_to_live():
    universe = [False, False, False, False, True, False, False, True, True]
    universe = evolve(universe, 3, 3)
    assert True == is_alive(universe, 3, 1, 1)

@pytest.mark.test_id(6)
def test_given_a_dead_cell_with_three_neighbors_when_evolving_cell_becomes_alive():
    universe = [True, False, False, False, False, False, False, True, True]
    universe = evolve(universe, 3, 3)
    assert True == is_alive(universe, 3, 1, 1)

@pytest.mark.test_id(7)
def test_given_a_dead_cell_with_two_neighbors_when_evolving_cell_dies():
    universe = [False, False, False, False, False, False, False, True, True]
    universe = evolve(universe, 3, 3)
    assert False == is_alive(universe, 3, 1, 1)

@pytest.mark.test_id(8)
def test_given_a_live_cell_in_the_upper_left_corner_with_two_neighbors_when_evolving_cell_continues_to_live():
    universe = [True, False, False, True, True, False, False, False, False]
    universe = evolve(universe, 3, 3)
    assert True == is_alive(universe, 3, 0, 0)

@pytest.mark.test_id(8)
def test_given_a_live_cell_in_the_lower_right_corner_with_two_neighbors_when_evolving_cell_continues_to_live():
    universe = [False, False, False, False, True, True, False, False, True]
    universe = evolve(universe, 3, 3)
    assert True == is_alive(universe, 3, 2, 2)
