from pbx_component_files_uploader.uploader import Uploader

if __name__ == '__main__':
    api = Uploader(Uploader.STORAGE_SELECTEL, {
        'username': 'user',
        'password': 'pass',
        'container': 'tmp'
    }, {
        'token_cache_dir': 'tmp'
    })

    uploadedFileUrl = api.upload('test.txt', 'test.txt')
