# Values and Stuff.

munch_enc = lambda video_br, audio_br: f'-c:v libx264 -b:v {video_br}k -preset slower -c:a aac -b:a {audio_br}k -x264-params partitions=p4x4,i4x4'

dur_cmd = lambda video: f'ffprobe -v error -of default=noprint_wrappers=1:nokey=1 -select_streams v:0 -show_entries format=duration "{video}"'

video_cmd = lambda video: f'ffprobe -v error -show_entries stream=width,height -of default=noprint_wrappers=1:nokey=1 "{video}"'
