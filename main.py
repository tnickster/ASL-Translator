def setup_paths():

    #setups paths
    WORKSPACE_PATH = './RealTimeObjectDetection/Tensorflow/workspace' #. calls the current dir
    SCRIPTS_PATH = './RealTimeObjectDetection/Tensorflow/scripts'   #generate tf records location
    APIMODEL_PATH = './RealTimeObjectDetection/Tensorflow/models'   #obj detection model
    ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'                 #label map and tensor flow records
    IMAGE_PATH = WORKSPACE_PATH+'/images'                           #images location
    MODEL_PATH = WORKSPACE_PATH+'/models'                           #trained model location
    PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'    #transfer learn
    CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'       #gives us the details of the models we are using
    CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

    #create label maps
    labels = [
        {'name':'Hello', 'id':1},                                   #xml files
        {'name':'Yes', 'id':2},
        {'name':'No', 'id':3},
        {'name':'Thank you', 'id':4},
        {'name':'I love you', 'id':5},
    ]

    with open(ANNOTATION_PATH + '/label_map.txt', 'w') as f: #put the labels in a txt file under annotations
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')

setup_paths()