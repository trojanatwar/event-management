import requests



url = "http://127.0.0.1:5000/"


def test_create_event():
    respo = requests.post(url + "events/create/" + "121/" + "qAC/" + "01031999/" + "40" )
    print("Event Added: ", respo.json())

def test_events():
    respo = requests.get(url + "events/"+ "7" )
    print("Events: ", respo.json())

def test_tickets_availabilty():
    respo = requests.get(url + "events/available/"+ "7" )
    print("Available tickets: ", respo.json())

def test_redeem_ticket():
    respo = requests.put(url + "events/redeem/"+ "6/" + "5" )
    print("Ticket Redeemed", respo.json())

def test_add_ticket():
    respo = requests.put(url + "events/add/"+ "5/" + "15" )
    print("Ticket added", respo.json())


if __name__ == "__main__":
    test_create_event()
    test_events()
    test_tickets_availabilty()
    test_add_ticket
    test_redeem_ticket()