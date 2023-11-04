from mongoengine import Document, StringField, BooleanField, connect

url = "mongodb+srv://dbUser:dbUserPassword@cluster0.9fi0utw.mongodb.net/?retryWrites=true&w=majority"
connect(host=url)

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField(required=True)
    preferred_contact_method = StringField(required=True, choices=('email', 'sms'))
    is_contacted = BooleanField(default=False)
