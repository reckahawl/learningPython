import pytube

# function to download audio or video
def download_media(url, media_type):
    yt = pytube.YouTube(url)

    # download audio
    if media_type == "audio":
        audio_streams = yt.streams.filter(only_audio=True)
        audio_streams.first().download()
        print("Audio downloaded successfully!")

    # download video
    elif media_type == "video":
        video_streams = yt.streams.filter(only_video=True)
        video_streams.first().download()
        print("Video downloaded successfully!")

    # invalid media type
    else:
        print("Invalid media type. Please choose 'audio' or 'video'.")


# example usage
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
media_type = "audio"  # change to "video" to download video instead
download_media(url, media_type)
