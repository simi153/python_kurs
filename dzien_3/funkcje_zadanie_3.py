def online_count(statuses, statuss):
    # count = 0
    # for user, status in statuses.items():
    #     if status.lower() == statuss.lower():
    #         count += 1
    # return count
    return list(statuses.values()).count(statuss)


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def test_online_count_with_existing_status():
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online",
    }
    assert online_count(statuses, "online") == 2
    assert online_count(statuses, "offline") == 1


def test_online_count_with_empty_dict():
    statuses = {}
    assert online_count({}, "online") == 0
    assert online_count({}, "offline") == 0


def test_online_count_without_existing_status():
    statuses = {
        "Alice": "",
        "Bob": "",
        "Eve": "",
    }
    assert online_count({}, "online") == 0
    assert online_count({}, "offline") == 0
