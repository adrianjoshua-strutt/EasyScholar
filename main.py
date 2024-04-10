from EasyScholar.Content.PublicationContent import PublicationContent

content = PublicationContent('Discriminative unsupervised feature learning with convolutional neural networks')

print(content.getDate()) # Output: 2014
print(content.getPublicationWebsite()) # Output: proceedings.neurips.cc
print(content.getPublicationUrl()) # Output: https://proceedings.neurips.cc/paper/2014/hash/07563a3fe3bbe7e3ba84431ad9d055af-Abstract.html