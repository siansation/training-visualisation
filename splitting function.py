import os
import logging
def split_video_annotation_into_frames_gt(prediction_file):
    folder_path = os.path.dirname(prediction_file)
    prediction_folder = os.path.join(folder_path, 'labels')
    try:
        if not os.path.exists(prediction_folder):
            os.makedirs(prediction_folder)
    except OSError:
        logging.error('Error creating directory')
    with open(prediction_file, 'r') as pred_f:
        for lines in pred_f:
            annotation = lines.split()
            if len(annotation) ==1: 
                frame_number = annotation[0]
                Frame_annotation_file = os.path.join(prediction_folder, 'frame' + frame_number + '.txt')
                with open(Frame_annotation_file, 'a+') as frame_f:
                    pass
                frame_f.close()
            else:
                frame_number = annotation[0]
                xmin = float(annotation[1])
                ymin = float(annotation[2])
                xmax = float(annotation[3])
                ymax = float(annotation[4])
                #confidence_level = float(annotation[5])
                info = ['drone', 0.00, 0, 0.0, "{:.2f}".format(xmin), "{:.2f}".format(ymin), "{:.2f}".format(xmax), "{:.2f}".format(ymax), 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                string = ' '.join([str(elem) for elem in info])
                Frame_annotation_file = os.path.join(prediction_folder, 'frame' + frame_number + '.txt')
                with open(Frame_annotation_file, 'a+') as frame_f:
                    frame_f.write(string + '\n')
                frame_f.close()
    pred_f.close()
    print('done')
    
split_video_annotation_into_frames_gt("C:\Users\User\Downloads\livestream-0.95-10groundtruth\livestream-0.95-10groundtruth.txt")