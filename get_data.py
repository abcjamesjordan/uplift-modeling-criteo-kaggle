import kaggle
import os

path = os.getcwd()
path_for_data = os.path.join(path, 'data')

kaggle.api.authenticate()

kaggle.api.dataset_download_files('arashnic/uplift-modeling', path=path_for_data, unzip=True)
print('All done!')