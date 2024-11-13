'''
Description: 
Author: uioll
Date: 2024-11-06 00:45:25
LastEditTime: 2024-11-06 01:37:18
LastEditors: uioll
'''
# your_app/management/commands/import_vehicle.py
from django.core.management.base import BaseCommand
from carrent.models import Vehicle,Location
import pandas as pd

class Command(BaseCommand):
    help = '从 vehicle.xls 文件中导入 vehicle 数据'

    def handle(self, *args, **kwargs):
        try:
            df = pd.read_excel('C:/Users/KAZHILI8/Desktop/vehicle.xls')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"读取 Excel 文件时出错: {e}"))
            return

        vehicles = []
        for _, row in df.iterrows():
            try:
                location_instance = Location.objects.get(locationID=row['location'])
                vehicle = Vehicle(
                    type=row['type'],
                    batteryStatus=row['batteryStatus'],
                    location=location_instance,
                    isDefective=row['isDefective'],
                    cost_per_minute=row['cost_per_minute'],
                    position_x=row['position_x'],
                    position_y=row['position_y'],
                    range=row['range']
                )
                vehicles.append(vehicle)
            except Location.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"未找到 ID 为 {row['location']} 的 Location 实例，跳过该行记录"))
        try:
            Vehicle.objects.bulk_create(vehicles)
            self.stdout.write(self.style.SUCCESS(f"成功导入 {len(vehicles)} 条 Vehicle 记录。"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"批量插入数据时出错: {e}"))