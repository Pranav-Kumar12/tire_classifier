import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.GRAYSCALE)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((240,240))
sensor.skip_frames(time=2000)

clock=time.clock()

while(True):
    clock.tick()
    img= sensor.snapshot # gets iamge.
    # other filters of parallax and distortion not needed as of now.
    print(clock.fps())