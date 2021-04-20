import deeplabcut
import os

dir_path = os.getcwd()
print(dir_path)
'''
demo_video_path = dir_path+'test1.mp4'

deeplabcut.create_new_project('test1','riv2r',[demo_video_path],working_directory=dir_path,copy_videos=True)

config_path = dir_path+'test1-riv2r-2021-04-20\\config.yaml'

video_path = dir_path+'test1-riv2r-2021-04-20\\videos\\test1.mp4'

deeplabcut.extract_frames(config_path,mode="automatic",algo="kmeans")

deeplabcut.label_frames(config_path)

deeplabcut.check_labels(config_path)

deeplabcut.create_training_dataset(config_path)

deeplabcut.train_network(config_path)

deeplabcut.evaluate_network(config_path,plotting=True)

deeplabcut.analyze_videos(config_path,[dir_path+'test1-riv2r-2021-04-20\\videos\\'],videotype='.mp4',save_as_csv=True)

deeplabcut.create_labeled_video(config_path, [video_path],videotype=".mp4")

deeplabcut.plot_trajectories(config_path,[video_path], showfigures=True)
'''