from pytube import YouTube
from sys import argv
import sys


def on_progress(vid, chunk, bytes_remaining):
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    total_size = (total_size / 1024) / 1024
    total_size = round(total_size, 1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion, 2)

    # print(f'Total Size: {totalsz} MB')
    print(
        f'Download Progress: {percentage_of_completion}%, Total Size:{total_size} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')


def progress_function(vid, chunk, bytes_remaining):
    filesize = vid.filesize
    current = ((filesize - bytes_remaining) / filesize)
    percent = '{0:.1f}'.format(current * 100)
    progress = int(50 * current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


link = argv[1]
yt = YouTube(link, on_progress_callback=progress_function)
# yt.register_on_progress_callback(progress_function)

print("Title: ", yt.title)
print("View: ", yt.views)


yd = yt.streams.get_highest_resolution()
print('Available Resolutions: ')
res_list = []
for stream in yt.streams.order_by('resolution'):
    if not res_list.__contains__(stream.resolution):
        res_list.append(stream.resolution)
print('\n'.join(res_list))
print('Downloading: ', yd.resolution)
total_size = (yd.filesize / 1024) / 1024
total_size = round(total_size, 1)
print('File Size', str(total_size) + 'MB')
# ADD FOLDER HERE
yd.download('./YTfolder')
print('\n')
print('Downloaded to ./YTfolder')
