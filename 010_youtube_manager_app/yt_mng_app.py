import json

def load_data():
    try:
        with open("youtube.txt","r") as file:
            # .load does goes to the file automaticaly and loads all the data in json format
            return json.load(file) 
            # this loaded data is of list type but ot json list, print(type(json.load(file)))
    except FileNotFoundError: # except is for exception which is like catch of try-catch block
        return []
    finally:
        pass

# this method is a helper method for saving all the videos
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        # dump is to write all data in json
        # writing videos in file i.e: youtube.txt
        json.dump(videos,file)


def list_all_videos(videos):
    # our videos loaded are of json data , and the video list is not index so fro indexing enumerate is used
    # enumerate adds indexing to any iterable object
    print("\n")
    print("x" *50)
    for index, video in enumerate(videos, start=1):
        print(f"Index: {index}, Video: {video['video_name']}, Duration: {video['time']}")
    # print("\n")
    print("x" *50)

def add_video(videos):
    video_name = input("Enter Video Name: ")
    time = input("Enter video time: ")
    videos.append({'video_name':video_name, 'time':time})
    save_data_helper(videos)

    # this is how our list looks like
    """ [
        {
            "video_name":"akjfn"
            "time":"faj"
        },
        {
            "video_name":"akjfn"
            "time":"faj"
        }
    ] """
    

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to Update"))
    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        # now appending the json list
        videos[index-1] = {'name':name, 'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def  delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number index to be deleted: "))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid Video index selected")
    

# main() entry point of any program
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _: #_ This is for other default value
                print("Invalid Choice")
# if function name equals to main() function in sthis code file run this code
if __name__ == "__main__":
    main()
# __ this double underscore is called dunder