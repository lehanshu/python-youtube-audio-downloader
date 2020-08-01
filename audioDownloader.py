import pafy
url = "https://www.youtube.com/watch?v=Gqb7Xm-nigc"
result = pafy.new(url)
bestAudio = result.getbestaudio()
print(bestAudio)
bestAudio.download()