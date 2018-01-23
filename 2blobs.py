from random import seed
from fontTools.pens.basePen import BasePen


rad = width()/4

nFrames=40

class BezierPathPen(BasePen):
    """FontTools pen -> BezierPath adapter."""
    def __init__(self, glyphSet, bezPath):
        super(BezierPathPen, self).__init__(glyphSet)
        self.bezPath = bezPath
    def _moveTo(self, pt):
        self.bezPath.moveTo(pt)
    def _lineTo(self, pt):
        self.bezPath.lineTo(pt)
    def _curveToOne(self, pt1, pt2, pt3):
        self.bezPath.curveTo(pt1, pt2, pt3)
    def _closePath(self):
        self.bezPath.closePath()

numPoints=6

randomPhases = [(2 * pi * random(), choice([-1, 1])) for i in range(numPoints)]

blobRadius=100

def varyPoint(pt, radius, phase):
    transx, transy = pt
    dx = radius * cos(phase)
    dy = radius * sin(phase)
    translate(transx,transy)
    return transx + dx, transy + dy
    
def drawBlob(blobPhase, blobRadius):
    points = []  # list of off curve points forming the blob.
    for i in range(numPoints):
        a = 2 * pi * i / numPoints
        x = blobRadius * cos(a)
        y = blobRadius * sin(a)
        rPhase, rSign = randomPhases[i]
        points.append(varyPoint((x, y), 0.2 * blobRadius, rPhase + rSign * 2 * pi * blobPhase))
    # Add a final 'fake' point, to tell the pen there is *no* on curve point at all
    points.append(None)
    bezPath = BezierPath()
    p = BezierPathPen(None, bezPath)
    p.qCurveTo(*points)
    p.closePath()
    drawPath(bezPath)

nBlobs=20 #why can't this be 1 without being too small?

r,g,b = 141, 130, 155

r,g,b = r/255, g/255 , b/255

r2,g2,b2 = 142, 141, 126

r2,g2,b2 = r2/255, g2/255 , b2/255


for frame in range(nFrames):
    framePhase = frame / nFrames
    newPage(500,500)
    frameDuration(1/20)
    fill(r,g,b)
    rect(0,0,width(), height())
    strokeWidth(15)
    stroke(0)
    fill(r2,g2,b2)
    translate(width()/6, height()/6)
    seed=1
    for i in range(nBlobs):
        blobPhase = i / nBlobs
        radius = 5 + i * 14
        drawBlob(framePhase + blobPhase * 0.7, radius)
    seed=0 #any other way to get different movement for each blob?
    translate(width(), height()/2)
    for i in range(nBlobs):
        blobPhase = i / nBlobs
        radius = 5 + i * 14
        drawBlob(framePhase + blobPhase * 0.7, radius)

saveImage("2blobs.gif")

#special thanks to Just for writing the original code: https://gist.github.com/justvanrossum/b65f4305ffcf2690bc65
