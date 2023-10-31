from random import randint

class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            { 
                "id": 2,
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            { 
                "id": 3,
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": 1
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Generate a new ID for the member
        member_id = self._generateId()
        member["id"] = member_id
        self._members.append(member)
        return member_id


    def delete_member(self, id):
        members = self._members
        # Find member to delete
        for index, item in enumerate(members):
            if item["id"] == id:
                member_to_delete = index
        
        self._members.pop(member_to_delete)

        # fill this method and update the return
        return self._members


    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    
        

    def get_all_members(self):
        return self._members