import json

def load_data():
  try:
    # open youtube.txt file , which i can read only , here r means read only
    with open('youtube.txt' , 'r') as file:
      # json will load the data in file and convert it into json
      return json.load(file)
  except FileNotFoundError:
    return []

# helper method to save videos data in file
def save_data_helper(videos):
  with open('youtube.txt' , 'w') as file:
    json.dump(videos , file)

def list_all_videos(videos):
  # enumerate add indexing in any iterable data and convert it into a tuple , ()
  for index , video in enumerate(videos , start=1):
    print(index)

def add_video(videos):
  name= input("enter video name")
  time = input("enter video time")
  videos.append({"name":name , "time":time})
  save_data_helper(videos)

def update_video(videos):
  list_all_videos(videos)
  index= input("Enter the video number to update")
  if 1 <= index <= len(videos):
    name=input("Enter the new video name")
    time = input("Enter the new video time")
    videos[index-1]= {"name": name , "time":time}
    save_data_helper(videos)
  else:
    print("Invalid index selected")


def delete_video(videos):
  list_all_videos(videos)
  index = input("Enter the bideo number to be deleted")
  if 1<= index <= len(videos):
    del videos[index-1]
    save_data_helper(videos)
  else:
    print("Invalid index")


def main():
  videos=load_data()
  while True:
    print("YOUTUBE MANAGER")
    print("1. LIST ALL YOUTUBE VIDEOS")
    print("2. ADD A YOUTUBE VIDEO")
    print("3. UPDATE A YOUTUBE VIDEO DETAILS")
    print("4. DELETE A YOUTUBE VIDEO")
    print("5. EXIT THE APP")
    choice=input("enter your choice")
    print("videos" , videos)

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
main()