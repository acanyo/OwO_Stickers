# 删除指定文件夹下所有文件名中的 下划线 _ 以及之前的字符串，如: "file_name.txt" -> "name.txt"

import os
import re

def remove_emoji_from_filenames(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        # Define the new filename by removing everything before and including the first underscore
        new_filename = re.sub(r'^.*?_', '', filename)

        # Get the full paths for renaming
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: "{filename}" to "{new_filename}"')



# Example usage
folder_path = r'D:\Development\Project\CSharp\LottieViewConvert\LottieViewConvert\bin\Debug\net8.0\SavedStickers\RestrictedEmoji\RestrictedEmoji_output'
remove_emoji_from_filenames(folder_path)