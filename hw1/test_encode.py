from encode import encode

def test_empty_string():
     assert encode("") == ""

def test_expected_string():
     input = "aaabbbcccddd"
     assert encode(input) == "a3b3c3d3"
