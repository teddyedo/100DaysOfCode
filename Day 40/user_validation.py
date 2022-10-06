from user import User
import requests

ADD_USER_ENDPOINT = "https://api.sheety.co/*******************" \
                    "/flightDeals/users "


class UserValidation:

    def create_new_user(self):
        print("Welcome to the teddy's Flight Club!")
        first_name = input("What's your name? ")
        last_name = input("What's your last name? ")
        username = input("What's your username? ")
        email = input("What's your email? ")
        verification_email = input("Repeat your email: ")

        if email != verification_email:
            print("Emails don't match. Retry.")
        else:
            new_user = User(first_name=first_name,
                            last_name=last_name, username=username, email=email)
            self.save_new_user(new_user)

    def save_new_user(self, user: User):
        new_user = {
            "user": {
                "firstName": user.first_name,
                "lastName": user.last_name,
                "username": user.username,
                "email": user.email
            }}

        response = requests.post(ADD_USER_ENDPOINT, json=new_user)
        response.raise_for_status()
