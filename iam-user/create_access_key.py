import boto3

iam_client = boto3.client("iam")

# function to create access key for user
def create_access_key(user_name):
    try:
        response = iam_client.create_access_key(
            UserName = user_name
        )
        key = response["AccessKey"]
        print("UserName:        ", key["UserName"])
        print("AccessKeyID:     ", key["AccessKeyId"])
        print("Status:          ", key["Status"]) 
        print("SecretAccessKey: ", key["SecretAccessKey"])
        print("CreateDate:      ", key["CreateDate"])
    except Exception as e:
        print(e)
if __name__ == "__main__":
    username = input("Enter username: ")
    create_access_key(username)