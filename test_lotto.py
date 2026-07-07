from lotto import generate_ticket

def test_generate_ticket_length_and_range():
    t = generate_ticket()
    assert len(t) == 6
    assert len(set(t)) == 6
    assert all(1 <= x <= 45 for x in t)
