import torch

CONFIG = {
    'device': torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
    'detr_model_path': 'facebook/detr-resnet-101',
    'glpn_model_path': 'vinvino02/glpn-kitti',
    'lstm_model_path': 'data/models/pretrained_lstm.pth',
    'lstm_scaler_path': 'data/models/lstm_scaler.pkl',
}
