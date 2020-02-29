def status_counter(statuses, status):
    # counter = 0
    # for k, v, in statuses.items():
    #     if status in v:
    #         counter += 1
    # return counter
    return list(statuses.values()).count(status)


def test_status_counter():
    statuses = {
        "Alice": "online",
        "Bob": "offline",
        "Eve": "online"
    }
    assert status_counter(statuses, "xxx") == 0
    assert status_counter(statuses, "online") == 2
    assert status_counter(statuses, "offline") == 1
