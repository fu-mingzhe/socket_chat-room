import subprocess
import os



directory = (os.path.split(os.path.realpath(__file__))[0]).split("\\")
directory = "/".join(directory)+"/"
def get_image(video_path, image_path):
    img_count = 1
    crop_time = 0.0
    while crop_time <=55:
        cmd_str = f'ffmpeg -i {video_path} -f image2 -ss {crop_time} -vframes 1 {image_path}/{img_count}.png'
        subprocess.run(cmd_str,encoding='utf-8',shell=True)
        img_count += 1
        print(f'Geting Image {img_count}.png from time {crop_time: .5g}')
        crop_time += 1
    print("视频转化完成")

if __name__ == "__main__":
    get_image(directory+"1.mp4",directory)