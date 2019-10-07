# -*- coding: utf-8; -*-

from libqtile import widget
from libqtile.widget.battery import BatteryState, BatteryStatus


class Backlight(widget.Backlight):
    def poll(self):
        info = self._get_info()
        if info is False:
            return '---'
        no = int(info['brightness'] / info['max'] * 9.999)
        char = '☼'
        # self.layout.colour = color_alert
        return '{}{}'.format(char, no)  # chr(0x1F50B))


class Battery(widget.Battery):
    def __init__(self, **kwargs):
        self.short_format = kwargs.pop('short_format')
        self.high_foreground = kwargs.pop('high_foreground')
        super().__init__(**kwargs)
        self.normal_format = kwargs['format']
        self.normal_foreground = self.foreground

    def build_string(self, status):
        status = BatteryStatus(status.state, int(status.percent*10),
                               status.power, status.time)
        if status.state in [BatteryState.EMPTY,
                            BatteryState.FULL,
                            BatteryState.UNKNOWN]:
            self.format = self.short_format
        else:
            self.format = self.normal_format
        if self.layout is not None:
            if any((status.state == BatteryState.CHARGING,
                    status.state == BatteryState.DISCHARGING
                    and status.percent >= 7)):
                self.foreground = self.high_foreground
            elif all((status.state == BatteryState.DISCHARGING,
                      status.percent <= 2)):
                self.foreground = self.low_foreground
            else:
                self.foreground = self.normal_foreground
        return super().build_string(status)


class ThermalSensor(widget.ThermalSensor):
    def poll(self):
        temp_values = self.get_temp_sensors()
        if temp_values is None:
            return '---'
        no = int(float(temp_values.get(self.tag_sensor, [0])[0]))
        return '{}{}'.format(no, '°')  # chr(0x1F321))


class Volume(widget.Volume):
    def update(self):
        vol = self.get_volume()
        if vol != self.volume:
            self.volume = vol
            if vol < 0:
                no = '0'
            else:
                no = int(vol / 100 * 9.999)
            char = '♬'
            self.text = '{}{}{}'.format(char, no, 'V')  # chr(0x1F508))
