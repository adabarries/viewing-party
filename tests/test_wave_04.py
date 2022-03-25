import pytest
from viewing_party.party import *
from tests.test_constants import *

# Test 1
# @pytest.mark.skip()
def test_get_available_friend_rec():
    # Arrange
    amandas_data = clean_wave_4_data()

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) == 2
    assert HORROR_1b in recommendations
    assert FANTASY_4b in recommendations
    assert amandas_data == clean_wave_4_data()

# Test 2
# @pytest.mark.skip()
def test_no_available_friend_recs():
    # Arrange
    amandas_data = {
        "subscriptions": ["hulu", "disney+"],
        "watched": [],
        "friends": [
            {
                "watched": [HORROR_1b]
            },
            {
                "watched": [FANTASY_3b]
            }
        ]
    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) == 0
