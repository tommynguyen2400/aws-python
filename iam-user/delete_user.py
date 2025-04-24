import boto3

iam_client = boto3.client("iam")


# check user if exist
def check_user_exist(user_name):
    try:
        iam_client.get_user(UserName=user_name)
        return True
    except Exception as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            return False
        else:
            raise e


# function to delete user
def delete_user(user_name):
    try:
        response = iam_client.delete_user(
            UserName = user_name
        )
        return response
    except Exception as e:
        print(e)


if __name__ == "__main__":
    try:
        username = input("Enter username to delete: ")
        if check_user_exist(username):
            confirm = input(f"Are you to delete user {username} ? (y/n) ")
            if confirm == "y" or confirm == "Y":
                delete_user(username)
                print(f"Deleted {username} successfully.")
            else:
                print("Canceled to delete")
        else:
            print(f"User {username} has no exist. Please to create user.")
    except KeyboardInterrupt:
        print("Canceled by user")