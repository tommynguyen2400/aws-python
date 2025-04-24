import boto3

iam_client = boto3.client("iam")


# function to delete access key
def delete_access_key(user_name, access_key):
    try:
        response = iam_client.delete_access_key(
            UserName=user_name,
            AccessKeyId=access_key
        )
        return response
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        username = input("Enter username: ")
        access_key = input("Enter access key ID: ")
        delete_access_key(username, access_key)
    except KeyboardInterrupt:
        print("Canceled")


