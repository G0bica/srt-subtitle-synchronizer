# SRT subtitle synchronizer

Usage : python srtsync.py subtitlename.srt delay newsubtitlename.srt

delay - where to move a subtitle in seconds. <br> if you want to make subtitles appear sooner, use the minus prefix (as shown in the examples)

**IMPORTANT!! If you do not provide the last (new subtitle file name) argument, <br> the program will simply change your source .srt file (subtitlename.srt)**

## Examples

**python srtsync.py subtitles.srt 15**

This makes the subtitles appear 15 seconds later!

**python srtsync.py subtitles.srt -7**

This makes the subtitles appear 7 seconds earlier.



