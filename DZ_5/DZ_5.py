# Для начала спроектируем базовую структуру классов для работы с медиафайлами.
# Будет абстрактный класс MediaFile, который будет содержать общие методы и свойства для всех типов медиа-файлов.
# Затем создадим наследуемые классы для конкретных типов медиа: AudioFile, VideoFile и ImageFile.
# Также предусмотрим возможность работы с различными хранилищами через интерфейс Storage.

# Базовый класс MediaFile

from abc import ABC, abstractmethod
import datetime


class MediaFile(ABC):
    def __init__(self, name: str, size: int, created_at: datetime.datetime, owner: str):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner

    @abstractmethod
    def save(self, storage: 'Storage') -> None:
        """Сохраняет файл в указанном хранилище."""
        pass

    @abstractmethod
    def delete(self, storage: 'Storage') -> None:
        """Удаляет файл из указанного хранилища."""
        pass

    @abstractmethod
    def extract_features(self) -> dict:
        """Извлекает характеристики файла."""
        pass

    @abstractmethod
    def convert_to_format(self, new_format: str) -> 'MediaFile':
        """Конвертирует файл в новый формат."""
        pass

    # Метод для обновления метаданных
    def update_metadata(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)

# Классы для различных типов медиа

# AudioFile

class AudioFile(MediaFile):
    def __init__(
        self,
        name: str,
        size: int,
        created_at: datetime.datetime,
        owner: str,
        duration: float,
        bitrate: int
    ):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.bitrate = bitrate

    def save(self, storage: 'Storage') -> None:
        # Реализация сохранения аудиофайла в хранилище
        print(f"Сохранение аудиофайла {self.name} в хранилище {storage}")

    def delete(self, storage: 'Storage'):
        # Реализация удаления аудиофайла из хранилища
        print(f"Удаление аудиофайла {self.name} из хранилища {storage}")

    def extract_features(self) -> dict:
        return {
            "duration": self.duration,
            "bitrate": self.bitrate
        }

    def convert_to_format(self, new_format: str) -> 'AudioFile':
        # Конвертируем аудиофайл в другой формат
        # Например, MP3 -> WAV
        return AudioFile(name=self.name + f".{new_format}", size=self.size, created_at=datetime.datetime.now(), owner=self.owner, duration=self.duration, bitrate=self.bitrate)

# VideoFile

class VideoFile(MediaFile):
    def __init__(
        self,
        name: str,
        size: int,
        created_at: datetime.datetime,
        owner: str,
        duration: float,
        resolution: tuple[int, int]
    ):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.resolution = resolution

    def save(self, storage: 'Storage') -> None:
        # Реализация сохранения видеофайла в хранилище
        print(f"Сохранение видеофайла {self.name} в хранилище {storage}")

    def delete(self, storage: 'Storage'):
        # Реализация удаления видеофайла из хранилища
        print(f"Удаление видеофайла {self.name} из хранилища {storage}")

    def extract_features(self) -> dict:
        return {
            "duration": self.duration,
            "resolution": self.resolution
        }

    def convert_to_format(self, new_format: str) -> 'VideoFile':
        # Конвертируем видеофайл в другой формат
        # Например, MP4 -> AVI
        return VideoFile(name=self.name + f".{new_format}", size=self.size, created_at=datetime.datetime.now(), owner=self.owner, duration=self.duration, resolution=self.resolution)

# ImageFile

class ImageFile(MediaFile):
    def __init__(
        self,
        name: str,
        size: int,
        created...