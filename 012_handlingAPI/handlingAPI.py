""" # handling API from freeAPI.api
import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/users/random"
    response = requests.get(url)
    # the response is string
    data = response.json()

    if data["success"] and "data" in data:
        userdata = data["data"]
        # login bhitra username
        username =  userdata["login"]["username"]
        country = userdata["location"]["country"]
        return username, country
    else:
        # raise raise error explicitly by prpgrammer
        raise Exception("Failed to Fetch User data")
    
def main():
    try:
        username, country = fetch_random_user_freeapi()
        print(f"the country is {country} and username is {username}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main() """


import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country = fectch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()