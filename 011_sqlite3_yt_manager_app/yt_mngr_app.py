import sqlite3

conn = sqlite3.connect("youtube_videos_details.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    # this cursor objects holds the returned output of the sql query execution given above
    # we got a tuple and need to loop for video values
    for row in cursor.fetchall():
        print(row)
    

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    # now commiting the executed query
    conn.commit()
    
def update_video(videoID, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name, new_time, videoID))
    conn.commit()
    

def delete_video(videoID):
    cursor.execute("DELETE FROM videos where id = ?",(videoID,))
    # accepts only tuple values to make is tupple videoID has trailing comma
    conn.commit()

    

def main():
    while True:
        print("Youtube Manager app with SqlLite3 DB")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                add_video(name,time)
            case '3':
                videoID = input("Enter the video id that you want to update: ")
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                update_video(videoID, name, time)
            case '4':
                videoID = input("Enter the video id that you want to delete: ")
                delete_video(videoID)
            case '5':
                break
            case _: #_ This is for other default value
                print("Invalid Choice")

    # after all the work done db connection closed, less chance of db corruption
    conn.close()

if __name__ == "__main__":
    main()