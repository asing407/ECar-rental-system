'''
Description: 
Author: uioll
Date: 2024-11-06 00:45:25
LastEditTime: 2024-11-06 00:58:40
LastEditors: uioll
'''
# your_app/management/commands/import_locations.py
from django.core.management.base import BaseCommand
from carrent.models import Location
import pandas as pd

class Command(BaseCommand):
    help = '从 locations.xls 文件中导入 Location 数据'

    def handle(self, *args, **kwargs):

        try:
            df = pd.read_excel('C:/Users/KAZHILI8/Desktop/location.xlsx')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"读取 Excel 文件时出错: {e}"))
            return



        required_columns = {'locationID', 'Position_x', 'Position_y'}
        if not required_columns.issubset(df.columns):
            self.stdout.write(self.style.ERROR("Excel 文件缺少必要的列。"))
            return


        locations = [
            Location(
                locationID=row['locationID'],
                address=row['address'],
                position_x=row['Position_x'],
                position_y=row['Position_y']
            )
            for _, row in df.iterrows()
        ]


        try:
            Location.objects.bulk_create(locations)
            self.stdout.write(self.style.SUCCESS(f"成功导入 {len(locations)} 条 Location 记录。"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"批量插入数据时出错: {e}"))
