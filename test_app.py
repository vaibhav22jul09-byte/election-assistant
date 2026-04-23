from helper import check_eligibility

def test_valid():
    assert check_eligibility("18", "yes") == "You are eligible to vote in India."

def test_invalid():
    assert check_eligibility("abc", "yes") == "Invalid age input"

def test_underage():
    assert check_eligibility("16", "yes") == "You are not eligible to vote."

test_valid()
test_invalid()
test_underage()

print("All tests passed")
