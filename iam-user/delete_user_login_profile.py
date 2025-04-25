import boto3

iam_client = boto3.client("iam")

# function to delete user login profile
def delete_login_profile(user_name):
    try:
        response = iam_client.delete_login_profile(
            UserName=user_name
        )
        return response
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        username = input("Enter username: ")
        if delete_login_profile(username):
            print(f"Deleted user login profile successfully!")
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Canceled")