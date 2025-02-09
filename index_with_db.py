import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor =conn.cursor()

cursor.execute(''' 
   CREATE TABLE IF NOT EXISTS VIDEOS(
               id INTERGER PRIMARY KEY,
               name  TEXT NOT NULL,
               time TEXT NOT NULL        
   )
''')

def list_videos():
  cursor.execute("SELECT * FROM VIDEOS")
  for row in cursor.fetchall():
    print(row)

def add_video(name , time):
  cursor.execute("INSERT INTO VIDEOS VALUES(? , ?)" , (name , time))
  conn.commit()

def update_video(video_id , new_name , new_time):
  cursor.execute("UPDATE VIDEOS SET name=? , time=? WHERE id=?" , (new_name , new_time , video_id))
  conn.commit()

def delete_video(video_id):
  cursor.execute("DELETE FROM VIDEOS WHERE id=?" , (video_id,))

def main():
  while True:
    print("YOUTUBE MANAGER with db")
    print("1. LIST ALL YOUTUBE VIDEOS")
    print("2. ADD A YOUTUBE VIDEO")
    print("3. UPDATE A YOUTUBE VIDEO DETAILS")
    print("4. DELETE A YOUTUBE VIDEO")
    print("5. EXIT THE APP")
    choice=input("enter your choice")

    if choice =='1':
      list_videos()
    elif choice=='2':
      name= input("Enter the video name")
      time= input("enter the video time")
      add_video(name , time)
    elif choice=='3':
      video_id = input("Enter video id to update")
      name= input("Enter the video name")
      time= input("enter the video time")
      update_video(video_id , name , time)
    elif choice=='4':
      video_id= input("Enter the video id you want to delete")
      delete_video(video_id)
    elif choice=='5':
      break
    else:
      print("Invalid input")
  
  conn.close()


main()