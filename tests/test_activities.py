def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, dict)
    assert len(payload) == expected_count


def test_get_activities_contains_expected_activity_keys(client):
    # Arrange
    expected_activity_names = {
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball Team",
        "Soccer Club",
        "Drama Club",
        "Painting Workshop",
        "Debate Team",
        "Math Olympiad Club",
    }

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert expected_activity_names.issubset(payload.keys())


def test_get_activities_activity_shape_is_valid(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    for activity_data in payload.values():
        assert required_keys.issubset(activity_data.keys())
        assert isinstance(activity_data["participants"], list)
