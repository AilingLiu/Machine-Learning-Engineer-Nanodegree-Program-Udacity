# Import pretrained model
ResNet50 = models.resnet50(pretrained=True)

if use_cuda:
    ResNet50.cuda()

# Performance variables
dogs_in_human_files_ResNet50 = 0
dogs_in_dog_files_ResNet50 = 0

# Preprocess definitions
normalize = transforms.Normalize(mean=(0.485, 0.456, 0.406),
                                 std=(0.229, 0.224, 0.225))
preprocess = transforms.Compose([transforms.Resize(256),
                                 transforms.CenterCrop(224),
                                 transforms.ToTensor(),
                                 normalize])
# Turn on evaluation mode
ResNet50.eval()

# Test performance of ResNet50 model on human_files_short
for img_path in tqdm_notebook(human_files_short, desc='human_files'):
    img = Image.open(img_path)
    img_tensor = preprocess(img).unsqueeze_(0)
    if use_cuda:
        img_tensor = img_tensor.cuda()

    with torch.no_grad():
        output_ResNet50 = ResNet50(img_tensor)
        prediction_ResNet50 = torch.argmax(output_ResNet50).item()
        if 151 <= prediction_ResNet50 <= 268:
            dogs_in_human_files_ResNet50 += 1

# Test performance of ResNet50 model on dogs_files_short
for img_path in tqdm_notebook(dog_files_short, desc='dog_files'):
    img = Image.open(img_path)
    img_tensor = preprocess(img).unsqueeze_(0)
    if use_cuda:
        img_tensor = image_tensor.cuda

    with torch.no_grad():
        output_ResNet50 = ResNet50(img_tensor)
        prediction_ResNet50 = torch.argmax(output_ResNet50).item()
        if 151 <= prediction_ResNet50 <= 268:
            dogs_in_dog_files_ResNet50 += 1

ResNet50.train()

print('#### ResNet50 ####')
print(f'Dogs detected in "human_files_short": {dogs_in_human_files_ResNet50 / len(human_files_short) * 100}%')
print(f'Dogs detected in "dog_files_short": {dogs_in_dog_files_ResNet50 / len(human_files_short) * 100}%')
