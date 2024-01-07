def rectangle_area(width:int, height:int) -> int:
    return width * height


rectangle_width = int(input())
rectangle_height = int(input())
rectangle_area = rectangle_area(rectangle_width, rectangle_height)
print(rectangle_area)