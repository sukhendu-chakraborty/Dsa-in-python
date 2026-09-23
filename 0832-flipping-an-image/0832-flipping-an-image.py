class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        l = len(image)
        r = len(image[0])
        for i in image:
            i.reverse()
        for j in range(l):
            for k in range(r):
                if image[j][k] == 1:
                    image[j][k] = 0
                else:
                    image[j][k] =1
        return image
        