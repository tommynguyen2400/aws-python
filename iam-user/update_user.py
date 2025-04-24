import boto3

iam_client = boto3.client("iam")


# function to check new user name if exist
def check_user_exist(new_user_name):
    try:
        iam_client.get_user(UserName=new_user_name)
        return True
    except Exception as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            return False
        else:
            raise e

# fucntion to update username of user
def update_user(user_name, new_user_name):
    try:
        response = iam_client.update_user(
            UserName=user_name,
            NewUserName=new_user_name
        )
        return response
    except Exception as e:
        print(e)



if __name__ == "__main__":
    try:
        username = input("Enter old username to update: ")
        newUserName = input("Enter new username to update: ")
        if check_user_exist(newUserName):
            print(f"New user name {newUserName} has exist. Please choose username another.")
        else:
            update_user(username, newUserName)
            print("Updated successfully!")
    except KeyboardInterrupt:
        print("Canceled by user")