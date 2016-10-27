import os
import shutil

from django.conf import settings
from reader.models import Regions, Countries


class Utils:

    # Clear media directory from previous uploaded file
    @staticmethod
    def clear_media():
        folder = settings.MEDIA_ROOT
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    @staticmethod
    def put_all_to_db(file_name):
        # Open file only for riding
        file = open(file_name, 'r')
        file_strings = file.read()
        parsing_file = file_strings.split('\n')
        current = ''
        region = Regions
        for line in parsing_file:
            # Check for empty lines
            if len(line) > 0:
                tmp_line = line.split(',')
                # Check value type of parameter
                try:
                    int(tmp_line[2])
                except ValueError:
                    continue
                if current == tmp_line[0]:
                    country = Countries(region=region, name=tmp_line[1], parameter=tmp_line[2])
                    country.save()
                else:
                    region = Regions(name=tmp_line[0])
                    region.save()
                    country = Countries(region=region, name=tmp_line[1], parameter=tmp_line[2])
                    country.save()
                    current = tmp_line[0]
        file.close()
        return region
