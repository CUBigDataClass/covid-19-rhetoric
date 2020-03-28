import twitterScraper as ts

######################################################################################################################
# Tests for twitterScraper
######################################################################################################################	

def test_make_string_query_case_1():
    track_list = ["funny","joke","hilarious","meme"]
    loc_near = "Grand Junction,CO"
    loc_within_mi = 50

    expected = "funny OR joke OR hilarious OR meme near:\"Grand Junction,CO\" within:50mi"
    actual = ts.make_string_query(track_list,loc_near,loc_within_mi)

    assert expected == actual

def test_make_string_query_case_2():
    track_list = ["funny"]
    loc_near = "New York,NY"
    loc_within_mi = 200

    expected = "funny near:\"New York,NY\" within:200mi"
    actual = ts.make_string_query(track_list,loc_near,loc_within_mi)

    assert expected == actual
