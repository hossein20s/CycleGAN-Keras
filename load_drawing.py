from quickdraw import QuickDrawData

if __name__ == '__main__':
    quickdraw = QuickDrawData()
    print(quickdraw.drawing_names)
    n = 3
    for i in range(n*2):
        draw = quickdraw.get_drawing("bicycle")
        draw.image.save("data/trainA/train_bicycle{}.gif".format(i))
    for i in range(n):
        draw = quickdraw.get_drawing("bicycle")
        draw.image.save("data/testA/test_bicycle{}.gif".format(i))
    for i in range(n*2):
        draw = quickdraw.get_drawing("campfire")
        draw.image.save("data/trainB/train_campfire{}.gif".format(i))
    for i in range(n):
        draw = quickdraw.get_drawing("campfire")
        draw.image.save("data/testB/test_campfire{}.gif".format(i))
