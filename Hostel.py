

class Visitor:
    def __init__(self, fname, lname, visitor_id):
        self.fname = fname
        self.lname = lname
        self.visitor_id = visitor_id

    def fullname(self):
        return f"{self.fname} {self.lname}"

    def __str__(self):
        return f"Visitor(Name: {self.fullname()}, ID: {self.visitor_id})"


class Resident:
    def __init__(self, name, room):
        self.name = name
        self.room = room

    def __str__(self):
        return f"Resident(Name: {self.name}, Room: {self.room})"


class Hostel:
    def __init__(self, name):
        self.name = name
        self.visits = []

    def record_visit(self, visitor, resident):
        visit_info = {
            "first_name": visitor.fname,
            "last_name": visitor.lname,
            "visitor_id": visitor.visitor_id,
            "resident": resident.name,
            "room": resident.room
        }
        self.visits.append(visit_info)
        print(f"✅ Visit recorded: {visitor.fname} {visitor.lname} visited {resident.name} in room {resident.room}")

    def show_visits(self):
        print(f"\n Visit Records for {self.name}:")
        if not self.visits:
            print("No visits recorded yet.")
        else:
            for i, visit in enumerate(self.visits, 1):
                print(f"{i}. {visit['first_name']} {visit['last_name']} "
                      f"(ID: {visit['visitor_id']}) visited {visit['resident']} (Room: {visit['room']})")

    def find_visits_by_visitor(self, visitor_name):
        print(f"\n Searching visits by {visitor_name}:")
        found = False
        for visit in self.visits:
            full_name = f"{visit['first_name']} {visit['last_name']}"
            if visitor_name.lower() in full_name.lower():
                print(f"- {visit['first_name']} {visit['last_name']} visited {visit['resident']} in Room {visit['room']}")
                found = True
        if not found:
            print("No visits found for this visitor.")

    def find_visits_by_room(self, room_number):
        print(f"\n Searching visits to Room {room_number}:")
        found = False
        for visit in self.visits:
            if visit['room'].lower() == room_number.lower():
                print(f"- {visit['first_name']} {visit['last_name']} visited {visit['resident']}")
                found = True
        if not found:
            print("Room doesnt exist.")
        



visitor1 = Visitor("Mwiza", "Dorothy", "V123")
visitor2 = Visitor("Tuwmwine", "Timothy", "V456")
visitor3 = Visitor("Natuhamya", "Liz", "V789")
visitor4 = Visitor("Mutoni", "Denise", "V101")
visitor5 = Visitor("Deogracious", "Ocen", "V202")
visitor6 = Visitor("Okello", "Jonathan", "V303")

resident1 = Resident("Bob", "12B")
resident2 = Resident("Aliker", "10A")
resident3 = Resident("Aijuka", "14C")
resident4 = Resident("Angela", "11D")
resident5 = Resident("Erinah", "13E")
resident6 = Resident("Bataringaya", "15F")

hostel = Hostel("Sky Courts")

hostel.record_visit(visitor1, resident1)
hostel.record_visit(visitor2, resident2)
hostel.record_visit(visitor1, resident2)
hostel.record_visit(visitor1, resident3)
hostel.record_visit(visitor3, resident1)
hostel.record_visit(visitor2, resident6)
hostel.record_visit(visitor3, resident5)
hostel.record_visit(visitor4, resident2)
hostel.record_visit(visitor5, resident1)
hostel.record_visit(visitor6, resident4)
hostel.record_visit(visitor4, resident3)
hostel.record_visit(visitor1, resident5)

hostel.show_visits()

search_name = input("\nEnter visitor name to search: ")
hostel.find_visits_by_visitor(search_name)

search_room = input("\nEnter room number to search visits: ")
hostel.find_visits_by_room(search_room)

print("\n Thank you for Visiting Our Sky Court Hostel")
