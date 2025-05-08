from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
import numpy as np

def generate_color_gradient(start_color, end_color, num_colors):
    # 将RGB元组转换为Lab颜色空间（感知线性）
    def rgb_to_lab(rgb):
        return convert_color(sRGBColor(*[x / 255.0 for x in rgb], is_upscaled=False), LabColor)

    def lab_to_rgb(lab):
        rgb = convert_color(lab, sRGBColor)
        return tuple(int(x * 255) for x in (rgb.rgb_r, rgb.rgb_g, rgb.rgb_b))

    start_lab = rgb_to_lab(start_color)
    end_lab = rgb_to_lab(end_color)

    gradient = []
    for i in range(num_colors):
        t = i / (num_colors - 1)
        # 线性插值Lab空间的L、a、b通道
        l = start_lab.lab_l + (end_lab.lab_l - start_lab.lab_l) * t
        a = start_lab.lab_a + (end_lab.lab_a - start_lab.lab_a) * t
        b = start_lab.lab_b + (end_lab.lab_b - start_lab.lab_b) * t
        rgb = lab_to_rgb(LabColor(l, a, b))
        # 限制RGB值在[0,255]范围内
        rgb_clamped = tuple(np.clip(int(c), 0, 255) for c in rgb)
        gradient.append(rgb_clamped)

    return gradient
