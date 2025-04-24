import boto3

# Create IAM client
iam_client = boto3.client('iam')



# function to check user if exist
def check_user_exist(user_name):
    try:
        iam_client.get_user(UserName=user_name)
        return True
    except Exception as e:
        if e.response['Error']['Code'] == 'NoSuchEntity':
            return False
        else:
            raise e



# function to creat new user
def create_user(user_name):
    try:
        response = iam_client.create_user(
            UserName=user_name,
        )
        return response
    except Exception as e:
        print(e)


if __name__  == "__main__":
    try:
        username = input("Enter username: ")
        if check_user_exist(username):
            print(f"User {username} has exist")
        else:
            if create_user(username):
                print(f"Create user {username} successfully")
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Stop!")
        