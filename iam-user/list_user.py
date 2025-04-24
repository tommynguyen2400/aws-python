import boto3

# Create IAM client
iam_client = boto3.client('iam')

# function to list user
def list_user():
    try:
        response = iam_client.list_users()
        for user in response["Users"]:
            print("Username: ", user["UserName"])
            print("UserId: ", user["UserId"])
            print("Arn: ", user["Arn"])
            print("CreateDate: ", user["CreateDate"])
            print("=======================================")
    except Exception as e:
        print(e)


if __name__  == "__main__":
    try:
        list_user()
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("Stop!")