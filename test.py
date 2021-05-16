import deeplabcut
import os

class proj:

    def __init__(self,father_path,project_name,video_name):
        self.path = father_path+'\\'+project_name
        self.config_path = self.path+'\\'+'config.yaml'
        self.video_path = self.path+'\\'+'videos'+'\\'+video_name

father_path = os.getcwd()

video_name = 'test.mp4'

origin_video_path = father_path+'\\'+'originvideo'+'\\'+video_name

# deeplabcut.create_new_project('test','riv2r',[origin_video_path],working_directory=father_path,copy_videos=True)

# 编辑config.yaml文件，可以编辑识别点的个数等

project_name = 'test-riv2r-2021-05-16'

Proj = proj(father_path,project_name,video_name)

# deeplabcut.extract_frames(Proj.config_path,mode="automatic",algo="kmeans")

# deeplabcut.label_frames(Proj.config_path)

# deeplabcut.check_labels(Proj.config_path)

# deeplabcut.create_training_dataset(Proj.config_path)

# 编辑dlc-models\iteration-0\testApr20-trainset95shuffle1\train\pose_cfg.yaml，可编辑每几次循环终端显示一次训练信息(display_iters)，也可编辑记录训练快照(snapshot)的迭代次数(save_iters)

# deeplabcut.train_network(Proj.config_path)

# deeplabcut.evaluate_network(Proj.config_path,plotting=True)

# deeplabcut.analyze_videos(Proj.config_path,[Proj.video_path],videotype='.mp4',save_as_csv=True)

# 下行生成带有标记视频的语句要在终端运行
# deeplabcut.create_labeled_video(Proj.config_path, [Proj.video_path],videotype=".mp4")

# deeplabcut.plot_trajectories(Proj.config_path,[Proj.video_path], showfigures=True)