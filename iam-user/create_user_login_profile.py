import boto3


# client
iam_client = boto3.client("iam")

# function to create user to login console
def create_user_login_profile(user_name, password):
    try:
        response = iam_client.create_login_profile(
            UserName = user_name,
            Password = password,
            PasswordResetRequired=True
        )
        return response
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if create_user_login_profile(username, password):
            print(f"Created user login profile successfully!")
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Canceled")