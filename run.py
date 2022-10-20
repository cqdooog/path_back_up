from source import file_back
from source import settings

if __name__ == '__main__':
    file_back.run(src=settings.src, dsts=settings.dsts, filetype=settings.file_type)
