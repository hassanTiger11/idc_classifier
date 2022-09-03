import torch
import torch.nn as nn
import torchvision
import torch
from torchvision import transforms
from PIL import Image

def load_model(model = './idc_classifier_cuda.pth') -> int:
    '''
    This  function loads the model from a .pth file
    I trained this model using google colab
    I found the data set that this model was trained on in:
        https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images
    
    '''
    NUM_CLASSES = 2
    idc_clasifier = torchvision.models.resnet18()
    num_features = idc_clasifier.fc.in_features
    print(num_features)

    idc_clasifier.fc = nn.Sequential(
        nn.Linear(num_features, 512),
        nn.ReLU(),
        nn.BatchNorm1d(512),
        nn.Dropout(0.5),
        
        nn.Linear(512, 256),
        nn.ReLU(),
        nn.BatchNorm1d(256),
        nn.Dropout(0.5),
        
        nn.Linear(256, NUM_CLASSES))
    idc_clasifier.load_state_dict(torch.load(model, map_location=torch.device('cpu')))
    idc_clasifier.eval()
    return idc_clasifier

def predict(model: torch.nn, img_path:str) -> str:
    # read an image
    img = Image.open(img_path)
    convert_tensor = transforms.ToTensor()
    input = convert_tensor(img)
    input = input.unsqueeze(0)
    #must make into a 4d tensor

    outputs = model(input)
    print(outputs)

    _, preds = torch.max(outputs, 1)
    preds=preds.cpu().numpy()

    return str(preds[0])
