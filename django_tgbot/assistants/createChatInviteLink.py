


class CreateChatInviteLink():
    fields = {
        'invite_link': str,
        'is_primary': bool,
        'is_revoked': bool,
        'creates_join_request'  : bool , 
        'creator' : {
            'id' : str ,
            'is_bot' : bool , 
            'first_name' : str ,
            'username' : str ,
        }
    }

    def __init__(self, obj=None):
        self.fields = obj

    def invite_link(self):
        return self.fields[self.invite_link.__name__]
        
    def is_primary(self):
        return bool(self.fields[self.is_primary.__name__])

    def is_revoked(self):
        return bool(self.fields[self.is_revoked.__name__])

    def creates_join_request(self):
        return bool(self.fields[self.creates_join_request.__name__])

    def creator(self) -> dict :
        return self.fields[self.creator.__name__]
    
    def creator_id(self):
        return str(self.fields["creator"]["id"])
    
    def creator_is_bot(self):
        return str(self.fields["creator"]["is_bot"])
    
    def creator_first_name(self):
        return str(self.fields["creator"]["first_name"])

    def creator_username(self):
        return str(self.fields["creator"]["username"])



