import json

def load_users():
    """Load users from users.json"""
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("users.json file not found.")
        return []
    except json.JSONDecodeError:
        print("users.json is not valid JSON.")
        return []

def filter_users(name=None, age=None, email=None):
    """
    Filter users by name, age, and/or email.
    All filters are optional.
    """
    users = load_users()
    if not users:
        return

    filtered_users = users

    if name:
        filtered_users = [
            user for user in filtered_users
            if user.get("name", "").lower() == name.lower()
        ]

    if age is not None:
        filtered_users = [
            user for user in filtered_users
            if user.get("age") == age
        ]

    if email:
        filtered_users = [
            user for user in filtered_users
            if user.get("email", "").lower() == email.lower()
        ]

    if not filtered_users:
        print("No users found with the given criteria.")
        return

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    # Ask user for filter criteria
    name_input = input("Enter name to filter by (or leave blank): ").strip()
    age_input = input("Enter age to filter by (or leave blank): ").strip()
    email_input = input("Enter email to filter by (or leave blank): ").strip()

    name_filter = name_input if name_input else None
    age_filter = None
    if age_input:
        try:
            age_filter = int(age_input)
        except ValueError:
            print("Invalid age entered. Ignoring age filter.")
    email_filter = email_input if email_input else None

    filter_users(name=name_filter, age=age_filter, email=email_filter)
