from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://python_mongo:<add here passowrd>@pythonmongo.mbpgpgu.mongodb.net/")
db = client["pythonMongo"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({
        "name": name,
        "time": time
    })

def update_video(videoID, new_name, new_time):
    try:
        if ObjectId.is_valid(videoID):
            result = video_collection.update_one(
                {'_id': ObjectId(videoID)},
                {'$set': {
                    "name": new_name,
                    "time": new_time
                }}
            )
            if result.matched_count:
                print(f"Video with ID {videoID} updated successfully.")
            else:
                print(f"No video found with ID {videoID}.")
        else:
            print("Invalid video ID format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_video(videoID):
    try:
        if ObjectId.is_valid(videoID):
            result = video_collection.delete_one({
                "_id": ObjectId(videoID)
            })
            if result.deleted_count:
                print(f"Video with ID {videoID} deleted successfully.")
            else:
                print(f"No video found with ID {videoID}.")
        else:
            print("Invalid video ID format.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("Youtube Manager app with MongoDB")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                add_video(name, time)
            case '3':
                videoID = input("Enter the video ID that you want to update: ")
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                update_video(videoID, name, time)
            case '4':
                videoID = input("Enter the video ID that you want to delete: ")
                delete_video(videoID)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()
